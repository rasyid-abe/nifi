import requests
import json
import helper

conf = helper.getConfNifi()

def processGroup(params, headers, data):
    obj = obj_process_group(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(params['root_pg_id'])}/process-groups"
    act = requests.post(url, json = obj, headers=headers)
    json_pg = json.loads(act.text)
    return json_pg['id']

def precessorInvokeHTTP(params, headers, pg_id, data):
    obj = obj_invokeHttp(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/processors"
    act = requests.post(url, json = obj, headers=headers)
    http = json.loads(act.text)
    return http['id']

def processorLogAttribute_original(params, headers, pg_id):
    data = {
        'client_id': params['client_id'],
        'pos_x' : 0,
        'pos_y' : 0,
    }

    obj = obj_logAttribute(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/processors"
    act = requests.post(url, json = obj, headers=headers)
    attr_original = json.loads(act.text)
    return attr_original['id']

def connection_original(params, headers, pg_id, source_id, destination_id):
    data = {
        'client_id': params['client_id'],
        'pg_id': pg_id,
        'source': source_id,
        'destination': destination_id,
        'relation': 'Original'
    }

    obj = obj_connection(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/connections"
    act = requests.post(url, json = obj, headers=headers)
    conn_original = json.loads(act.text)
    return conn_original['id']

def processorLogAttribute_retry(params, headers, pg_id):
    data = {
        'client_id': params['client_id'],
        'pos_x' : -700,
        'pos_y' : 0,
    }

    obj = obj_logAttribute(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/processors"
    act = requests.post(url, json = obj, headers=headers)
    attr_retry = json.loads(act.text)
    return attr_retry['id']

def connection_retry(params, headers, pg_id, source_id, destination_id):
    data = {
        'client_id': params['client_id'],
        'pg_id': pg_id,
        'source': source_id,
        'destination': destination_id,
        'relation': 'Retry'
    }

    obj = obj_connection(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/connections"
    act = requests.post(url, json = obj, headers=headers)
    conn_retry = json.loads(act.text)
    return conn_retry['id']

def processorLogAttribute_failure(params, headers, pg_id):
    data = {
        'client_id': params['client_id'],
        'pos_x' : -700,
        'pos_y' : 300,
    }

    obj = obj_logAttribute(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/processors"
    act = requests.post(url, json = obj, headers=headers)
    attr_failure = json.loads(act.text)
    return attr_failure['id']

def connection_failure(params, headers, pg_id, source_id, destination_id):
    data = {
        'client_id': params['client_id'],
        'pg_id': pg_id,
        'source': source_id,
        'destination': destination_id,
        'relation': 'Failure'
    }

    obj = obj_connection(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/connections"
    act = requests.post(url, json = obj, headers=headers)
    conn_failure = json.loads(act.text)
    return conn_failure['id']

def processorLogAttribute_response(params, headers, pg_id):
    data = {
        'client_id': params['client_id'],
        'pos_x' : 700,
        'pos_y' : 300,
    }

    obj = obj_logAttribute(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/processors"
    act = requests.post(url, json = obj, headers=headers)
    attr_response = json.loads(act.text)
    return attr_response['id']

def connection_response(params, headers, pg_id, source_id, destination_id):
    data = {
        'client_id': params['client_id'],
        'pg_id': pg_id,
        'source': source_id,
        'destination': destination_id,
        'relation': 'Response'
    }

    obj = obj_connection(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/connections"
    act = requests.post(url, json = obj, headers=headers)
    conn_response = json.loads(act.text)
    return conn_response['id']

def processorLogAttribute_no_retry(params, headers, pg_id):
    data = {
        'client_id': params['client_id'],
        'pos_x' : 700,
        'pos_y' : 0,
    }

    obj = obj_logAttribute(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/processors"
    act = requests.post(url, json = obj, headers=headers)
    attr_no_retry = json.loads(act.text)
    return attr_no_retry['id']

def connection_no_retry(params, headers, pg_id, source_id, destination_id):
    data = {
        'client_id': params['client_id'],
        'pg_id': pg_id,
        'source': source_id,
        'destination': destination_id,
        'relation': 'No Retry'
    }

    obj = obj_connection(data)
    url = f"http://{conf['host']}/nifi-api/process-groups/{str(pg_id)}/connections"
    act = requests.post(url, json = obj, headers=headers)
    conn_no_retry = json.loads(act.text)
    return conn_no_retry['id']

def obj_process_group(p):
    return {
        "revision":{
            "clientId":str(p['client_id']),
            "version":0
        },
        "component":{
            "name":p['pg_name'],
            "position":{
                "x":p['pos_x'],
                "y":p['pos_y']
            }
        }
    }

def obj_invokeHttp(p):
    return {
        "revision": {
            "clientId": str(p['client_id']),
            "version": 0
        },
        "component": {
            "type": "org.apache.nifi.processors.standard.InvokeHTTP",
            "name": p['http_name'],
            "position": {
                "x": p['pos_x'],
                "y": p['pos_y']
            },
            "config": {
                "schedulingStrategy": p['schedulingStrategy'],
                "schedulingPeriod": p['run_scheduler'],
                "executionNode": p['executionNode'],
                "concurrentlySchedulableTaskCount": p['concurrentlySchedulableTaskCount'],
                "runDurationMillis": p['runDurationMillis'],
                "properties": {
                    "max-idle-connections": p['max_idle_connection'],
                    "idle-timeout": p['idle-timeout'],
                    "HTTP Method": p['http_method'],
                    "Remote URL": p['remote_url'],
                    "Connection Timeout": p['connection_timeout'],
                    "Read Timeout": p['read_timeout'],
                },
                "penaltyDuration": p['penaltyDuration'],
                "yieldDuration": p['yieldDuration'],
                "bulletinLevel": p['bulletinLevel'],
            }
        }
    }

def obj_logAttribute(p):
    return {
        "revision": {
            "clientId": str(p['client_id']),
            "version": 0
        },
        "component": {
            "type": "org.apache.nifi.processors.standard.LogAttribute",
            "name": "LogAttribute",
            "position": {
                "x": p['pos_x'],
                "y": p['pos_y']
            },
            "config": {
                "schedulingPeriod": "0 sec",
                "autoTerminatedRelationships":["success"]
            }
        }
    }

def obj_connection(p):
    return {
        "revision": {
            "clientId": str(p['client_id']),
            "version": 0
        },
        "component": {
            "name": "",
            "source": {
                "id": str(p['source']),
                "groupId": str(p['pg_id']),
                "type": "PROCESSOR"
            },
            "destination": {
                "id": str(p['destination']),
                "groupId": str(p['pg_id']),
                "type": "PROCESSOR"
            },
            "selectedRelationships": [p['relation']],
        }
    }

def change_pg_state(params, headers, proc_id, state):
    obj = {"id":str(proc_id),"state":state}
    url = f"http://{conf['host']}/nifi-api/flow/process-groups/{proc_id}"
    act = requests.put(url, json = obj, headers=headers)
    print(state)
