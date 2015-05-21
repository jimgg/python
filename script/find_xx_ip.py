# -*- coding: utf-8 -*-
import socket
import ssl


def test(ip, port, url, host, keyword):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        ssl_sock = ssl.wrap_socket(s)
        ssl_sock.connect((ip, port))
        data = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host)
        ssl_sock.write(data)
        data = []
        while True:
            res = ssl_sock.read()
            if not res:
                break
            data.append(res)
        ssl_sock.close()

        data = ''.join(data)
        if data.find(keyword):
            print ip, 'ok'
        else:
            print ip, 'fail'
    except Exception:
        print ip, 'fail'


def test_range(ip_prefix, port, url, host, keyword):
    for i in xrange(1, 256):
        ip = ip_prefix + '.' + str(i)
        test(ip, port, url, host, keyword)
