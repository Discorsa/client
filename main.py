import ac; import acsys  # https://github.com/ckendell/ACAppTutorial/blob/master/ACAppTutorial.md#accessing-shared-memory                                                                                                                                      # noqa: F401
import os; import sys; import pathlib; import threading; import subprocess; import time; import datetime; from datetime import datetime, timezone, timedelta    # noqa: F401, F811
from shared_memory.sim_info import *                                                                                                                            # noqa: F403
from . import wrapper                                                                                                                                           # noqa: F401
simInfo = simInfo()                                                                                                                                             # noqa: F405


# Define some basic information about the app ig
appName = 'Discorsa'
appHeight = 400
appWidth = 250

def acMain(ac_version):
    global appWindow
    appWindow = ac.newApp(appName)
    ac.setTitle(appWindow, appName)
    ac.setSize(appWindow, appWidth, appHeight)