./bin/codis-config -c conf/config.ini config putidc xy rw
./bin/codis-config -c conf/config.ini config putidc yz r
./bin/codis-config -c conf/config.ini server add 1 10.0.0.8:6000 master xy
./bin/codis-config -c conf/config.ini server add 1 10.0.0.9:7000 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 2 10.0.0.8:6001 master xy
./bin/codis-config -c conf/config.ini server add 2 10.0.0.9:7001 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 3 10.0.0.8:6002 master xy
./bin/codis-config -c conf/config.ini server add 3 10.0.0.9:7002 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 4 10.0.0.8:6003 master xy
./bin/codis-config -c conf/config.ini server add 4 10.0.0.9:7003 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 5 10.0.0.8:6004 master xy
./bin/codis-config -c conf/config.ini server add 5 10.0.0.9:7004 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 6 10.0.0.8:6005 master xy
./bin/codis-config -c conf/config.ini server add 6 10.0.0.9:7005 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 7 10.0.0.9:6000 master xy
./bin/codis-config -c conf/config.ini server add 7 10.0.0.8:7000 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 8 10.0.0.9:6001 master xy
./bin/codis-config -c conf/config.ini server add 8 10.0.0.8:7001 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 9 10.0.0.9:6002 master xy
./bin/codis-config -c conf/config.ini server add 9 10.0.0.8:7002 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 10 10.0.0.9:6003 master xy
./bin/codis-config -c conf/config.ini server add 10 10.0.0.8:7003 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 11 10.0.0.9:6004 master xy
./bin/codis-config -c conf/config.ini server add 11 10.0.0.8:7004 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 12 10.0.0.9:6005 master xy
./bin/codis-config -c conf/config.ini server add 12 10.0.0.8:7005 slave xy
sleep 1
./bin/codis-config -c conf/config.ini server add 1 10.0.0.10:6000 slave yz
./bin/codis-config -c conf/config.ini server add 1 10.0.0.11:7000 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 2 10.0.0.10:6001 slave yz
./bin/codis-config -c conf/config.ini server add 2 10.0.0.11:7001 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 3 10.0.0.10:6002 slave yz
./bin/codis-config -c conf/config.ini server add 3 10.0.0.11:7002 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 4 10.0.0.10:6003 slave yz
./bin/codis-config -c conf/config.ini server add 4 10.0.0.11:7003 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 5 10.0.0.10:6004 slave yz
./bin/codis-config -c conf/config.ini server add 5 10.0.0.11:7004 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 6 10.0.0.10:6005 slave yz
./bin/codis-config -c conf/config.ini server add 6 10.0.0.11:7005 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 7 10.0.0.11:6000 slave yz
./bin/codis-config -c conf/config.ini server add 7 10.0.0.10:7000 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 8 10.0.0.11:6001 slave yz
./bin/codis-config -c conf/config.ini server add 8 10.0.0.10:7001 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 9 10.0.0.11:6002 slave yz
./bin/codis-config -c conf/config.ini server add 9 10.0.0.10:7002 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 10 10.0.0.11:6003 slave yz
./bin/codis-config -c conf/config.ini server add 10 10.0.0.10:7003 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 11 10.0.0.11:6004 slave yz
./bin/codis-config -c conf/config.ini server add 11 10.0.0.10:7004 slave yz
sleep 1
./bin/codis-config -c conf/config.ini server add 12 10.0.0.11:6005 slave yz
./bin/codis-config -c conf/config.ini server add 12 10.0.0.10:7005 slave yz
./bin/codis-config -c conf/config.ini slot init
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 0 84 1 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 85 169 2 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 170 254 3 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 255 339 4 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 340 424 5 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 425 509 6 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 510 594 7 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 595 679 8 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 680 764 9 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 765 849 10 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 850 934 11 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 935 1019 12 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 1020 1020 1 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 1021 1021 2 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 1022 1022 3 online
sleep 1
./bin/codis-config -c conf/config.ini slot range-set 1023 1023 4 online
sleep 1
sleep 5
./bin/codis-config -c conf/config.ini config haturnon
