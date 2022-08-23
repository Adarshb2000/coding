def maxPresentations(scheduleStart, scheduleEnd):
    things = [[endTime, startTime] for startTime, endTime in zip(scheduleStart, scheduleEnd)]
    
    things.sort()
    
    currEnd = things[0][0]
    
    answer = 1
    
    for end, start in things[1 :]:
        if start >= currEnd:
            answer += 1
            currEnd = end
            
    
    return answer

print(maxPresentations([3, 3, 7, 2, 3, 5], [7, 6, 15, 4, 7, 8]))