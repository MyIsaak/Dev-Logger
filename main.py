import git
import json
import os
import io
import datetime
import string

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

if os.path.exists('data.json'):
	data = {}
	with open('data.json') as outfile:
		data = json.load(outfile)

	with open('data.json', 'w', encoding='utf8') as outfile:
		data['log'] = data['log'].append('Day ' + str(data['day'])
			+ ': ' + datetime.datetime.now().strftime("%B %d, %A"))

		# repo.git.commit('-m', message, author='isaak.eriksson@gmail.com')

		data['day'] += 1
		str_ = json.dumps(data,
	                      indent=4, sort_keys=True,
	                      separators=(',', ': '), ensure_ascii=False)
		outfile.write(to_unicode(str_))

else:
	data = {
		'day' : 1,
		'log' : []
	}

	# Write JSON file
	with open('data.json', 'w', encoding='utf8') as outfile:
	    str_ = json.dumps(data,
	                      indent=4, sort_keys=True,
	                      separators=(',', ': '), ensure_ascii=False)
	    outfile.write(to_unicode(str_))