import pyodbc as serverSql
import bcrypt as bc

msj =   [
            {
                "Bandera": True,
                "Control": "",#va control
                "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
            },
            {
                "Bandera": False,
                "Control": "",#
                "Mensaje": "No existe el Usuario"
            },
            {
                "Bandera": False,
                "Control": "",#va control
                "Mensaje": "Contraseña incorrecta"
            }
        ]

server="DESKTOP-NPGL15G"
database="videogames"

def autenticar_usuario(control,clave):
    try:
        conn_string = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"
        conn = serverSql.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(f"SELECT CLAVE FROM Usuarios WHERE ncontrol='{str(control)}'")
        info = cursor.fetchone()
        cursor.close()
        conn.close()
        if info:
            msj[0]["Control"] = control
            if info[0] == clave:
                return msj[0]
            else:
                return msj[2]
        else:
            return msj[1]
            
    except Exception as e:
        print(e)
        
print(autenticar_usuario("19420525","YAMCHA"))
    

    