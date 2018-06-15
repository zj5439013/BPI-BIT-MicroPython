
import socket

def http_get(url):
    _, _, host, path = url.split('/', 3)
    addr = soc