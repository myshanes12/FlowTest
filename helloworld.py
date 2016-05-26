import thread
import time
import os
import sys
from sys import argv
import signal


class Gracefulexit:
    kill_now=False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)
    def exit_gracefully(self,signum, frame):
        print'do something'
        self.kill_now = True

def ThreadFunc():
    while(True):
        time.sleep(2)
        print'Im alive'

cmd = argv
if(len(cmd)>1): 
    print 'Start with: '
    print cmd[1]
else:
    print 'Start'

thread.start_new_thread(ThreadFunc,())

killer = Gracefulexit()
while(True):
    print'Main Thread'
    if killer.kill_now:
       break
    time.sleep(1)
print'exit gracefully'

