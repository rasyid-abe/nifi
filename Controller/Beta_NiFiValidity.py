from Model import Beta_ValidityModel

def validityVarian(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Varian"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Varian'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/varian',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validitySubVarian(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Sub Varian"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Sub Varian'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/sub_varian',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validityProduk(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Produk"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Produk'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/produk',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validityAkunting(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Akunting"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Akunting'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/akunting',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validityCDC(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart CDC"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity CDC'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/cdc',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validityBusiestItemTime(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Busiest Item Time"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Busiest Item Time'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/busiest_item_time',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validityCompliment(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Compliment"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Compliment'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/compliment',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validityOutletSales(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Outlet Sales"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Outlet Sales'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/outlet_sales',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validityProductSales(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Product Sales"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Product Sales'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/product_sales',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validitySummaryReservation(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Summary Reservation"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Summary Reservation'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/summary_reservation',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validityTransactionType(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Transaction Type"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Transaction Type'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/transaction_type',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)

def validityUtilization(resource, params, headers, state, x, y):
    process_group_name = "VALIDITY Mart Utilization"

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
        pg_id = Beta_ValidityModel.processGroup(params, headers, data)

        ## CREATE PROCESSOR INVOKEHTTP
        http_name = 'InvokeHTTP API Validity Utilization'
        data = {
            'penaltyDuration': '300 sec',
            'yieldDuration': '1 sec',
            'bulletinLevel': 'WARN',
            'schedulingStrategy': 'CRON_DRIVEN', ## TIMER_DRIVEN || CRON_DRIVEN
            'run_scheduler': '0 0 2 1/1 * ? *', ## 10 sec || 0 0 19 1/1 * ? *
            'executionNode': 'ALL', ## PRIMARY || ALL
            'concurrentlySchedulableTaskCount': 1,
            'runDurationMillis': 0,
            'client_id': params['client_id'],
            'http_name': http_name,
            'http_method': 'GET',
            'remote_url': 'https://data-validity.mangkujagat.com/validity/rawmart/utilization',
            'connection_timeout': '1200 secs',
            'read_timeout': '1200 secs',
            'max_idle_connection': 1,
            'idle-timeout': '10 mins',
            'pos_x': 0,
            'pos_y': 300,
        }
        http_id =Beta_ValidityModel.precessorInvokeHTTP(params, headers, pg_id, data)

        ## CREATE PROCESSOR LOG ATTRIBUTE
        log_original_id = Beta_ValidityModel.processorLogAttribute_original(params, headers, pg_id)
        conn_original_id = Beta_ValidityModel.connection_original(params, headers, pg_id, http_id, log_original_id)

        log_retry_id = Beta_ValidityModel.processorLogAttribute_retry(params, headers, pg_id)
        conn_retry_id = Beta_ValidityModel.connection_retry(params, headers, pg_id, http_id, log_retry_id)

        log_failure_id = Beta_ValidityModel.processorLogAttribute_failure(params, headers, pg_id)
        conn_failure_id = Beta_ValidityModel.connection_failure(params, headers, pg_id, http_id, log_failure_id)

        log_response_id = Beta_ValidityModel.processorLogAttribute_response(params, headers, pg_id)
        conn_response_id = Beta_ValidityModel.connection_response(params, headers, pg_id, http_id, log_response_id)

        log_no_retry_id = Beta_ValidityModel.processorLogAttribute_no_retry(params, headers, pg_id)
        conn_no_retry_id = Beta_ValidityModel.connection_no_retry(params, headers, pg_id, http_id, log_no_retry_id)

        print(pg_id)
        print(process_group_name)

        Beta_ValidityModel.change_pg_state(params, headers, pg_id, state)
