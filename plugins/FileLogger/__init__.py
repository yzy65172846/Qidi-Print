# Copyright (c) 2015 QIDI B.V.
# QDTECH is released under the terms of the LGPLv3 or higher.

#Shoopdawoop
from . import FileLogger


def getMetaData():
    return {
    }

def register(app):
    return { "logger": FileLogger.FileLogger("{0}.log".format(app.getApplicationName())) }
