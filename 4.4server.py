# Dvir Sadon
import socket
import re
import os

NOT_FOUND = '404 Not Found'
FORBIDDEN = '403 Forbidden'
ISE = '500 Internal Server Error'


def if_calculate_triange(path):
    is_in = re.search(r'calculate-area[?]height=(.*\d)&width=(.*\d)', path)
    if is_in:
        height = is_in.group(1)
        width = is_in.group(2)
    else:
        return ''
    return str((int(height)*int(width))/2)


def if_calculate_next(path):
    calculate = re.search(r'calculate-next[?]num=(.*\d)', path)
    if calculate:
        num = calculate.group(1)
        return str(int(num) + 1)
    else:
        return ''


def ifhttp(got_from, client_socket):
    """
    Checks if its the data we got is for HTTP and returns the name/path
    """
    match = re.search(r'GET /(.*) HTTP.*', got_from)  # checks if its an HTTP request
    path = ''
    if match:  # if it is HTTP
        path = match.group(1)  # the Name
        if path == 'c:/wallpapers':
            client_socket.send(FORBIDDEN)  # Error 403
            client_socket.close()
    else:
        client_socket.send(ISE)  # Error 500
        # client_socket.close()
    # print path
    return path


def send_that_line_thingy(got):
    """
     returns:
        [status line , status code]
            status line pattern: "http/VERSION STATUS_CODE DESCRIPTION\r\n"
            status code: can be 404, 200, 403, 302, 500
    """
    status = ['200', 'OK\r\n']
    if not os.path.exists(got):
        status = ['404', 'Not Found\r\n']
    return ['HTTP/1.0 ' + ' '.join(status), status[0]]  # the status line and code


def header_send(path, status_code):
    dic = {'txt': 'text/html; charset=utf-8',  # dictionary of the different types
           'html': 'text/html; charset=utf-8',
           'jpg': 'image/jpeg', 'js': 'text/javascript; charset=UTF-8',
           'css': 'text/css'}
    length = 0
    if status_code == '200':
        length = os.path.getsize(path)
    header = 'Content-Length: ' + str(length) + '\n'  # sets content Length
    if status_code == str(200):
        if re.search(r'[.](.*)', path).group(1) in dic:  # the regex expression return everything after a dot.
            header += 'Content-Type: ' + dic[re.search(r'[.](.*)', path).group(1)]
    return header + '\n'


def data_maker(path, status_code):
    """
    :param path: the name/path to the file
    :param status_code: can be 404,302,403,500
    :return: returns the message that the server sends to the client
    """
    data = '\n'
    if status_code == '200':  # if its all good
        f = open(path, 'rb')
        data += f.read()
        f.close()
    return data


def build_response(path):
    """
    :param path: the name/path to the file
    :return: returns the whole thing that is sent to the client.
    """
    if re.search(r'calculate-area[?]height=(.*\d)&width=(.*\d)', path):
        response = if_calculate_triange(path)
    else:
        if re.search(r'calculate-next[?]num=(.*\d)', path):
            response = if_calculate_next(path)
        else:
            response, status_code = send_that_line_thingy(path)
            response += header_send(path, status_code)
            response += data_maker(path, status_code)

    print response
    return response


def main():
    server_socket = socket.socket()
    server_socket.bind(('127.0.0.1', 80))
    server_socket.listen(5)
    root = 'e:/SCHOOL/syber/webroot/'
    while True:  # makes the server run infinetly.
        client_socket, address = server_socket.accept()  # connects to the server
        humus = client_socket.recv(1024)
        path = root + ifhttp(humus, client_socket)
        if path == root:  # if the root is to the site or another file
            path += 'index.html'
        client_socket.send(build_response(path))


if __name__ == '__main__':
    main()
