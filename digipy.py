#!/usr/bin/env python3

"""
Simple wrapper of the digicamcontrol API (digicamcontrol.com)
"""

import sys
import os
import requests
from typing import List


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


if len(sys.argv) == 1:
    sys.exit(1)

api = Api(
    os.environ.get("DIGIPY_HOST", "127.0.0.1"), int(os.environ.get("DIGIPY_PORT", 5513))
)

if sys.argv[1] == "slc":
    api.slc(sys.argv[2], sys.argv[3:])
    sys.exit(0)
elif sys.argv[1] == "cmd":
    api.cmd(sys.argv[2])
else:
    print("Unknown command")
    sys.exit(1)
