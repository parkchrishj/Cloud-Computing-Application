# import os
# from os.path import join
# from time import sleep
import time
# from streamparse import Spout
import storm


class FileReaderSpout(storm.Spout):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self._complete = False
        fileName = self._conf['inputFile']
        storm.logInfo("Spout instance starting...")

        # TODO:
        # Task: Initialize the file reader
        self._f = open(fileName, 'r')
        # End

    def nextTuple(self):
        # TODO:
        # Task 1: read the next line and emit a tuple for it
        # Task 2: don't forget to sleep for 1 second when the file is entirely read to prevent a busy-loop
        # with self._f as fp:
        #     line = fp.readline()
        #     while line:
        #         storm.logInfo("sentence: %s" %line)
        #         storm.emit([line])
        #         line = fp.readline()
        #     sleep(1)
        # with self._f as fp:
        #     line = fp.readline()
        #     if line != None:
        #         storm.logInfo("sentence: %s" %line)
        #         storm.emit([line])
        #         line = fp.readline()
        sentence = self._f.readline()
        if sentence == "":
            time.sleep(1)
        else:
            storm.emit([sentence])
        # End


# Start the spout when it's invoked
FileReaderSpout().run()
