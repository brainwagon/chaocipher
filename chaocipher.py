#!/usr/bin/env python
#
#       _                      _       _               
#   ___| |__   __ _  ___   ___(_)_ __ | |__   ___ _ __ 
#  / __| '_ \ / _` |/ _ \ / __| | '_ \| '_ \ / _ \ '__|
# | (__| | | | (_| | (_) | (__| | |_) | | | |  __/ |   
#  \___|_| |_|\__,_|\___/ \___|_| .__/|_| |_|\___|_|   
#                               |_|                    
# An implementation of John Byrnes' Chaocipher as described in papers
# by Moshe Rubin.
# 
# Written by Mark VandeWettering <mvandewettering@gmail.com>
# No rights are reserved.  No warranties are implied.
#

import sys
import random
import string
import optparse

p = optparse.OptionParser()
p.add_option("-d", "--decrypt", action="store_true", dest="decrypt",
	default=False, help="decrypt instead of encrypt")
p.add_option("-p", "--pwheel", dest="pw",
	default="PTLNBQDEOYSFAVZKGJRIHWXUMC",
	help="plaintext wheel setting")
p.add_option("-c", "--cwheel", dest="cw",
	default="HXUCZVAMDSLKPEFJRIGTWOBNYQ",
	help="cipher wheel setting")

opts, args = p.parse_args()

# initialize the code machine...

cnt = 0 

def output(c):
    global cnt
    sys.stdout.write(c)
    cnt = cnt + 1 
    if cnt % 50 == 0:
        sys.stdout.write('\n')
        cnt = 0
    elif cnt % 5 == 0:
        sys.stdout.write(' ')

	
class Machine:
    def __init__(self, cw, pw):
        self.cw = cw 		# cipher wheel
        self.pw = pw 		# plaintext wheel
        pass
    def twizzle(self, idx):
        self.cw = self.cw[idx:] + self.cw[0:idx]
        self.cw = list(self.cw[0]) + \
		  self.cw[2:14] + \
		  list(self.cw[1]) + \
		  self.cw[14:]
        # and the plaintext wheel
        self.pw = self.pw[idx:] + self.pw[0:idx]
        self.pw = self.pw[1:] + list(self.pw[0])
        self.pw = self.pw[0:2] + \
		  self.pw[3:14] + \
		  list(self.pw[2]) + \
		  self.pw[14:]
    def encrypt(self, d):
        # find where it is in the plain text wheel...
        idx = self.pw.index(d)
        r = self.cw[idx]
        self.twizzle(idx)
        return r
    def decrypt(self, d):
        idx = self.cw.index(d)
        r = self.pw[idx]
        self.twizzle(idx)
        return r 

random.seed(0)
machine = Machine(list(opts.cw), list(opts.pw))

for arg in args:
    try:
        data = open(arg).read()
    except IOError as msg:
        print("%s: %s" % (arg, msg), file=sys.stderr)
        print("continuing...", file=sys.stderr)
    print(data)
    data = data.upper()
    # filter out all the non alpha characters...
    data = [x for x in data if x in string.ascii_uppercase]
    if opts.decrypt:
        for d in data:
            output(machine.decrypt(d))
    else:
        for d in data:
            output(machine.encrypt(d))
    print()
