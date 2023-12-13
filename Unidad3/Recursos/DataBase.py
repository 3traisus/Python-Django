import pyodbc as serverSql
def sqlserver_connection(server,database):
    try:
        conn_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
        conn = serverSql.connect(conn_string)
        cursor = conn.cursor()
        return conn,cursor
    except Exception as e:
        print(e)
        
def met_ini():
    print("Hola")        
        
def sqlserver_connection(server,database,username,password):
    try:        
        conn_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}Trusted_Connection=yes;"
        conn = serverSql.connect(conn_string)
        cursor = conn.cursor()
        return conn,cursor
    except Exception as e:
        print(e)
    
        
        
#sqlserver_connection(server="DESKTOP-NPGL15G",database="NATURISTADEFINITIVA",username="",password="")
    