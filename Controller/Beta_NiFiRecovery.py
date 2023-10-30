from Model import Beta_RecoveryModel

def recoveryVarian(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Varian"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Varian'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/varian',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoverySubVarian(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Sub Varian"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Sub Varian'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/sub_varian',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoveryProduk(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Produk"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Produk'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/produk',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoveryAkunting(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Akunting"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Akunting'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/akunting',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoveryBusiestItemTime(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Busiest Item Time"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Busiest Item Time'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/busiest_item_time',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoveryCompliment(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Compliment"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Compliment'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/compliment',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoveryOutletSales(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Outlet Sales"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Outlet Sales'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/outlet_sales',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoveryProductSales(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Product Sales"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Product Sales'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/product_sales',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoverySummaryReservation(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Summary Reservation"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Summary Reservation'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/summary_reservation',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoveryTransactionType(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Transaction Type"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Transaction Type'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/transaction_type',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)

def recoveryUtilization(resource, params, headers, state, x, y):
    process_group_name = "RECOVERY Mart Utilization"

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
        pg_id = Beta_RecoveryModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Recovery Utilization'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'TIMER_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '1 sec', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/recovery/rawmart/utilization',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_RecoveryModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_RecoveryModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_RecoveryModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_RecoveryModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_RecoveryModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_RecoveryModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_RecoveryModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_RecoveryModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_RecoveryModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_RecoveryModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_RecoveryModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_RecoveryModel.change_pg_state(params, headers, pg_id, state)
