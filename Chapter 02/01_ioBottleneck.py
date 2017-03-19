import urllib2
import time
from BeautifulSoup import BeautifulSoup

t0 = time.time()
req = urllib2.urlopen('http://www.example.com')
t1 = time.time()
print("Total Time To Fetch Page: {} Seconds".format(t1-t0))
soup = BeautifulSoup(req.read())

for link in soup.findAll('a'):
  print link.get('href')


t2 = time.time()
print("Total Execeution Time: {} Seconds".format(t2-t1))