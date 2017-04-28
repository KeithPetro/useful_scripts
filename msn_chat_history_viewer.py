#MSN Chat History Viewer
#Keith Petro - 2016/10/23
#Description: A simple program to view the contents of an MSN messenger
#XML chat log file

from bs4 import BeautifulSoup
import sys

def parse_log(file):
	content = open(file, encoding='utf-8').read()
	soup = BeautifulSoup(content, 'html.parser')
	wf = open('CLARIFIED - ' + file[:-4] + '.txt', 'a')

	for message in soup.find_all('message'):
		msg_attrs = dict(message.attrs)
		sender = message.find('from').user
		sender_dict = dict(sender.attrs)

		print("\n[%s | %s]\n=========================\n[%s]: %s\n" % (
			  msg_attrs[u'date'],
			  msg_attrs[u'time'],
			  sender_dict[u'friendlyname'],
			  message.find('text').text))

		wf.write("\n[%s | %s]\n=========================\n[%s]: %s\n" % (
				 msg_attrs[u'date'],
				 msg_attrs[u'time'],
				 sender_dict[u'friendlyname'],
				 message.find('text').text))

	wf.close()

parse_log(sys.argv[1])