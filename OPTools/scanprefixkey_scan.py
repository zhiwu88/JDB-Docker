#!/usr/bin/env python
#coding=utf-8

import redis
import urllib2
import json
import time

start_time = time.time()

prefix = "k"

def getInfo(url):
	response = urllib2.urlopen(url)
	page_str = response.read()
	json_list = json.loads(page_str)
	return json_list
	#print(type(response.read()))
	#print(type(jsondata))

groupsurl = "http://10.0.0.5:8080/api/server_groups"
groupsInfo = getInfo(groupsurl)

for group in groupsInfo:
	slave = ""
	#print(group)
	for server in group["servers"]:
		if server["type"] == "slave":
			slave = server["addr"]
			#print slave
			#每个组获取第一个slave后跳出for循环。
			break
	if slave != "":
		redisIP = slave.split(":")[0]
		redisPort = int(slave.split(":")[1])
		print(redisIP,redisPort)
		r = redis.StrictRedis(host=redisIP, port=redisPort)
		#allkeys = r.keys(pattern='*')
		#print(allkeys)
		cursor = '0'
		while cursor != 0:
			cursor, keys = r.scan(cursor, match=prefix + "*", count=1000)
			for key in keys:
				print(key)

end_time = time.time()
print("done: %f s" % (end_time - start_time))
