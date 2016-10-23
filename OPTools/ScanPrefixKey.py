#!/usr/bin/env python
#coding=utf-8

import redis
import urllib2
import json
import time

start_time = time.time()

prefix = "c"
groupsurl = "http://10.0.0.5:8080/api/server_groups"

def getInfo(url):
	response = urllib2.urlopen(url)
	page_str = response.read()
	json_list = json.loads(page_str)
	return json_list

groupsInfo = getInfo(groupsurl)

n = 0
for group in groupsInfo:
	slave = ""
	for server in group["servers"]:
		if server["type"] == "slave":
			slave = server["addr"]
			#每个组获取第一个slave后跳出for循环。
			break
	if slave != "":
		redisIP = slave.split(":")[0]
		redisPort = int(slave.split(":")[1])
		print(redisIP,redisPort)
		r = redis.StrictRedis(host=redisIP, port=redisPort)
		for key in r.scan_iter(match=prefix + "*", count=1000):
			print(key)
			n += 1
print n,"keys"

end_time = time.time()
print("done: %f s" % (end_time - start_time))
