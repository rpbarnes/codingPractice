"""
This takes a list of tuples of all meeting times for a company and finds any slots where everyone is free.

such as
  [(1, 2), (2, 6), (3, 5), (7, 9)]

and returns
  [(1,6), (7,9)]

I want to make a list that keeps track of the blocks of time that everyone is busy.
"""

meetingTimes = [ (1, 2), (2, 6), (3, 5), (7, 9)]
meetingTimes = [(1, 2), (2, 3)]
existingMeetings = []

for count,meeting in enumerate(meetingTimes):
    if count == 0:
        existingMeetings.append(meeting)
    else:
        for count1,existingMeeting in enumerate(existingMeetings):
            overlap = False
# check if the meeting starts before and handle cases necessary
            if meeting[0] < existingMeeting[0]: # meeting starts before existingMeeting starts
                currentStart = meeting[0]
                if meeting[1] >= existingMeeting[0]: # meeting finishes after existingMeeting starts or just as meeting starts. Now update this block
                    overlap = True
                    if meeting[1] > existingMeeting[1]:
                        currentEnd = meeting[1]
                    else:
                        currentEnd = existingMeeting[1]
                else:
                    currentEnd = meeting[1]
# check if the thing overlaps on the after slot.
            elif (meeting[0] <= existingMeeting[1]) and (meeting[0] >= existingMeeting[0]): # the meeting starts during another
                overlap = True
                currentStart = existingMeeting[0]
                if meeting[1] > existingMeeting[1]:
                    currentEnd = meeting[1]
                else:
                    currentEnd = existingMeeting[1]
# the meeting starts after this meeting ends and there is no overlap
            else:
                currentStart = meeting[0]
                currentEnd = meeting[1]
            if overlap:
                existingMeetings[count1] = (currentStart, currentEnd)
                break

        if (currentStart==meeting[0]) and (currentEnd==meeting[1]):
            print 'there is no overlap with an existing meeting block, creating a new slot'
            existingMeetings.append(meeting)
            








    
