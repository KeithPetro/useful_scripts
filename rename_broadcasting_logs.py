import os
import re
import sys

station_code = sys.argv[1]

for file in os.listdir('.'):
	f = open(file, 'r')
	first_line = f.readline()
	re_result = re.search('[0-9]{4}', first_line)

	if(re_result):
		year_short_code = re_result.group(0)[0:2]
		if(int(year_short_code) > 50):
			year = '19' + year_short_code
		else:
			year = '20' + year_short_code

		month = re_result.group(0)[2:4]

		new_file = '[' + station_code + '] [' + year + "'" + month + '].log'

		if(os.path.exists(new_file)):
			os.rename(new_file, new_file[:-4] + ' [2].log')
		
		os.rename(file, new_file)
	else:
		print('ERROR: UNABLE TO FIND DATE CODE FOR ' + file)
