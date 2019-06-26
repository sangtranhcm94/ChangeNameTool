def handleName(name):
    firstStt = -1
    firstName = -1
    firstDayOfBorn = -1
    for ind, e in enumerate(name.lower()):
        if e in '0123456789':
            if firstStt < 0 and ind < 5:
                firstStt = ind
            elif firstDayOfBorn < 0 or firstDayOfBorn < (firstStt + 5):
                firstDayOfBorn = ind
        if e in ' abcdefghijklmnopqrstuvwxyz':
            if firstName < 0:
                firstName = ind
    if firstStt > firstName:
        fisrtStt = -1
    if firstStt >= 0:
        print('first stt: ', firstStt, ' stt: ', name[0:firstName])
    if firstDayOfBorn >= 0:
        print('first name: ', firstName, ' name: ', name[firstName:firstDayOfBorn])
        print('first day: ', firstDayOfBorn, ' day: ', name[firstDayOfBorn:])
    else:
        print('first Name: ', firstName, ' name: ', name[firstName:])


handleName('Tran hoang sang 20-08-1994')