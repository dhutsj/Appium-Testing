#!/usr/bin/env monkeyrunner
from com.android.monkeyrunner import MonkeyRunner,MonkeyDevice,MonkeyImage

device = MonkeyRunner.waitForConnection()
pic=device.takeSnapshot()
pic.writeToFile('./shot.png','png')
