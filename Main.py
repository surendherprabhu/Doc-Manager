import sys
import os as os1
import platform
from DSA import *
from App import *
from GUI import *



os = str(platform.system())

OS = (OS_Dict[os])

app =  App(OS = 0,directory="sample")
app.sort()

