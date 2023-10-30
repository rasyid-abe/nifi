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

    res_tok = requests.post(f"https://{conf['host']}/nifi-api/access/token", verify=False, headers=head_tok, data=data_tok)
    token = res_tok.text


    headers = {
        # 'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
    }

    res = requests.get(f"https://{conf['host']}/nifi-api/resources", verify=False, headers=headers)
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

    #
    # ## NEW NIFI CONFIGURATION
    # # Generator("stagging").generateConfigs(resource, params, headers=headers, environment="BETA")
    #
    # ## X DISTANCE 400
    # ## Y DISTANCE 200
    #
    # ## STATE PROCESSOR = RUNNING, STOPPED OR DISABLED
    #
    Beta_NiFiRecovery.recoveryVarian(resource, params, headers, 'STOPPED', x=0, y=-600) #
    Beta_NiFiRecovery.recoveryProduk(resource, params, headers, 'STOPPED', x=400, y=-600) #
    Beta_NiFiRecovery.recoverySubVarian(resource, params, headers, 'STOPPED', x=800, y=-600) #
    Beta_NiFiRecovery.recoveryAkunting(resource, params, headers, 'STOPPED', x=1200, y=-600) #
    Beta_NiFiRecovery.recoveryBusiestItemTime(resource, params, headers, 'STOPPED', x=1600, y=-600) #
    Beta_NiFiRecovery.recoveryCompliment(resource, params, headers, 'STOPPED', x=2000, y=-600) #
    Beta_NiFiRecovery.recoveryOutletSales(resource, params, headers, 'STOPPED', x=2400, y=-600) #
    Beta_NiFiRecovery.recoveryProductSales(resource, params, headers, 'STOPPED', x=2800, y=-600) #
    Beta_NiFiRecovery.recoverySummaryReservation(resource, params, headers, 'STOPPED', x=3200, y=-600) #
    Beta_NiFiRecovery.recoveryTransactionType(resource, params, headers, 'STOPPED', x=3600, y=-600) #
    Beta_NiFiRecovery.recoveryUtilization(resource, params, headers, 'STOPPED', x=4000, y=-600) #

    Beta_NiFiValidity.validityVarian(resource, params, headers, 'RUNNING', x=0, y=-400) #
    Beta_NiFiValidity.validitySubVarian(resource, params, headers, 'RUNNING', x=400, y=-400)
    Beta_NiFiValidity.validityProduk(resource, params, headers, 'RUNNING', x=800, y=-400)
    Beta_NiFiValidity.validityAkunting(resource, params, headers, 'RUNNING', x=1200, y=-400)
    Beta_NiFiValidity.validityCDC(resource, params, headers, 'STOPPED', x=1600, y=-400)
    Beta_NiFiValidity.validityBusiestItemTime(resource, params, headers, 'RUNNING', x=2000, y=-400)
    Beta_NiFiValidity.validityCompliment(resource, params, headers, 'RUNNING', x=2400, y=-400)
    Beta_NiFiValidity.validityOutletSales(resource, params, headers, 'RUNNING', x=2800, y=-400)
    Beta_NiFiValidity.validityProductSales(resource, params, headers, 'RUNNING', x=3200, y=-400)
    Beta_NiFiValidity.validitySummaryReservation(resource, params, headers, 'RUNNING', x=3600, y=-400)
    Beta_NiFiValidity.validityTransactionType(resource, params, headers, 'RUNNING', x=4000, y=-400)
    Beta_NiFiValidity.validityUtilization(resource, params, headers, 'RUNNING', x=4400, y=-400)

    # Beta_NiFiDatamartBusiestItemTimePostgres.sequence5min(resource, params, headers, 'STOPPED', x=0, y=1800)


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

    ## STATE PROCESSOR = RUNNING, STOPPED OR DISABLED
    NiFiValidity.validityVarian(resource, params, headers, 'RUNNING', x=0, y=-600)
    NiFiValidity.validitySubVarian(resource, params, headers, 'RUNNING', x=400, y=-600)
    NiFiValidity.validityProduk(resource, params, headers, 'RUNNING', x=800, y=-600)
    NiFiValidity.validityAkunting(resource, params, headers, 'RUNNING', x=1200, y=-600)
    NiFiValidity.validityCdc(resource, params, headers, 'STOPPED', x=1600, y=-600)
    NiFiValidity.validityBusiestItemTime(resource, params, headers, 'STOPPED', x=2000, y=-400)
    NiFiValidity.validityCompliment(resource, params, headers, 'STOPPED', x=2400, y=-400)
    NiFiValidity.validityOutletSales(resource, params, headers, 'STOPPED', x=2800, y=-400)
    NiFiValidity.validityProductSales(resource, params, headers, 'STOPPED', x=3200, y=-400)
    NiFiValidity.validitySummaryReservation(resource, params, headers, 'STOPPED', x=3600, y=-400)
    NiFiValidity.validityTransactionType(resource, params, headers, 'STOPPED', x=4000, y=-400)
    NiFiValidity.validityUtilization(resource, params, headers, 'STOPPED', x=4400, y=-400)

    NiFiRecovery.recoveryVarian(resource, params, headers, 'STOPPED', x=0, y=-400) #
    NiFiRecovery.recoveryProduk(resource, params, headers, 'STOPPED', x=400, y=-400) #
    NiFiRecovery.recoverySubVarian(resource, params, headers, 'STOPPED', x=800, y=-400) #
    NiFiRecovery.recoveryAkunting(resource, params, headers, 'STOPPED', x=1200, y=-400) #
    NiFiRecovery.recoveryBusiestItemTime(resource, params, headers, 'STOPPED', x=1600, y=-600) #
    NiFiRecovery.recoveryCompliment(resource, params, headers, 'STOPPED', x=2000, y=-600) #
    NiFiRecovery.recoveryOutletSales(resource, params, headers, 'STOPPED', x=2400, y=-600) #
    NiFiRecovery.recoveryProductSales(resource, params, headers, 'STOPPED', x=2800, y=-600) #
    NiFiRecovery.recoverySummaryReservation(resource, params, headers, 'STOPPED', x=3200, y=-600) #
    NiFiRecovery.recoveryTransactionType(resource, params, headers, 'STOPPED', x=3600, y=-600) #
    NiFiRecovery.recoveryUtilization(resource, params, headers, 'STOPPED', x=4000, y=-600) #

    # Postgres

    # NiFiDatamartSalesItemPostgres.sequence15min(resource, params, headers, 'STOPPED', x=0, y=1200)
    #
    # NiFiDatamartSalesAddonPostgres.sequence5min(resource, params, headers, 'RUNNING', x=0, y=1400)

    # NiFiDatamartAkuntingPostgres.sequence5min(resource, params, headers, 'STOPPED', x=0, y=2000)

## RUN SCRIPTS
if __name__ == "__main__":
    deploy_beta()
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--env', help='environment variable (stagging/prod)', required=True)
    # args = parser.parse_args()
    #
    # env = args.env
    # print(f"Deploying at {env}")
    # if env == "stagging":
    #     deploy_beta()
    # elif env == "production":
    #     deploy_prod()
