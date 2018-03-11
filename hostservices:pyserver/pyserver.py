#!/usr/bin/python
#-*- coding: utf-8-*-
# @edt ASSIX-M06 Curs 2017-2018
#
# Calendar server 
#  - programa, el pare finalitza i deixa el fill en execució.
#  - governat pels senyals:
#     user1: llista clients, usr2: #clients, alarm: plegar,
#     hup: inicialitzar llista, term: missatge refusant plegar. 
# ----------------------------------
import os, sys, signal, argparse, socket
from subprocess import Popen, PIPE
parser = argparse.ArgumentParser(description="calendar-server [-p port]")
parser.add_argument("-p", "--port", default=50001)
args = parser.parse_args() 
print args
HOST = '' 
PORT = args.port
MAX=5
clients=[]
def mysigusr1(signum,frame):
  global clients
  print clients
def mysigusr2(signum,frame):
  global clients
  print len(clients)
def mysighup(signum,frame):
  global clients
  clients=[]
def mysigterm(signum,frame):
  global clients
  print "Signal handler called with signal:", signum
  print "No vull plegar!!"
  clients.append(signum)
def mysigalarm(signum,frame):
  global clients
  print "Signal handler called with signal:", signum
  print clients, len(clients)
  print "bye bye!"
  sys.exit(0)
signal.signal(signal.SIGUSR1,mysigusr1)
signal.signal(signal.SIGUSR2,mysigusr2)
signal.signal(signal.SIGALRM,mysigalarm)
signal.signal(signal.SIGTERM,mysigterm)
signal.signal(signal.SIGHUP,mysighup)
signal.alarm(MAX*60)

# -----------------------------------------------
print "Inici del programa principal PARE"
pid = os.fork()
if pid != 0:
  print "Fi Programa PARE", os.getpid(), pid
  sys.exit(0)
# ----------------------------------------------

# ----------------------------------------------
print "Programa FILL", os.getpid(), pid
# ----------------------------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(1)
while True:
  try:
    conn, addr = s.accept()
    clients.append(addr)
  except Exception:
    continue
  sys.stderr.write("Connected by %s" % addr[0])
  command = ["/usr/bin/uname -a; hostname -A; hostname -i"]
  pipeData = Popen(command, shell = True, stdout=PIPE, stderr=PIPE)
  for line in pipeData.stdout:
    conn.send(line)
  conn.close()
sys.exit(0)

