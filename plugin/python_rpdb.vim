let s:script_folder_path = escape( expand( '<sfile>:p:h' ), '\' )
exe 'python sys.path.insert( 0, "' . s:script_folder_path . '/../python" )'
py import rpdb_client

command RpdbStart py rpdb_client.start_debug_session()
command RpdbEnd py rpdb_client.end_debug_session()
command RpdbNext py rpdb_client.do_next()
command RpdbStep py rpdb_client.do_step()
command RpdbContinue py rpdb_client.do_continue()
