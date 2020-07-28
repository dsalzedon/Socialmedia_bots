"""
API key:
DOeZjqLSL16eHxoNyYmaaKiEY

API key secret:
2mUrwSYZPFyHNF7obXxboYHTsAvlFP6FdwGo5MUpVcTw16OO9T

Access token:
1279290570758914048-HIFh8hXTjZ8VgGAtfLqJfQgzpWaeNF

Access token secret:
ujuu6XNOIzO64L5LgeejNDMK8CdE2V5jcPVoiv5UrqMuk

https://geekswipe.net/technology/computing/code-python-twitter-bot-in-ten-minutes/
"""

from twython import Twython, TwythonError
import time

APP_KEY = 'EUNrEiVyIbgc6oRmQaV31egPq'
APP_SECRET = 'YUHGsYTDPEqAAGM9RShhbnuC2uXKaZqGrEMzOcltMVXaBqz6dV'
OAUTH_TOKEN = '1279290570758914048-S92XWecr46gLpZrm5ZkbPyzMiwlgWj'
OAUTH_TOKEN_SECRET = 'jhpH16DkTW6ACUX27sdnA9FPVQryeI2U5ogtVKuufaw1U'

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

with open('liners.txt', 'r+') as tweetfile:
	buff = tweetfile.readlines()

for line in buff[:]:
	line = line.strip(r'\n') # Strips any empty line.
	if len(line)<=140 and len(line)>0:
		print ("Tweeting...")
		try:
			twitter.update_status(status=line)
		except TwythonError as e:
			print (e)
		with open ('liners.txt', 'w') as tweetfile:
			buff.remove(line) # Removes the tweeted line.
			tweetfile.writelines(buff)
		time.sleep(180)
	else:
		with open ('liners.txt', 'w') as tweetfile:
			buff.remove(line) # Removes the line that has more than 140 characters.
			tweetfile.writelines(buff)
		print ("Skipped line - Too long for a tweet!")
		continue
print ("No more lines to tweet...") # When you see this... Well, go find some new tweets...
