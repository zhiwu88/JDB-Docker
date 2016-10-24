#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys
import commands


def Usage():
	print("""
	Usage:
		python InitHost.py ip""")
def goon():
	answer = raw_input("Go on ? Enter yes or no: ")
	if answer.strip() != "yes":
		exit()

def cp_sshpubkey(hostIP):
	for IP in hostIP:
		rst = commands.getoutput("ssh-copy-id root@%s" % IP)
	        print(rst)

def adduser(hostIP,username):
	for IP in hostIP:
		rst = commands.getoutput("ssh -l root -t %s \"useradd %s\"" %(IP, username))
		print(rst)

def rpminstall(hostIP, rpmlist):
	for IP in hostIP:
		rst = commands.getoutput("ssh -l root -t %s \"yum install -y %s\"" %(IP, rpmlist))

def main():
        if len(sys.argv) != 2:
		Usage()
		exit()

	hostALL = sys.argv[1]
	hostIP = hostALL.strip().split(",")
	for ip in hostIP:
		print("--- HostIP is " + ip)

	goon()
	
	print("--- ssh-copy public key to remote.")
	cp_sshpubkey(hostIP)

	print("--- Add user work.")
	adduser(hostIP,"work")

	print("--- Install RPM PKT")
	rpmlist = "rsync sysvinit-tools psmisc openssh-clients cronie"
        rpminstall(hostIP, rpmlist)

if __name__ == "__main__":
	main()
