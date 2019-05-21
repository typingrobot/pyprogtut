# echoserv.py

from socket import *
import asyncio


async def echo_server(address, loop):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(1)
    sock.setblocking(False)
    while True:
        client, addr = await loop.sock_accept(sock)
        print('connection from ', addr)
        loop.create_task(echo_handler(client, loop))


async def echo_handler(client, loop):
    while True:
        data = await loop.sock_recv(client, 100000)
        if not data:
            break
        await loop.sock_sendall(client, b'Got:' + data)
    print('Connection closed')
    client.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(echo_server(('0.0.0.0', 8000), loop))


# from socket import *
# import threading
#
#
# def echo_server(address):
#     sock = socket(AF_INET, SOCK_STREAM)
#     sock.bind(address)
#     sock.listen(1)
#     while True:
#         client, addr = sock.accept()
#         print('connection from ', addr)
#         # single threaded
#         # echo_handler(client)
#         t = threading.Thread(target=echo_handler,
#                              args=(client,))
#         t.start()
#
#
# def echo_handler(client):
#     while True:
#         data = client.recv(100000)
#         if not data:
#             break
#         client.sendall(b'Got:' + data)
#     print('Connection closed')
#     client.close()
#
#
# if __name__ == '__main__':
#     echo_server(('0.0.0.0', 8000))
