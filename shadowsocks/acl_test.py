#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, \
    with_statement

import os
import sys
from common import IPNetwork


def test_acl_network():
    chn_path = os.path.join(os.path.dirname(__file__), '../', 'chn.acl')
    with open(chn_path, "r") as f:
        acl_txt = f.read()
        proxy_all, bypass_witelist = acl_txt.split("[bypass_list]")
        bypass, witelist = bypass_witelist.split("[whitelist]")
        proxy_all_list = proxy_all.replace("\n", ",")
        bypass_list = bypass.replace("\n", ",")[1:]
        witelist = witelist.replace("\n", ",")
    # return IPNetwork(bypass_list), witelist
    ip_network = IPNetwork(bypass_list)
    assert '52.72.178.213' in ip_network


if __name__ == '__main__':
    test_acl_network()
