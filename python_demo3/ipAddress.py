import requests

def getIpAddressWithHttpbin():
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']

def getIpAddressWithIpinfo():
    response = requests.get('https://ipinfo.io/ip')
    return response.text
