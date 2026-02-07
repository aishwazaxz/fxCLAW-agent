import signal
import time
import sys

def handler(sig, frame):
    print("received signal, ignoring")

signal.signal(signal.SIGTERM, handler)
signal.signal(signal.SIGINT, handler)

print("fxCLAW agent running")

while True:
    time.sleep(3600)
