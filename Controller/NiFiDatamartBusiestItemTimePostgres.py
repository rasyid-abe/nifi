from Model import DatamartModel

def sequence5min(resource, params, headers, state, x, y):
    process_group_name = "ETL MART BusiestItemTime Seq5Min - Postgres"

    ## CONFIGURATION EXISTS
    s = 0
    for i in resource['resources']:
        if (i['name'] == process_group_name):
            s = 1

    if s < 1:
        ## CREATE PROCESS GROUP
        data = {
            'client_id': params['client_id'],
            'pg_name': process_group_name,
            'pos_x': x,
            'pos_y': y,
        }
        pg_id = DatamartModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API DATAMART SEQ5MIN'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 sec',
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'http://10.130.248.133:8001/mart/sales/busiest-item-time-sequence-5min',
            'connection_timeout': '7200 secs',
            'read_timeout': '7200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =DatamartModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = DatamartModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = DatamartModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = DatamartModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = DatamartModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = DatamartModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = DatamartModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = DatamartModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = DatamartModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = DatamartModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = DatamartModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        DatamartModel.change_pg_state(params, headers, pg_id, state)
