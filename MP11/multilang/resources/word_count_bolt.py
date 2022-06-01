import storm
# Counter is a nice way to count things,
# but it is a Python 2.7 thing
from collections import Counter


class CountBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")
        self._count = Counter()
        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        # TODO
        # Task: word count
        # Hint: using instance variable to tracking the word count
        # thisdict = {}
        # for word in tup:
        #     self._count[word] += 1
        #     thisdict[word] = self._count[word]
        word = tup.values[0]
        self._count[word] += 1
        count = self._count[word]
        count = str(count)
        storm.logInfo("Emitting %s:%s" % (word, count))
        storm.emit([word,count])
        # storm.emit((word,self._count[word]))
        # End


# Start the bolt when it's invoked
CountBolt().run()
