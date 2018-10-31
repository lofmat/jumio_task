#!/usr/bin/env python3

import requests
import json
import yaml


def dump_data_to_file(filename, data):
    with open(filename, 'a') as outfile:
        outfile.write(data)


def get_data_from_file(f):
    with open(f, 'r') as stream1:
        d1 = yaml.load(stream1)
    return d1


def send_request(url, value, headers):
    data_proxy = {"image": str(value)}
    json_proxy = json.dumps(data_proxy)
    requests.post(url, data=json_proxy, headers=headers)
