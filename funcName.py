def handleName(name, excludeFirstC = False):
    if "Lâm" in name:
        a = 1

    name = name.lower()
    firstStt = -1
    firstName = -1
    firstDayOfBorn = -1
    realStt = ''
    for ind, e in enumerate(name):
        if e in '0123456789':
            if firstStt < 0 and ind < 5:
                firstStt = ind
            elif (firstDayOfBorn < 0 or firstDayOfBorn < (firstStt + 5)) and ind > 10:
                firstDayOfBorn = ind
        if e in ' abcdefghijklmnopqrstuvwxyzđêơôơăâư':
            if firstName < 0:
                firstName = ind

    if firstStt > firstName:
        fisrtStt = -1
    if firstStt >= 0:
        stt = name[0:firstName]

        for e in str(stt):
            if e in '0123456789':
                realStt += e
        # print('first stt: ', firstStt, ' stt: ', name[0:firstName])
    if firstDayOfBorn >= 0:
        fullname = name[firstName:firstDayOfBorn]
        namsinh = name[firstDayOfBorn:]
        # print('first name: ', firstName, ' name: ', name[firstName:firstDayOfBorn])
        # print('first day: ', firstDayOfBorn, ' day: ', name[firstDayOfBorn:])
    else:
        fullname = name[firstName:]
        namsinh = ''
        # print('first Name: ', firstName, ' name: ', name[firstName:])
    fullname = fullname.split('.jpg')[0].split('sn')[0]. \
                split('ns')[0].split(',')[0]\
                .split('-')[0]\
                .strip()
    if excludeFirstC:
        fullname = ' '.join(fullname.split(' ')[1:]).strip()
    namsinh = namsinh.split('.jpg')[0].split('_')[0].strip()

    return [realStt, fullname, namsinh]

