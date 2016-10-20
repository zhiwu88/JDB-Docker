#!/usr/bin/env python

import redis
import urllib2
import json
import time

def getInfo(url):
	response = urllib2.urlopen(url)
	print(response)

groupsurl = "http://10.127.43.17:8080/api/server_groups"
groupsInfo = getInfo(gu)
