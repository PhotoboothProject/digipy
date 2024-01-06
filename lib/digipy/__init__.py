#!/usr/bin/env python

"""
Simple wrapper of the digicamcontrol API (digicamcontrol.com)
"""

import requests
from typing import List

__VERSION__ = "0.1.0"


class Api:
    _host: str
    _port: int

    def __init__(self, host="127.0.0.1", port=5513):
        self._host = host
        self._port = port

    def slc(self, command: str, params: List[str]):
        url = f"http://{self._host}:{self._port}/?slc={command}"

        for i, p in enumerate(params, start=1):
            url = f"{url}{'?' if i == 0 else '&'}param{i}={p}"

        r = requests.get(url)
        r.raise_for_status()

        if r.text != "OK":
            raise Exception(r.text)

    def cmd(self, command: str):
        url = f"http://{self._host}:{self._port}/?CMD={command}"

        r = requests.get(url)
        r.raise_for_status()
