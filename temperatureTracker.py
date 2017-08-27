"""
This tracks the max, min, mean, and mode temperature of a temperature logger.

insert()
get_max()
get_min()
get_mean()
get_mode()

If there is more than one mode, return any of the modes.

get_mean returns a float. All temperatures are ints otherwise.

as new temperatures come in via insert function keep track of max, min, total number of temperatures and sum temperature (for mean), and a dict histogram for mode.

"""

import random

class tempTracker:# {{{
    def __init__(self):# {{{
        self.min = None
        self.max = None
        self.mean = None
        self.mode = None
        self._sumTemp = 0
        self._countTemp = 0
        self._tempHist = {} # this is the one 'memory intesive' part of the code. I make a histogram of all temperatures I record.}}}

    def insert(self,temperature):# {{{
        """ temperature (int) 
        returns (null)
        Don't acutally keep all of the temperautres just update the variables accordingly.
        """

        # initialize on first temp
        if self.min == None:
            self.min = temperature
            self.max = temperature
            self.mean = temperature
            self.mode = temperature
        else:
            # set min and max
            if temperature < self.min:
                self.min = temperature
            if temperature > self.max:
                self.max = temperature
            
        # set mean
        self._sumTemp += temperature
        self._countTemp += 1
        self.mean = float(self._sumTemp) / float(self._countTemp)

        # set mode
        currentTempCount = self._tempHist.get(temperature)
        if currentTempCount == None:
            self._tempHist.update({temperature: 1})
        else:
            self._tempHist.update({temperature: currentTempCount + 1})

        modeTempCount = self._tempHist.get(self.mode)
        if currentTempCount > modeTempCount:
            self.mode = temperature# }}}

    def get_max(self):# {{{
        return self.max# }}}

    def get_min(self):# {{{
        return self.min# }}}

    def get_mean(self):# {{{
        return self.mean# }}}

    def get_mode(self):# {{{
        return self.mode# }}}
# }}}

        
tracker = tempTracker()

tempList = [random.randint(70,90) for i in range(100)]
for temp in tempList:
    tracker.insert(temp)




