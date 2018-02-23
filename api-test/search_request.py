import pystache
import requests
from requests.auth import HTTPBasicAuth
import datetime
from bs4 import BeautifulSoup

departure = input('From (default - ADA): ') or 'ADA'
arrival = input('To (default - AYT): ') or 'AYT'
date = input('Departure Date (default - today): ') or datetime.date.today().strftime('%Y-%m-%d')

with open('templates/SearchRequest.xml', 'r') as f:
    template = f.read()

values = {
    'country_code': 'DE',
    'agent_user_id': 'HKTHONUSR',
    'travelers': '5',
    'departure': departure,
    'date': date,
    'arrival': arrival,
    'max_connections': '1'
}
payload = pystache.render(template, values)

endpoint = 'https://iflyrestest.ibsgen.com:6013/iRes_NdcRes_WS/services/NdcResServiceSOAPPort?wsdl'
auth = {
    'username': 'HKTHONUSR',
    'password': '12345'
}

response = BeautifulSoup(requests.post(endpoint, headers=auth, data=payload).text, 'xml')
print(response.prettify())
