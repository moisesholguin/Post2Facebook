#!/usr/bin/env python
#title           :main.py
#description     :Used to post status to Facebook
#author          :Moises Holguin
#email           :mholguin@cs.utexas.edu
#date            :07-06-2014
#python_version  :2.7.6 
#==============================================================================
from facepy import GraphAPI
import sys

print '\n[Process Initiated]'

# Default Message
msg = '[TEST] This is an automated message [TEST]'

# Access token can be obtained by doing the following:
# - Log into facebook
# - Go to this url: https://developers.facebook.com/tools/explorer
ACCESS_TOKEN = ''

if ACCESS_TOKEN == '':
  print 'Access Token not provided'
  print '[Process Terminated]'
  exit()
else:
  print 'Access Token has been set'

# Replace default message if one is provided as a command line argument
if len(sys.argv) > 1:
  msg = str(sys.argv[1])
  print 'Custom message set'
else:
  print 'Using default message'

try:
  graph = GraphAPI(ACCESS_TOKEN)
  graph.post('me/feed', message=msg)
  print 'Message has been successfully posted'
except BaseException as e:
  print 'An error has occurred: ' + str(e)
finally:
  print '[Process Complete]'
