"""
This is another pass at the merge meeting times 
I want to sort the meeting times list then check if I can merge neighbors or not.

"""

meetingTimes = [ (2, 6), (1, 2), (3, 5), (7, 9)]


# def mergeMeetings(meetingTimes):
sortedMeetings = sorted(meetingTimes)
mergedMeetings = [sortedMeetings[0]]
for startVal,endVal in sortedMeetings[1:]:
    lastMergedStart, lastMergedEnd = mergedMeetings[-1]
    if startVal <= lastMergedEnd: # they overlap
        mergedMeetings[-1] = (lastMergedStart, max(endVal, lastMergedEnd))
    else: # they don't overlap
        mergedMeetings.append((startVal,endVal))







