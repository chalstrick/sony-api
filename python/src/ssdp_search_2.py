import socket  
import sys
dst = "239.255.255.250"  
if len(sys.argv) > 1:  
    dst = sys.argv[1]
st = "upnp:rootdevice"  
if len(sys.argv) > 2:  
    st = sys.argv[2]
msg = [  
    'M-SEARCH * HTTP/1.1',
    'Host:239.255.255.250:1900',
    'ST:%s' % (st,),
    'Man:"ssdp:discover"',
    'MX:1',
    '']
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  
s.settimeout(100)  
s.sendto('\r\n'.join(msg), (dst, 1900) )
while True:  
    try:
        data, addr = s.recvfrom(32*1024)
    except socket.timeout:
        break
    print "[+] %s\n%s" % (addr, data)
