import requests
import json
import uuid
import helper
from NifiGeneralGenerator import Generator
import argparse

def deploy_beta():
    from Controller import Beta_NiFiValidity, Beta_NiFiRecovery, Beta_NiFiDatamartBusiestItemTimePostgres
    conf = helper.getConfNifi_beta()
    client_id = uuid.uuid4()

    head_tok = {
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
    }

    data_tok = {
        'username': conf['user'],
        'password': conf['pass'],
    }

    res_tok = requests.post(f"https://{conf['host']}/nifi-api/access/token", headers=head_tok, data=data_tok)
    token = res_tok.text

    headers = {
        # 'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }

    res = requests.get(f"https://{conf['host']}/nifi-api/resources", headers=headers)
    pg_name = 'NiFi Flow'

    root_pg_id = ''
    resource = json.loads(res.text)
    for x in resource['resources']:
        if ((x['name'] == pg_name) and ("/process-groups/" in x['identifier'])):
            pgid = x['identifier'].split('/')
            root_pg_id = pgid[-1]

    params = {
        'client_id' : client_id,
        'root_pg_id' : root_pg_id,
    }

    ## NEW NIFI CONFIGURATION
    Generator("stagging").generateConfigs(resource, params, headers=headers, environment="BETA")

    ## X DISTANCE 400
    ## Y DISTANCE 200

    ## STATE PROCESSOR = RUNNING, STOPPED OR DISABLED

    Beta_NiFiDatamartBusiestItemTimePostgres.sequence5min(resource, params, headers, 'STOPPED', x=0, y=1800)


def deploy_prod():
    from Controller import \
        NiFiRecovery, \
        NiFiValidity

    conf = helper.getConfNifi()
    client_id = uuid.uuid4()

    head_tok = {
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
    }

    data_tok = {
        'username': conf['user'],
        'password': conf['pass'],
    }

    res_tok = requests.post(f"https://{conf['host']}/nifi-api/access/token", headers=head_tok, data=data_tok)
    token = res_tok.text

    headers = {
        # 'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }

    res = requests.get(f"https://{conf['host']}/nifi-api/resources", headers=headers)
    pg_name = 'NiFi Flow'

    root_pg_id = ''
    resource = json.loads(res.text)
    for x in resource['resources']:
        if ((x['name'] == pg_name) and ("/process-groups/" in x['identifier'])):
            pgid = x['identifier'].split('/')
            root_pg_id = pgid[-1]

    params = {
        'client_id' : client_id,
        'root_pg_id' : root_pg_id,
    }


    # X DISTANCE 400
    # Y DISTANCE 200
    # NEW NIFI CONFIGURATION
    Generator("production").generateConfigs(resource, params, headers=headers, environment="PROD")


## RUN SCRIPTS
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', help='environment variable (stagging/prod)', required=True)
    args = parser.parse_args()

    env = args.env
    print(f"Deploying at {env}")
    if env == "stagging":
        deploy_beta()
    elif env == "production":
        deploy_prod()
