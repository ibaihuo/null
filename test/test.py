#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os.path

path = '/var/www/chopper/'

print os.path.split(path)
print '/'.join(path.split('/')[:-2]) + '/'
