import requests
import json

# Carga datos desde el archivo JSON
with open('atp_tennis_couchdb.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Base de datos CouchDB
base_datos = "personas005"
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Enviar documentos 
for doc in data['docs']:
    response = requests.post(url, headers=headers, json=doc)
    print(f"Insertando documento con _id: {doc['_id']} | Código de respuesta: {response.status_code}")