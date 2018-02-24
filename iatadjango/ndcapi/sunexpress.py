import requests
from requests.auth import HTTPBasicAuth
import datetime
from bs4 import BeautifulSoup
import pystache

api_endpoint = 'https://iflyrestest.ibsgen.com:6013/iRes_NdcRes_WS/services/NdcResServiceSOAPPort?wsdl'
api_auth = {
    'username': 'HKTHONUSR',
    'password': '12345'
}


def get_ticket_details(pnr):
    template = """<?xml version="1.0" encoding="UTF-8"?>
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:edis="http://www.iata.org/IATA/EDIST">
       <soapenv:Header />
       <soapenv:Body>
          <edis:AirDocDisplayRQ>
             <edis:Document>
                <edis:Name>NDC</edis:Name>
                <edis:ReferenceVersion>15.2</edis:ReferenceVersion>
             </edis:Document>
             <edis:Party>
                <edis:Sender>
                   <edis:AgentUserSender>
                      <edis:AgentUserID>HKTHONUSR</edis:AgentUserID>
                   </edis:AgentUserSender>
                </edis:Sender>
                <edis:Recipient>
                   <edis:ORA_Recipient>
                      <edis:AirlineID>XQ</edis:AirlineID>
                   </edis:ORA_Recipient>
                </edis:Recipient>
             </edis:Party>
             <edis:Query>
                <edis:TicketDocument>
                   <edis:TicketDocNbr>{{pnr}}</edis:TicketDocNbr>
                </edis:TicketDocument>
             </edis:Query>
          </edis:AirDocDisplayRQ>
       </soapenv:Body>
    </soapenv:Envelope>"""
    payload = pystache.render(template, {'pnr': pnr})
    response = requests.post(api_endpoint, headers=api_auth, data=payload)
    ticket = BeautifulSoup(response.text, 'xml')
    return {
        'airline': 'SunExpress',
        'pnr': pnr,
        'source': ticket.find('Departure').find('AirportCode').get_text(),
        'destination': ticket.find('Arrival').find('AirportCode').get_text(),
        'date': ticket.find('Departure').find('Date').get_text()[:-1],
    }
