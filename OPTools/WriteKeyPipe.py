#!/usr/bin/env python

import redis
import string
import random
import time

r = redis.StrictRedis(host='10.0.0.8', port=9100)
pipe = r.pipeline(transaction=False)

letter26 = []
for letter in string.lowercase:
	letter26.append(letter)

n = 0
while n <= 10000:
	rand_num = random.randrange(100,999,1)
	rand_letter = string.join(random.sample(letter26,3)).replace(" ","")
	rand_str = rand_letter + str(rand_num)
	#print rand_str
	for i in range(10):
		print i
		str_name = rand_str + str(n) + str(i)
		str_value = 'string_string_string_string_string_' + str(n) + str(i)
		hash_name = 'hash' + str(n)
                hash_field = rand_str + str(n) + str(i)
		hash_value = 'hash_hash_hash_hash_hash_' + str(n) + str(i)
		list_name = 'list' + str(n)
		list_value = 'list_list_list_list_list_' + str(n) + str(i)
		#print str_name, str_value, hash_name, hash_field, hash_value, list_name, list_value
		
		pipe.set(str_name, str_value, ex=3600)
		pipe.hset(hash_name, hash_field, hash_value)
		pipe.rpush(list_name, list_value)

	pipe.get(str_name).hgetall(hash_name).lrange(list_name, 0, -1)
	n += 1
	rst = pipe.execute()
	print rst
	time.sleep(1)

