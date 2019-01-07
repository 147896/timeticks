#!/usr/bin/env python
#snmpwalk -v2c -c unimedvg 172.27.1.190 1.3.6.1.2.1.2.2.1.9.13600045
import datetime, time, subprocess, re, sys, getopt

def usage():
   print("usage: python timeticks.py [--help] [-c <community>] [-i <ipaddr>] [-o <oid>]")

try: 
   opts, args = getopt.getopt(sys.argv[1:], 'hc:i:o:', ['help', 'community=', 'ipaddr=', 'oid='])

   if not opts[0][0] or not opts[1][0] or not opts[2][0]:
      usage()
      sys.exit(1)

   if opts[0][0] in ('-h', '--help'):
      usage()
      sys.exit(1)

   for opt, arg in opts:
      if opt in ('-c', '--community'):
         community = arg
      elif opt in ('-i', '--ipaddr'):
         ipaddr = arg
      elif opt in ('-o', '--oid'):
         oid = arg
   
except IndexError:
   usage()
   sys.exit(2)   
except NameError:
   usage()
   sys.exit(2)

try: 
   cmd = subprocess.check_output(["snmpwalk -v2c -c %s %s %s" %(community, ipaddr, oid)], shell=True)
   timeticks = cmd.split(' ')
   timeticks = timeticks[3]
   timeticks = re.sub(r'\(|\)', '', timeticks)
   dticks = int(timeticks)/8640000
   hticks = int(timeticks)/360000
   ticksdays = datetime.timedelta(days=dticks).days

except ValueError:
   print('OID Invalid or parameters..')
   sys.exit(2)

except NameError:
   usage()
   sys.exit(2)

def quit(text, code):
   if code == 2:
      print('CRITICAL - %s' %(text))
      sys.exit(code)
   elif code == 0:
      print('OK - %s' %(text))
      sys.exit(code)

#if hticks > 12:
msg = '%s | timeticks=%shrs' %(hticks, hticks)
if hticks >= 12:
   quit(msg, 0)
elif hticks < 12:
   quit(msg, 2)
