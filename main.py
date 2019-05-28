import handlename
import re
import os
from openpyxl import load_workbook
import glob
import datetime


from handlename import PictureFileName, no_vietnamese

# t = PictureFileName("698 TRẦN VẠN NHIỆM.jpg", 0)




def handleName(name, methodType, rowStart):

    # function handle change name if matched.
    def handleChangeName():
        try:
            os.rename(o.filePath, './result/' + name + '/' + str(cell_cmnd) + '.jpg')
            text = 'OK: ' + cell_name, ' is changed to ', cell_cmnd
            print(text)
            aListOutput.append(text)
        except FileExistsError:
            os.rename(o.filePath,
                      './result/' + name + '/' + str(cell_cmnd) + '_' + cell_name + '.jpg')
            text = 'Warning: ' + cell_name, ' is changed to ', str(
                cell_cmnd) + '_' + cell_name + ' due to duplicated identify number.'
            print(text)
            aListOutput.append(text)
        except FileNotFoundError:
            text = 'Error: not found picture file ', o.filePath
            print(text)
            aListOutput.append(text)

    # get list file name.
    filePath1 = './result/' + name + '/*.jpg'
    filePath2 = './result/' + name + '/*.JPG'
    dataPath = './result/' + name + '/' + name + '.xlsx'
    aListFile = [f for f_ in [glob.glob(e) for e in [filePath1, filePath2]] for f in f_] #list picture file name

    aListOutput = [] #using to trace log

    aListFileName = []
    for item in aListFile:
        fileName = item[len('./result/' + name ) + 1 :]
        o = PictureFileName(fileName.encode('utf-8').decode('utf-8'), methodType)
        o.filePath = './result/' + name + '/' + o.name
        aListFileName.append(o)

        # This code use for checking data analyze!!!
    #     try:
    #         print(item, ' ', o.no_accent_name, o.date)
    #     except AttributeError:
    #         print('oop!')
    # return

    wb = load_workbook(dataPath)
    # select demo.xlsx
    # from openpyxl import load_workbook
    # wb2 = load_workbook('test.xlsx')
    # ws4 = wb2["New Title"]
    sheet = wb.active
    # get max row count
    max_row = sheet.max_row
    # get max column count
    max_column = sheet.max_column

    for i in range(rowStart, max_row + 1):
        if sheet.cell(row=i, column=1) and sheet.cell(row=i, column=1).value and isinstance(
                sheet.cell(row=i, column=1).value, int) and sheet.cell(row=i, column=1).value >= 1:
            info = ''
            cell_stt = sheet.cell(row=i, column=1).value
            cell_name = sheet.cell(row=i, column=2).value
            if cell_name:
                if sheet.cell(row=i, column=3).value:
                    cell_namSinh = sheet.cell(row=i, column=3).value
                else:
                    cell_namSinh = sheet.cell(row=i, column=4).value
                cell_cmnd = sheet.cell(row=i, column=6).value
                cell_tinh = sheet.cell(row=i, column=5).value
        else:
            continue
        # print(cell_name)
        for o in aListFileName:
            try:
                # print(cell_name)
                if o.STT:
                    if o.STT == cell_stt:
                        handleChangeName()
                else:
                    if no_vietnamese(cell_name).strip() in o.no_accent_name.strip():
                        if o.date:
                            try:
                                if str(cell_namSinh.year) in o.date or o.date == 'Missing':
                                    handleChangeName()
                            except AttributeError:
                                if o.lastFourC in cell_namSinh or o.date == 'Missing':
                                    handleChangeName()
                        else:
                            handleChangeName()
            except ValueError:
                pass
                text = 'Error: file name can not analyze: ' + o.filePath
                print(text)
                aListOutput.append(text)
            except AttributeError:
                print('check')
            except TypeError:
                print(o.name)

    writeListToTextFile(aListOutput, './result/' + name + '/log.txt')


def writeListToTextFile(list, filePath, mode='a'):
    ''' Write list to csv line by line '''
    with open(filePath, mode, encoding="utf8") as myfile:
        for item in list:
            myfile.write(str(item) +  '\n')

# handleName('BV_DaKhoaTinhBinhPhuoc', 0, 8)
# handleName('TT_YTeHuyenLocNinh', 1, 6)
# handleName('TT_YTeHuyenHonQuan', 1, 9)
# handleName('BV_HoanMyBinhPhuoc', 2, 9)
# handleName('BV_YHocCoTruyenBinhPhuoc', 2, 7)
# handleName('CC_DanSoBinhPhuoc', 2, 12)
# handleName('CC_VeSinhAnToanThucPham', 2, 15)
# handleName('CT_CoPhanDuocVatTuYTeDopharco', 2, 8)
# handleName('TT_GiamDinhPhapYTinhBinhPhuoc', 2, 6)
# handleName('TT_KiemNghiemDuocPhamMyPhamTinhBinhPhuoc', 2, 8)
# handleName('TT_KiemSoatBenhTatTinhBinhPhuoc', 2, 7)
# handleName('TT_YTeBuGiaMap', 2, 8)
# handleName('TT_YTeHuyenDongPhu', 2, 8)
# handleName('TT_YTeHuyenLocNinh', 2, 6)
# handleName('TT_YTeThiXaBinhLong', 2, 10)
# handleName('TT_YTeThiXaDongXoai', 2, 5)


# part2

# handleName('TrungTamYTeHuyenChonThanh', 2, 9)
# handleName('TrungTamYTeHuyenPhuRieng', 1, 8)
# handleName('TruongCaoDangYTeBinhPhuoc', 2, 9)
handleName('TrungTamYTeHuyenBuDang', 2, 12)


