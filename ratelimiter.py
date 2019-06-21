# SimplestRateLimit
# https://github.com/Ingmar05/SimplestRateLimit
# The simplest python rate limiting library in existence (probably).
#Originally created for rate limiting ROS callbacks.

import time

class rateLimiter:

    def __init__(self):
        self.previousTime = {}

    def rateLimit(self, name, delay):
        self.currentTime = int(round(time.time() * 1000))
        #Name called for the first time
        if name not in self.previousTime:
            self.previousTime.update( {name : self.currentTime} )
            return False
        #Name has called been called too fast
        elif self.currentTime - self.previousTime[name] < delay:
            return True
        #Name is allowed
        else:
            self.previousTime[name] = self.currentTime
            return False
