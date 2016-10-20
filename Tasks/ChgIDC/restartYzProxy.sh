#!/bin/bash
source ~/.bashrc

source /etc/profile

xyHostList=`cml $1 xy | awk '{print $4}'`
yzHostList=`cml $1 yz | awk '{print $4}'`

#for xyip in $xyHostList
#do
#  echo $xyip
#  ssh $xyip 'source /etc/profile && cd /home/work/proxy_9100 && sh load.sh stop && sleep 1 && sh load.sh start'
#  ssh $xyip 'source /etc/profile && cd /home/work/proxy_9200 && sh load.sh stop && sleep 1 && sh load.sh start'
#done 

for yzip in $yzHostList
do
  echo $yzip
  ssh root@$yzip "su - work -c 'source /etc/profile && cd /home/work/proxy_9100 && sh load.sh stop && sleep 1 && sh load.sh start'"
  ssh root@$yzip "su - work -c 'source /etc/profile && cd /home/work/proxy_9200 && sh load.sh stop && sleep 1 && sh load.sh start'"
done
