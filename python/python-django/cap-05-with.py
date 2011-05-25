#!/usr/bin/env python
# -*- coding: utf-8 -*-
# cap-05-with.py;

from __future__ import with_statement 

with open("in.txt","r") as arquivo:
    for n, linha in enumerate(arquivo):
        print "%05d: %s" % (n, linha.strip())