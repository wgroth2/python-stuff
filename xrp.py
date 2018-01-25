#
# Pulling data from Bitstmap
#
# Core original code written by Durren Shen @durrenshen 
# in a blog at https://www.wavefront.com/weather-metrics/
# 
# Cleaned up by Bill Roth @BillRothVMware
#
import urllib2
import json
import logging
import socket
import sys
import time
import re
import syslog
import calendar

sock = socket.socket()
#
# Below assumes the proxy is running on the same system. YMMV
#
sock.connect(('127.0.0.1', 2878))
#
# Set the source to yours.
#
sourceName = 'BRothCrypto'

#
# 

f = urllib2.urlopen('https://www.bitstamp.net/api/v2/ticker/xrpusd/')

json_string = f.read()
parsed_json = json.loads(json_string)

high = parsed_json['high']
sock.sendall('xrp.high ' + str(high) + ' source=' + sourceName + ' \n')
#
last = parsed_json['last']
sock.sendall('xrp.last ' + str(last) + ' source=' + sourceName + ' \n')

bid = parsed_json['bid']
sock.sendall('xrp.bid ' + str(bid) + ' source=' + sourceName + ' \n')

low = parsed_json['low']
sock.sendall('xrp.low ' + str(low) + ' source=' + sourceName + ' \n')

ask =  parsed_json['ask']
sock.sendall('xrp.ask ' + str(ask) + ' source=' + sourceName + ' \n')

ropen =  parsed_json['open']
sock.sendall('xrp.open ' + str(ropen) + ' source=' + sourceName + ' \n')

volume =  parsed_json['volume']
sock.sendall('xrp.volume ' + str(volume) + ' source=' + sourceName + ' \n')


syslog.syslog('Ripple Price logged at ' + str(calendar.timegm(time.gmtime())) + ' ' + str(parsed_json['timestamp']));

f.close()
sock.close()

