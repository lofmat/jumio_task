#!/usr/bin/env python3

from mokes import moke_server
from tools.tools import send_request, get_data_from_file
import base64
import os
from nose import with_setup
from nose.tools import assert_equals
http_server = moke_server.ThreadedHTTPServer("localhost", 5000)
request_value = 'Test01'
url_proxy = 'http://127.0.0.1:8081/api/image'
headers = {'Content-Type': 'application/json'}
res_dir = os.path.join(os.getcwd(), 'resources')
dump_file = os.path.join(res_dir, 'data.txt')


def remove_res_file():
    res_file = os.path.join(res_dir, 'data.txt')
    if os.path.exists(res_file):
        os.remove(res_file)


def setup_module():
    http_server.start()


def teardown_module():
    remove_res_file()
    http_server.stop()


@with_setup(remove_res_file())
def test_proxy_response_is_base64_encoded():
    send_request(url=url_proxy, value=request_value, headers=headers)
    d = get_data_from_file(dump_file)
    assert_equals(base64.b64decode(d).decode('utf8').replace("'", '"'), request_value)

