import json
import os
import datetime
import argparse
import git

from twitter.api import Twitter

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

# Setting up repo
repo = git.Repo(settings['repo'])

# Get the settings from settings.json
settings = {}
with open('settings.json') as outfile:
    settings = json.load(outfile)

# Setup the parser
parser = argparse.ArgumentParser(description='A simpler faster way to log your development process that tweets and pushes commits with screenshots')
parser.add_argument('message', type=str,
                   help='text to be commited and tweeted')

args = parser.parse_args()

def setupData():
    data = {
        'day': 1,
        'log': []
    }

    # Write JSON file
    with open('data.json', 'w', encoding='utf8') as outfile:
        str_ = json.dumps(data,
                          indent=4, sort_keys=True,
                          separators=(',', ': '), ensure_ascii=False)
        outfile.write(to_unicode(str_))


if os.path.exists('data.json') is False:
    setupData()

data = {}
with open('data.json') as outfile:
    try:
        data = json.load(outfile)
    except Exception as e:
        setupData()
        data = json.load(outfile)

with open('data.json', 'w', encoding='utf8') as outfile:
	if data['log'] is None:
		data['log'] = []

	if data['day'] is None:
		data['day'] = 1

	day = data['day']

	data['log'].append('### Day ' + str(day) + ': ' + datetime.datetime.now().strftime("%B %d, %A") + '\n\n' + args.message)

	data['day'] += 1
	str_ = json.dumps(data,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
	outfile.write(to_unicode(str_))

# Login and send tweet to Twitter
twitter = Twitter(settings['username'],settings['password'])
twitter.statuses.update(data['log'][-1]+ ' ' + settings['hashtags'])

# Update devlog markdown file and commit
with open(settings['logpath'], 'w', encoding='utf8') as outfile:
	str_ = ""
	for log in data['log']:
		str_ += log + '\n\n'

	outfile.write(to_unicode(str_))

repo.git.commit('-m', message, author=settings['email'])
