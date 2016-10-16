import MySQLdb

# Make the connection
connection = MySQLdb.connect(host='localhost',user='bcrowthe',passwd='Mu7YlQr2',db='bcrowthe')

sql = "call getquote()"

# Run query and get result
try:
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
except Exception, e:
        print e


print "Content-Type: text/html"
print
print result[1]

cursor.close()
connection.close()
