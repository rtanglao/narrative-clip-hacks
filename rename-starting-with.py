#!/usr/local/bin/python
import glob, os, re, sys
pat=re.compile("(\d+)\D*$")
def key_func(x):
  mat=pat.search(os.path.split(x)[-1]) # match last group of digits
  if mat is None:
    return x
  return "{:>10}".format(mat.group(1)) # right align to 10 digits.

start_int = int(sys.argv[1])

for oldname in sorted(glob.glob('*.jpg'), key=key_func):
  newname =  "%06d" % start_int + ".jpg"
  print "Current File Being Processed is: " + oldname +\
  " renaming to", newname
  os.rename(oldname, newname)
  start_int += 1

