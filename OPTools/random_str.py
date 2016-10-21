#!/usr/bin/env python

import random
import string

letter26 = []
for letter in string.lowercase:
	letter26.append(letter)
n = 0
while n <= 10:
	rand_num = random.randrange(100,999,2)
	rand_letter = string.join(random.sample(letter26,3)).replace(" ","")
	rand_str = rand_letter + str(rand_num)
	print rand_str
	n +=1
