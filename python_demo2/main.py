import requests


def getIpAddressWithHttpbin():
    response = requests.get('https://httpbin.org/ip')
    return response.json()['origin']


def getIpAddressWithIpinfo():
    response = requests.get('https://ipinfo.io/ip')
    return response.text


ipFromHttpbin = getIpAddressWithHttpbin()

ipFromIpinfo = getIpAddressWithIpinfo()

print(
    'Your IP is {0} retrieved from https://httpbin.org/ip'.format(ipFromHttpbin))

print(
    'Your IP is {ip} retrieved from https://ipinfo.io/ip'.format(ip=ipFromIpinfo))
