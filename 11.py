def frange(start, stop, step):
    i = start-step
    while i < stop-step*2:
       i += step 
       yield round(i, len(str(step))-1)
for i in frange(1, 6, 0.1):
    print(i)