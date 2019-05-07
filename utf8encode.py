#!/usr/bin/env python

import sys
import binascii
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('string', help="string to be encoded")
parser.add_argument('-b', help="Number of bytes", dest="num", default="2")

args = parser.parse_args()

def encode(c, b) :
  if (b == 1) :
  	return str(hex(ord(c))).replace("0x", "%")
  binC = bin(ord(c))
  flag = (len(binC) == 9)
  if (b == 2) :
    r1 = 192 
    r2 = 128
    if (flag) :
      r1 += 1
    r2 += int(binC[-6:], 2)
    return (str(hex(r1)) + str(hex(r2))).replace("0x", "%")
  if (b == 3) :
    r1 = 224
    r2 = 128
    r3 = 128
    if (flag) :
      r2 += 1
    r3 += int(binC[-6:], 2)
    return (str(hex(r1)) + str(hex(r2)) + str(hex(r3))).replace("0x", "%")
  if (b == 4) :
    r1 = 240
    r2 = 128
    r3 = 128
    r4 = 128
    if (flag) :
      r3 += 1
    r4 += int(binC[-6:], 2)
    return (str(hex(r1)) + str(hex(r2)) + str(hex(r3)) + str(hex(r4))).replace("0x", "%")
  return "none"

output = ""
for c in args.string :
  output += encode(c, int(args.num))
print output



