#!/usr/bin/env python3

import urllib.request

urllib.request.urlretrieve(
    "https://raw.githubusercontent.com/uvsmtid/protoprimer/refs/heads/main/src/protoprimer/main/protoprimer/primer_kernel.py",
    "bootstrap.py",
)
