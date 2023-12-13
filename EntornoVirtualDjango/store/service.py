import requests 

def get_Categorias():
    #hacer la peticion a la api rest
    response = requests.get('http://127.0.0.1:3000/api/categoria/list/')
    if response.status_code == 200:
        return response.json()
    
    
def get_Productos():
    #hacer la peticion a la api rest
    response = requests.get('http://127.0.0.1:3000/api/categoria/list/')
    if response.status_code == 200:
        return response.json()