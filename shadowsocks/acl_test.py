#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, \
    with_statement


from common import IPNetwork


def test_acl_network():
    with open("chn.acl", "r") as f:
        acl_txt = f.read()
        proxy_all, bypass = acl_txt.split("[bypass_list]")
        proxy_all_list = proxy_all.replace("\n",",")
        bypass_list = bypass.replace("\n", ",")[1:]
    ip_network = IPNetwork(bypass_list)
    assert '103.235.46.39' in ip_network


if __name__ == '__main__':
    test_acl_network()


