import time
import random

print "You cast your line, hoping for a bite."

seconds = random.randint(1,10)

for i in range(0,seconds):
	time.sleep(1)
	print "..."
	
time.sleep(1)	
print "You caught one! It only took %d hours!" % seconds

raw_input("[CONTINUE]")
