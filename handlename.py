import re
from funcName import handleName



class PictureFileName:
    def __init__(self, item, sName, methodGetName, excludeFirstC):
        self.method = methodGetName
        self.name = sName
        self.STT = False
        self.item = item
        # this method using when picture file has index.
        if self.method == 0:
            t = ''
            raw = no_accent_vietnamese(self.name).lower().split('.jpg')[0].split(' ')
            self.STT = raw[0]
            for item in raw[1:]:
                t += ' '
                for ch in item:
                    if (ch in ' abcdefghijklmnopqrstuvwxyz'):
                        t += ch
            self.no_accent_name = t.strip()

        # mothod with name and index.
        if self.method == 1:
            t = ''
            stt = ''
            raw = no_accent_vietnamese(self.name).lower().split('.jpg')[0].split('sn')[0]
            for i in raw:
                if i in '0123456789':
                    stt += i
                else:
                    break
            self.STT = stt
            for item in raw:
                for ch in item:
                    if (ch in ' abcdefghijklmnopqrstuvwxyz'):
                        t += ch
            self.no_accent_name = t.strip()
            # try:
            #     getDate = no_accent_vietnamese(self.name).lower().split('.jpg')[0].split('sn')[1]
            #     if getDate.index('vd') >= 0:
            #         self.date = getDate.split('vd')[0].strip()
            #     else:
            #         self.date = 'Missing'
            # except IndexError:
            #     print(getDate)

        # method for file name only have name and date of born.
        if self.method == 2:
            firstDateIndex = -1
            for e in self.name:
                if e in '0123456789':
                    firstDateIndex  = self.name.index(e)
                    self.no_accent_name = no_vietnamese(self.name[:firstDateIndex].strip()).split('sn')[0]
                    break
            if firstDateIndex < 0:
                self.no_accent_name = no_vietnamese(self.name).split('jpg')[0].strip().split('sn')[0]
                self.date = 'Missing'
                self.lastFourC = 'Missing'
                return
            self.date = self.name[firstDateIndex:].lower().split('.jpg')[0].strip()
            self.lastFourC = self.date.split(' ')[0].split(',')[0][-4:]

        # method excluded stt. get name and year of born.
        if self.method == 3:
            for e in self.name:
                if e.lower() in ' abcdefghijklmnopqrstuvwxyz':
                    firstNameCharacter = self.name.index(e)
                    newName = self.name[firstNameCharacter:].strip()
                    break
            firstDateIndex = -1
            for e in newName:
                if e in '0123456789':
                    firstDateIndex = newName.index(e)
                    self.no_accent_name = no_vietnamese(newName[:firstDateIndex].strip()).split('sn')[0]
                    break
            if firstDateIndex < 0:
                self.no_accent_name = no_vietnamese(newName).split('jpg')[0].strip().split('sn')[0]
                self.date = 'Missing'
                self.lastFourC = 'Missing'
                return
            self.date = newName[firstDateIndex:].lower().split('.jpg')[0].strip()
            self.lastFourC = self.date.split(' ')[0].split(',')[0][-4:]

        if self.method == 4:
            aRaw = handleName(self.name, excludeFirstC)
            self.STT = aRaw[0]
            self.date = aRaw[2]
            self.no_accent_name = no_vietnamese(aRaw[1])
            self.raw_name = aRaw[1]
            # print(aRaw[1])
        try:
            if self.STT:
                self.STT = int(self.STT)
        except ValueError:
            self.STT = 0

def no_accent_vietnamese(s):
    # s = s.encode('utf-8').decode('utf-8')
    s = re.sub('[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub('[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub('[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub('[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub('[òóọỏõôồốộổỗơờớợởỡ]', 'o', s)
    s = re.sub('[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠ]', 'O', s)
    s = re.sub('[ìíịỉĩ]', 'i', s)
    s = re.sub('[ÌÍỊỈĨ]', 'I', s)
    s = re.sub('[ùúụủũưừứựửữ]', 'u', s)
    s = re.sub('[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub('[ỳýỵỷỹ]', 'y', s)
    s = re.sub('[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub('[Đ]', 'D', s)
    s = re.sub('[đ]', 'd', s)
    return s.encode('utf-8').decode('utf-8').lower()


def no_vietnamese(s):
    result = ''
    try:
        for i in no_accent_vietnamese(s):
            if (i in ' abcdefghijklmnopqrstuvwxyz'):
                result += i
        return result.strip()
    except TypeError:
        return ''