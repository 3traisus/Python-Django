'''def Consulta_sql (Conec,sql):
    try:
        cursor = Conec.cursor()
        cursor.execute(sql)
    except Exception as error:
        print(error)
    else:
        if sql.lower().startswith("Select"):
            data = cursor.fetchall()'''
            

import pyodbc as serverSql
import Recursos.DataBase as db

def Conectar_server(server,database):
    try:
        #conn_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
        #conn_str = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        #conn = serverSql.connect(conn_string)
        #cursor = conn.cursor()
        print("Hola",server)
        db.met_ini()
        conn,cursor = db.serverSql(server,database)
        cursor.execute("SELECT * FROM EMPLEADO")
        rows = cursor.fetchall()
        
        for r in rows:
            print(r)
            
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)
    
Conectar_server(server="DESKTOP-NPGL15G",database="NATURISTADEFINITIVA")


def empleados(id):
    data = []
    sql = f"SELECT * FROM EMPLEADO WHERE PUESTO= '{id}'"
    conn_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER=DESKTOP-NPGL15G;DATABASE=NATURISTADEFINITIVA;Trusted_Connection=yes;"
    conn = serverSql.connect(conn_string)
    cursor = conn.cursor()
    cursor.execute(sql)
    empleado = cursor.fetchall()
    if cursor:
        for emp in empleado:
            print(emp)

    cursor.close()
    conn.close()
    
print("///////////////////////////////////////////////")
empleados("CAJERO")
        

lista1=[[100,"Berlusia"],[200,"Traisus"],[300,"Alan Turing"]]
print(lista1)
lista1.sort(key=lambda l: l[1])
print(lista1)

#Argumentos Albitrarios 
def funcion_n_argumentos(x,*args):
    return 0

def descargue_archivo(tipo,*args):
    num_arg=len(args)
    if(tipo=="video"):
        if num_arg == 0:
            print(f"El formato seleccionado, tipo de archivo{tipo}")
        elif num_arg == 1:
            print(f"El formato seleccionado, tipo de archivo{tipo} con resolucion {args[0]}")
        elif num_arg == 2:
            print(f"El formato seleccionado, tipo de archivo{tipo} con resolucion {args[0]} y {args[1]}fps")
    elif tipo=="audio":
        print(f"El formato seleccionado, tipo de archivo{tipo}")
    else:
        print("Formato no valido")
    
def mi_filtro(ciudad,estado,cp):
    return f"SELECT * FROM CLIENTES WHERE ciudad='{ciudad}'"

def otro_filtro(**kwargs):
    sql = "SELECT * FROM CLIENTES"
    i=0
    for clave,valor in kwargs.items():
        if i ==0:
            sql += " WHERE "
            i=1
        else:
            sql += " AND "
        sql += f"{clave} = '{valor}"
    return sql

print(otro_filtro(Estado="Mishigan",Clima="Frio"))