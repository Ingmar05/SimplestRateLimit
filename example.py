from ratelimiter import rateLimiter
import time

rl = rateLimiter()

for i in range(10+1):
    name = "myVariable"
    time.sleep(.25)
    #Ratelimit to 300ms
    if not rl.rateLimit(name, 300):
        #Print if not rate limited
        print(name + " = " + str(i))
