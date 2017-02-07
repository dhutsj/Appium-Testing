#!/usr/bin/env monkeyrunner
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

device = MonkeyRunner.waitForConnection()
#pic=device.takeSnapshot()
newpic=device.takeSnapshot()
shot=MonkeyRunner.loadImageFromFile('./shot'+'.png')
#newpic.writeToFile('./shot1.png','png')
#print (newpic.sameAs(shot,0.90))
flag=newpic.sameAs(shot,0.90)
if (flag == True):
    print 'Login&Logout Case passed'
else:
    print 'Login&Logout Case failed'

