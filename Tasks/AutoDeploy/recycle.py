#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import commands
import sys
import sqlite3

def Usage():
	print '''
Usage:
    python recycle.py IP1,IP2,IP3
'''

def killdel(IPlist):
	for ip in IPlist:
		rst = commands.getoutput("ssh root@%s '/usr/bin/pkill -9 codis && /usr/bin/sleep 5 && /usr/sbin/userdel -r work'" % ip)
		print rst

def deldb(IPlist):
	conn = sqlite3.connect('ClusterManager.db')
	for ip in IPlist:
		print 'delete from hostinfo where ip = "' + ip +'"'
		cursor = conn.execute('delete from hostinfo where ip = "' + ip +'"')
		rst = cursor.rowcount
		print rst
	conn.commit()
	conn.close()

def main():
	if len(sys.argv) != 2:
		Usage()
		exit()

	IPall = sys.argv[1]
	IPlist = IPall.split(",")
	print "Recycle IP is :"
	for ip in IPlist:
		print ip

	killdel(IPlist)
	deldb(IPlist)

if __name__ == "__main__":
	main()
