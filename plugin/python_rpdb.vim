let s:script_folder_path = escape( expand( '<sfile>:p:h' ), '\' )
exe 'python sys.path.insert( 0, "' . s:script_folder_path . '/../python" )'
py import rpdb_srv

command RpdbStart py rpdb_srv.start_debug_session()
command RpdbEnd py rpdb_srv.end_debug_session()
command RpdbNext py rpdb_srv.do_next()
command RpdbStep py rpdb_srv.do_step()
command RpdbContinue py rpdb_srv.do_continue()
