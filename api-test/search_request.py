import pystache
import requests
from requests.auth import HTTPBasicAuth

with open('templates/SearchRequest.xml', 'r') as f:
    template = f.read()

values = {
    'country_code': 'DE',
    'agent_user_id': 'HKTHONUSR',
    'travellers': '1',
    'departure': 'ADA',
    'date': '2018-02-22',
    'arrival': 'AYT',
    'max_connections': '1'
}
payload = pystache.render(template, values)

endpoint = 'https://iflyrestest.ibsgen.com:6013/iRes_NdcRes_WS/services/NdcResServiceSOAPPort?wsdl'
auth = {
    'username': 'HKTHONUSR',
    'password': '12345'
}

response = requests.post(endpoint, headers=auth, data=payload)

print(response.content)
