#!/usr/bin/env python

import redis
import string
import random

r = redis.StrictRedis(host='10.0.0.5', port=9100)

letter26 = []
for letter in string.lowercase:
	letter26.append(letter)

n = 0
while n <= 100000:
	rand_num = random.randrange(100,999,1)
	rand_letter = string.join(random.sample(letter26,3)).replace(" ","")
	rand_str = rand_letter + str(rand_num)
	#print rand_str
	list_value = 'string_string_string_string_string_' + str(n)
	#print list_value
	
	r.set(rand_str, list_value, ex=86400)
	n += 1

