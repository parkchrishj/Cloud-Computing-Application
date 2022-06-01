import heapq
from collections import Counter

import storm


class TopNFinderBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")

        # TODO:
        # Task: set N
        # pass
        # End
        self._N = self._conf['N']
        self._dict_items = {}
        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        '''
        TODO:
        Task: keep track of the top N words
        Hint: implement efficient algorithm so that it won't be shutdown before task finished
              the algorithm we used when we developed the auto-grader is maintaining a N size 
              min-heap
        '''
        word = tup.values[0]
        count = int(tup.values[1])
        #
        # dict_word = {"yolo":4,"hello": 10,"hello": 12, "heyyo": 9, "hela": 6, "biggest": 20, "smallest": 1}
        # print(dict_word)
        # list_word = list(dict_word.items())
        # print(heapq.nlargest(3,list_word, key = lambda kv:(kv[1],kv[0]) ))
        #
        self._dict_items[word] = count
        list_word = list(self._dict_items.items())
        top_ten_items = heapq.nlargest(self._N,list_word, key = lambda kv:(kv[1],kv[0]))
        answer = ""
        counter = 1
        for item in top_ten_items:
            if counter < self._N:
                answer += item[0] + ", "
                counter += 1
            else:
                answer += item[0]
        storm.logInfo("top-N %s" %answer)
        storm.emit(["top-N", answer])
        #
        # heapq.heappush(self._heap_items, (word,count))
        # top_ten_items = heapq.nlargest(10, self._list_items)
        # answer = ""
        # counter = 0
        # for item in top_ten_items:
        #     if counter < 10:
        #         answer += item[0] + ", "
        #         counter += 1
        #     else:
        #         answer += item[0]
        # storm.emit([answer])
        # pass
        # End


# Start the bolt when it's invoked
TopNFinderBolt().run()