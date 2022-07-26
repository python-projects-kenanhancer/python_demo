import ipAddress as ip

ipFromHttpbin = ip.getIpAddressWithHttpbin()

ipFromIpinfo = ip.getIpAddressWithIpinfo()

print(f'Your IP is {ipFromHttpbin} retrieved from https://httpbin.org/ip')

print(f'Your IP is {ipFromIpinfo} received from https://ipinfo.io/ip')
