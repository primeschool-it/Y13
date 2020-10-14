# Continue, break

import time
for i in range(0,50):
    time.sleep(.1)
    if i == 11:
        break
    print (i)

#Continue
for i in range(0, 300):
    time.sleep(.5)
    if (i % 3) == 0 or (i % 5) == 0:
        continue
    print(i)

