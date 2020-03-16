# 1. This a code for an empty response from server

# import socket

# s = socket.socket()
# s.bind(("0.0.0.0", 8080))
# s.listen(10)  # 10 is the backlog

# # wait for a connection
# conn, address = s.accept()
# print(str(conn.recv(4096)))

# 2. http response 'Hi there'
# import socket

# s = socket.socket()
# s.bind(("0.0.0.0", 8080))
# s.listen(10)  # 10 is the backlog

# http_response = b"""HTTP/1.1 200 OK\r
# Content-Lenght: 10\r

# Hi there :)\n\r\n"""

# while True:
#     # wait for a connection
#     conn, address = s.accept()
#     print(str(conn.recv(4096)))
#     conn.send(http_response)
# s.close()

# 3. several_responses
# import socket
# import time

# s = socket.socket()
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.bind(("0.0.0.0", 8080))
# s.listen(10)  # 10 is the backlog

# http_response = b"""HTTP/1.1 200 OK\r
# Content-Lenght: 10\r

# Hi there :)\n\r\n"""

# while True:
#     # wait for a connection
#     conn, address = s.accept()
#     print(str(conn.recv(4096)))
#     time.sleep(2)
#     conn.send(http_response)
#     conn.shutdown(socket.SHUT_WR)
#     conn.close()
# s.close()

# 4.	threads
import socket
import _thread

s = socket.socket()
s.bind(("0.0.0.0", 8080))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(10)  # 10 is the backlog

http_response = b"""HTTP/1.1 200 OK\r
Content-Lenght: 10\r

Hi there :)\n\r\n"""


def respond(conn):
    print(str(conn.recv(4096)))
    conn.send(http_response)
    conn.shutdown(socket.SHUT_WR)
    conn.close()


while True:
    # wait for a connection
    conn, address = s.accept()
    _thread.start_new_thread(respond, (conn,))

s.close()
