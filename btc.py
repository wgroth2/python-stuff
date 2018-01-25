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

f = urllib2.urlopen('https://www.bitstamp.net/api/v2/ticker/btcusd/')

json_string = f.read()
parsed_json = json.loads(json_string)

high = parsed_json['high']
sock.sendall('btc.high ' + str(high) + ' source=' + sourceName + ' infosource=bitstamp \n')
#
last = parsed_json['last']
sock.sendall('btc.last ' + str(last) + ' source=' + sourceName + ' infosource=bitstamp \n')

bid = parsed_json['bid']
sock.sendall('btc.bid ' + str(bid) + ' source=' + sourceName + ' infosource=bitstamp \n')

low = parsed_json['low']
sock.sendall('btc.low ' + str(low) + ' source=' + sourceName + '  infosource=bitstamp \n')

ask =  parsed_json['ask']
sock.sendall('btc.ask ' + str(ask) + ' source=' + sourceName + '  infosource=bitstamp \n')

ropen =  parsed_json['open']
sock.sendall('btc.open ' + str(ropen) + ' source=' + sourceName + ' infosource=bitstamp \n')

volume =  parsed_json['volume']
sock.sendall('btc.volume ' + str(volume) + ' source=' + sourceName + ' infosource=bitstamp \n')


syslog.syslog('BTC Price logged at ' + str(calendar.timegm(time.gmtime())) + ' ' + str(parsed_json['timestamp']));

f.close()
sock.close()

