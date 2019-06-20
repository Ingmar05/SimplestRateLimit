previousTime = {}

def rateLimit(name, delay):
    currentTime = int(round(time.time() * 1000))
    #Name called for the first time
    if name not in previousTime:
        previousTime.update( {name : currentTime} )
        return False
    #Name has called been called too fast
    elif currentTime - previousTime[name] < delay:
        return True
    #Name is allowed
    else:
        previousTime[name] = currentTime
        return False
