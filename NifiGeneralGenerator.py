from tokenize import group
from py import process
from pytest import param
import os, json, re, sys
import logging
import helper

# Created by : Akbar - 2022/11/10
# supported format : InvokeHTTP, LogAttribute
# for general format should be  :
#  [{
#       "group_name" : "",
#       "state" : "",
#       "processor"  : {
#                   "InvokeHTTP" : {
#                                       .....
#                                  },
#                   "LogAttribue" : [...],
#       }
#
#  }]
#
#
logging.basicConfig(
    format='%(asctime)-15s: %(name)s - %(levelname)s: %(message)s')
LOGGER = logging.getLogger('connectors-deploy')
LOGGER.setLevel(logging.INFO)

class Generator:

    def __init__(self, env):

        # postgres config
        self.configs = helper.getDatamartPostgresKloposBetaUrl() if env == "stagging" else helper.getDatamartPostgresKloposProdUrl()
        
        if env == "production":
            from Model import DatamartModel as Nifi
        else:
            from Model import Beta_DatamartModel as Nifi

        if 'Model.DatamartModel' in sys.modules:
            LOGGER.info("production models has been imported") 

        if 'Model.Beta_DatamartModel' in sys.modules:
            LOGGER.info("beta models has been imported") 

        self.nifi = Nifi
        self.url = self.configs["url"]
        self.port = self.configs["port"]

        # general env configs
        self.generals_configs = helper.getUrls()

        self.config_ext  = "json"


    def generateConfigs(self, resources ,params, headers = None, environment = "BETA"):
        params["deployment_environment"] = environment
        dir = "{}/configs/{}".format(os.getcwd(), environment.lower())
        LOGGER.info("going to create from {} file(s)".format(len(os.listdir(dir))))
        for file in os.listdir(dir): # find files
            LOGGER.info("Reading config file : {}....".format(file))
            if(file[-4:] != self.config_ext): # if not json then skip
                continue

            # open file
            with open("{dir}/{filename}".format(dir = dir, filename = file), "r") as jsonfile:
                json_object = json.load(jsonfile) # parse as json object
                pos_y = json_object["y-axis"]
                pos_x = json_object["x-axis"] if "x-axis" in json_object else 0
                configs = json_object["configs"]
                is_postgres = "type" in json_object and json_object["type"] == "postgresql"


                for config in configs: # iterate through each group creation
                    ifExist = self._checkIfGroupExist(config["group_name"],resources)
                    if(not ifExist):
                    # if not exist then create
                        LOGGER.info("Creating {group_name}....".format(group_name=config["group_name"]))
                        group_id = self._createGroup(params, headers, config["group_name"], pos_x, pos_y)
                        for processor in config["processor"].keys():
                            if(processor == "InvokeHTTP"):
                                self._createInvokeHTTP(params, headers,group_id, config["processor"][processor], is_postgres = is_postgres)


                        LOGGER.info("{group_name} successfully created....".format(group_name=config["group_name"]))
                        self._changeGroupState(params, headers, group_id, config["state"])
                        LOGGER.info("Current {group_name}'s state is {state} ....".format(group_name=config["group_name"], state=config["state"]))
                    else:
                        LOGGER.info("{group_name} already exist, skipping...".format(group_name=config["group_name"]))
                    pos_x += 400 # if already exist, skip to next coordinates

        LOGGER.info("Finished generating from all configs given..")

    def _checkIfGroupExist(self, group_name:str, existing):
        for resource in existing["resources"]:
            if resource["name"] == group_name:
                return True
        return False

    def _createGroup(self,params, headers, group_name:str , pos_x = 0, pos_y = 0):
        return self.nifi.processGroup(params, headers, { "client_id" : params["client_id"], "pg_name" :group_name, "pos_x" : pos_x, "pos_y" :pos_y })

    def _changeGroupState(self,params, headers, group_id , state):
        self.nifi.change_pg_state(params, headers, group_id, state)

    def _createInvokeHTTP(self, params, headers, group_id, data:dict, is_postgres = False):
        data["client_id"] = data["client_id"].format(client_id = params["client_id"])
        http_id = None
        urlLiteral = [key.lower() for key in re.findall(r'{(.*?)}',  data["remote_url"])]
        
        if set(urlLiteral) == set(['url', 'port']):
            # if using basic URL & PORT configs
            data["remote_url"] = data["remote_url"].format(url = self.url, port = self.port)

        else:
            # if custom url & ports
                # to cover if we add new VM, so assign it dynamically
            data["remote_url"] = data["remote_url"].format(**self.generals_configs)

        http_id = self.nifi.precessorInvokeHTTP(params, headers, group_id, data)

        predecessors = data["on"]
        del data["on"]
        for predecessor in predecessors.keys():
            if(predecessors[predecessor] == "LogAttribute"):
                self._createAndConnectLogAtrribue(params, headers, group_id, http_id, predecessor)

    def _createAndConnectLogAtrribue(self, params, headers, group_id , http_id , logtype:str):
        log_id = self._createLogAttribute(params, headers, group_id , logtype=logtype)
        return self._connectProcessor(params, headers, group_id, http_id, log_id, connection_type=logtype)


    def _createLogAttribute(self, params, headers, group_id, logtype:str = "original"):
        if logtype == "original":
            return self.nifi.processorLogAttribute_original(params, headers, group_id)
        elif logtype == "failure":
            return self.nifi.processorLogAttribute_failure(params, headers, group_id)
        elif logtype == "no_retry":
            return self.nifi.processorLogAttribute_no_retry(params, headers, group_id)
        elif logtype == "response":
            return self.nifi.processorLogAttribute_response(params, headers, group_id)
        else:
            return self.nifi.processorLogAttribute_retry(params, headers, group_id)

    def _connectProcessor(self, params, headers, group_id, current_id, destination_id, connection_type:str="original"):
        if connection_type == "original":
            return self.nifi.connection_original(params, headers, group_id, current_id, destination_id )
        elif connection_type == "failure":
            return self.nifi.connection_failure(params, headers, group_id, current_id, destination_id )
        elif connection_type == "no_retry":
            return self.nifi.connection_no_retry(params, headers, group_id, current_id, destination_id )
        elif connection_type == "response":
            return self.nifi.connection_response(params, headers, group_id, current_id, destination_id )
        else:
            return self.nifi.connection_retry(params, headers, group_id, current_id, destination_id )
