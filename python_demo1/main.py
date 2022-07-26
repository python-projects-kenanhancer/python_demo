import requests

httpBinResponse = requests.get('https://httpbin.org/ip')
ipFromHttpbin = httpBinResponse.json()['origin']


ipInfoResponse = requests.get('https://ipinfo.io/ip')
ipFromIpinfo = ipInfoResponse.text


print('Your IP is {0} retrieved from https://httpbin.org/ip'.format(ipFromHttpbin))

print('Your IP is {ip} retrieved from https://ipinfo.io/ip'.format(ip=ipFromIpinfo))
