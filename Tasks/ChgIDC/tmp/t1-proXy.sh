./bin/codis-config -c conf/config.ini config putidc xy rw
./bin/codis-config -c conf/config.ini server promote 10 10.0.0.6:6003
./bin/codis-config -c conf/config.ini server promote 9 10.0.0.6:6002
./bin/codis-config -c conf/config.ini server promote 8 10.0.0.6:6001
./bin/codis-config -c conf/config.ini server promote 5 10.0.0.5:6004
./bin/codis-config -c conf/config.ini server promote 4 10.0.0.5:6003
./bin/codis-config -c conf/config.ini server promote 7 10.0.0.6:6000
./bin/codis-config -c conf/config.ini server promote 6 10.0.0.5:6005
./bin/codis-config -c conf/config.ini server promote 1 10.0.0.5:6000
./bin/codis-config -c conf/config.ini server promote 3 10.0.0.5:6002
./bin/codis-config -c conf/config.ini server promote 11 10.0.0.6:6004
./bin/codis-config -c conf/config.ini server promote 2 10.0.0.5:6001
./bin/codis-config -c conf/config.ini server promote 12 10.0.0.6:6005
