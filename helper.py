from dotenv import dotenv_values
import json

config = dotenv_values(".env")

def getConfNifi_beta():
    return {
        "host": str(config['HOST_BETA']),
        "user": str(config['USER_BETA']),
        "pass": str(config['PASS_BETA']),
    }

def getConfNifi():
    return {
        "host": str(config['HOST_PROD']),
        "user": str(config['USER_PROD']),
        "pass": str(config['PASS_PROD']),
    }

def getDatamartKloposBetaUrl():
    return {
        "url" : config["KLOPOS_URL_BETA"] if "KLOPOS_URL_BETA" in config else "localhost",
        "port" : config["KLOPOS_PORT_BETA"] if "KLOPOS_PORT_BETA" in config else "8001"
    }

def getDatamartKloposProdUrl():
    return {
        "url" : config["KLOPOS_URL_PROD"] if "KLOPOS_URL_PROD" in config else "localhost",
        "port" : config["KLOPOS_PORT_PROD"] if "KLOPOS_PORT_PROD" in config else "8001"
    }

def getDatamartPostgresKloposBetaUrl():
    return {
        "url" : config["KLOPOS_URL_BETA_POSTGRES"] if "KLOPOS_URL_BETA_POSTGRES" in config else "localhost",
        "port" : config["KLOPOS_PORT_BETA_POSTGRES"] if "KLOPOS_PORT_BETA_POSTGRES" in config else "8001"
    }

def getDatamartPostgresKloposProdUrl():
    return {
        "url" : config["KLOPOS_URL_PROD_POSTGRES"] if "KLOPOS_URL_PROD_POSTGRES" in config else "localhost",
        "port" : config["KLOPOS_PORT_PROD_POSTGRES"] if "KLOPOS_PORT_PROD_POSTGRES" in config else "8001"
    }

def getUrls():
    settings = {}
    for key in config:
        if 'URL' in key or 'PORT' in key:
            settings[key.lower()] = config[key]
    return settings


#
# def getConfNifi_prod():
#     return {
#         "host": str(config['HOST_PROD']),
#         "port": str(config['PORT_PROD']),
#     }
