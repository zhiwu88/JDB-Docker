import sys
import sqlite3

#def getHostCount(codisName):
#	cdscodisName = "cds-" + codisName
#	print cdscodisName
#	conn = sqlite3.connect('DockerCodis.db')
#	#cursor = conn.execute("select count(*) from hostinfo where hostname like '" + cdscodisName + "%'")
#	cursor = conn.execute("select count(*) from hostinfo where hostname like ?", (cdscodisName + "%",))
#	Hostcount = cursor.fetchone()
#	print Hostcount[0]
#	print type(Hostcount)
#	return Hostcount[0]

def getHostMaxnum(codisName):
	cdscodisName = "cds-" + codisName
        print cdscodisName
        conn = sqlite3.connect('DockerCodis.db')
        #cursor = conn.execute("select count(*) from hostinfo where hostname like '" + cdscodisName + "%'")
        cursor = conn.execute("select hostname from hostinfo where hostname like ?", (cdscodisName + "%",))
	listHostnum = []
	for i in cursor:
		print i[0][-5:-3]
		num = int(i[0][-5:-3])
		listHostnum.append(num)
	print listHostnum
	print "Max num is:", max(listHostnum)
	return max(listHostnum)



codisName = sys.argv[1]
yzHosts = sys.argv[2]

if not codisName.endswith("-cache"):
	codisName += "-cache"

yzHostList = yzHosts.split(",")
for index, yzHost in enumerate(yzHostList):
	yzHostList[index] = yzHost.strip()

print codisName,yzHostList

#Hostcount = getHostCount(codisName)
#print Hostcount

Hostmaxnum = getHostMaxnum(codisName)
print Hostmaxnum

newHostnum = Hostmaxnum + 1
print newHostnum

for index, yzHost in enumerate(yzHostList):
	hostName = "cds-" + codisName + "0" + str(index+newHostnum) + ".yz"
	print hostName

