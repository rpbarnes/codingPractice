"""
This finds a duplicate in a list using O(n) time and O(1) space.

start from last element of list and find the cycle with the fast and slow jogger approach.

"""
class findDuplicateInt ():
    def __init__(self, numberList):
        self.numberList = numberList
        cycleLength = self.detectCycle()
        self.duplicate = self.findDuplicate(cycleLength)

    def detectCycle(self):
        """
        finds cycle and returns length of cycle
        """
        slowP = self.numberList[-1]
        fastP = self.numberList[-1]
        while True:
            # step fast twice and slow once
            fastP = self.numberList[fastP - 1]
            fastP = self.numberList[fastP - 1]
            slowP = self.numberList[slowP - 1]
            print fastP, slowP
            if slowP == fastP:
                cycleVal = slowP
                break
        count = 0
        while True:
            count += 1
            slowP = self.numberList[slowP - 1]
            if slowP == cycleVal:
                return count

    def findDuplicate(self, cycleLength):
        behind = self.numberList[-1]
        ahead = self.numberList[-1] 
        for i in range(cycleLength):
            ahead = self.numberList[ahead - 1]
        
        while ahead != behind: # This is the start of the cycle
            ahead = self.numberList[ahead - 1]
            behind = self.numberList[behind - 1]
        
        return ahead



numList = [2,3,1,4,3,5]
#numList = [2,1,4,5,3,1]

a = findDuplicateInt(numList)
print a.duplicate

