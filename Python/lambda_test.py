ip = "10.256.0.3"
ipnum = ip.split('.')
print(ipnum)
print(filter(lambda x: x.isdigit(), ipnum))
print(map(int, filter(lambda x: x.isdigit(), ipnum)))
print(filter(lambda x: x >= 0 and x <= 255,map(int, filter(lambda x: x.isdigit(), ipnum))))
print(len(filter(lambda x: x >= 0 and x <= 255,map(int, filter(lambda x: x.isdigit(), ipnum)))))
