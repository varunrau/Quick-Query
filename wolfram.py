import sys
import urllib2
from xml.dom.minidom import parseString

query = " ".join(sys.argv[1:])
file = urllib2.urlopen('http://api.wolframalpha.com/v2/query?input=' + urllib2.quote(query, "") + '&appid=695RVU-8V9WUKATK2')
data = file.read()
dom = parseString(data)
xmlTag = dom.getElementsByTagName("plaintext")[1].toxml()
xmlData = xmlTag.replace("<plaintext>", "").replace("</plaintext>", "")
print xmlData
file.close()
