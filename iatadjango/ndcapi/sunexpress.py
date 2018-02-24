import requests
from requests.auth import HTTPBasicAuth
import datetime
from bs4 import BeautifulSoup
from django.shortcuts import render

api_endpoint = 'https://iflyrestest.ibsgen.com:6013/iRes_NdcRes_WS/services/NdcResServiceSOAPPort?wsdl'
api_auth = {
    'username': 'HKTHONUSR',
    'password': '12345'
}

def get_ticket_details(pnr):
    payload = render('ndc/AirDocDisplay.xml', {'pnr': pnr})
    response = requests.post(api_endpoint, headers=api_auth, data=payload)
    ticket = BeautifulSoup(response.text, 'xml')
    return {
        'airline': 'SunExpress',
        'pnr': pnr,
        'source': ticket.find('Departure').find('AirportCode').get_text(),
        'destination': ticket.find('Arrival').find('AirportCode').get_text(),
        'date': ticket.find('Departure').find('Date').get_text()
        }
