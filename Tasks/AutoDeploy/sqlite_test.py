import sys
import sqlite3

codisName = sys.argv[1]
if not codisName.endswith("-cache"):
    codisName += "-cache"
cdscodisName = "cds-" + codisName

print cdscodisName

conn = sqlite3.connect('ClusterManager.db')
cursor = conn.execute('select * from hostinfo where hostname like "%' + cdscodisName + '%"')

for hostname in cursor:
	print hostname

conn.close()

