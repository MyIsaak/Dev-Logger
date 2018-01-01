import json
import os
import datetime
import argparse
import git
from mss import mss

from twitter.api import Twitter

try:
  to_unicode = unicode
except NameError:
  to_unicode = str

# Get the settings from settings.json
settings = {}
with open('settings.json') as outfile:
  settings = json.load(outfile)

# Setup the parser
parser = argparse.ArgumentParser(
    description='A simpler faster way to log your development process that tweets and pushes commits with screenshots')
parser.add_argument('message', type=str,
                    help='text to be commited and tweeted')
parser.add_argument('--append', action="store_true",
                    help='Commit on the same day as the last commit')
parser.add_argument('--offline', action="store_true",
                    help='Only update the readme file, no commit or tweet')
parser.add_argument('--text', action="store_true",
                    help="Don't take a screenshot for the latest log")

args = parser.parse_args()

# Setting up repo
if args.offline is False:
  repo = git.Repo(settings['repo'])


# Initialize the data.json file
def setupData():
  data = {
      'day': 1,
      'log': [""]
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
    setupData()

  if data['day'] is None:
    data['day'] = 1

  day = data['day']
  logTitle = '### Day ' + str(day) + ': ' + \
      datetime.datetime.now().strftime("%B %d, %A")

  if args.append is False:
    if data['log'][-1] == "":
      data['log'][-1] = (logTitle + '\n\n' + args.message)
    else:
      data['log'].append(logTitle + '\n\n' + args.message)
    
    data['day'] += 1
  else:
    data['log'][-1] += ('\n\n' + args.message)

  # The simplest use, save a screenshot of the 1st monitor
  # TODO: Use the callback of sct.save with lambda
  if args.text is False:
    with mss() as sct:
      sct.shot(output=settings['gallery'] + '/{date:%Y-%m-%d}.png')
      data['log'][-1] += "\n\n[![Foo]("+'https://github.com/'+settings['username'] +'/'+ settings['reponame'] +'/raw/master/'+ settings['gallery'] + datetime.datetime.now().strftime("%Y-%m-%d") + ".png)](Screenshot)"

  str_ = json.dumps(data,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False)
  outfile.write(to_unicode(str_))

# Login and send tweet to Twitter
if args.offline is False:
  twitter = Twitter(settings['username'], settings['password'])
  twitter.statuses.update(data['log'][-1] + ' ' + settings['hashtags'])


# Update devlog markdown file with screenshot and commit
with open(settings['logpath'], 'w', encoding='utf8') as outfile:
  str_ = ""

  for log in data['log']:
    str_ += log + '\n\n'
    
  outfile.write(to_unicode(str_))

if args.offline is False:
  repo.git.commit('-m', message, author=settings['email'])
