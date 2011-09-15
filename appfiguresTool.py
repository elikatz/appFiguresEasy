import base64
import urllib2
import sys
import json

def connect():
    username = "XXX"
    password = "XXX"
    url = "https://api.appfigures.com/v1.1/sales/dates/2011-08-20/2011-08-24"
    req = urllib2.Request(url)
    
    base64string = base64.encodestring('%s:%s' % (username, password))[:-1]
    authheader =  "Basic %s" % base64string
    req.add_header("Authorization", authheader)
    try:
        handle = urllib2.urlopen(req)
    except IOError, e:
        print "It looks like the username or password is wrong."
        sys.exit(1)
    thepage = handle.read()
    return thepage

#date, profit, download
def parseData(data):
    outString = ""
    result = eval(data)
    for key in json.loads(data):
        line = result[key]
        outString += key
        outString += ", "
        outString += line["revenue"]
        outString += ", "
        outString += str(line["downloads"])
        outString += "\n"
    print outString
    f = open('data.txt', 'w')
    f.write(outString)
    f.close()
        
def main():
    data = connect()
    parseData(data)

if __name__ == "__main__":
    main()
    
