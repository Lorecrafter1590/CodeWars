def elevator_distance(elevatorLevels):
    distanceArray = []
    for x in range (1,len(elevatorLevels)):
        distanceArray.append(abs(elevatorLevels[x]-elevatorLevels[x-1]))
    return sum(distanceArray)