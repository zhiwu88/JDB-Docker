#!/usr/bin/env python

import redis

r = redis.StrictRedis(host='10.0.0.5', port=9100)

keys = ['list_100','list_1337','list_3600','list_3986','list_4163','list_5483','list_5959','list_6454','list_6608','list_8514','list_8748','list_11151','list_12186','list_13466','list_14159','list_14305','list_15963','list_16632','list_18772','list_19292','list_20503','list_22034','list_22268','list_23788','list_25757','list_26780','list_26806','list_27260','list_28946','list_29320','list_31414','list_31648','list_32919','list_33123','list_34640','list_36377','list_37697','list_37911','list_38237','list_39851','list_40716','list_40890','list_42221','list_43847','list_45542','list_45898','list_46595','list_47075','list_47229','list_48689','list_49135','list_49369','list_51601','list_51987','list_52950','list_53336','list_54455','list_54609','list_56162','list_57482','list_57958','list_58022','list_59818','list_60253','list_61835','list_62538','list_62764','list_63284','list_65007','list_67530','list_68190','list_69470','list_70922','list_71118','list_71344','list_72393','list_73673','list_74110','list_76427','list_78567','list_79087','list_80875','list_81213','list_82098','list_83578','list_83724','list_84047','list_86570','list_87090','list_88430','list_90158','list_90304','list_91962','list_92633','list_95150','list_96187','list_97467','list_99527']
for i in keys:
  n = 0
  while n <= 10:
     listvalue = 'list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_list_'+str(n)
     r.lpush(i,listvalue)
     n = n + 1
  print r.lrange(i,0,100)

