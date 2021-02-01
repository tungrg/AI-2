# Doc File
fopen = open('caphanhchinh.pl', 'r')
a = fopen.readlines()
fopen.close()
#tạo các list để lưu các vị từ cơ bản
lcountry = []
lregion = []
lprovince = []
lcity = []
ldistrict = []
lward = []
lcommune = []
linclude = []
#duyệt từng dòng trong a
for key in a:
    #thêm country vào lcountry
    if 'country' in key and key.rfind('country') == 0:
        start = key.rfind('(') + 1
        end = key.rfind(')')
        lcountry.append(key[start:end])
    #thêm region vào lregion
    if 'region' in key and key.rfind('region') == 0:
        start = key.rfind('(') + 1
        end = key.rfind(')')
        lregion.append(key[start:end])
    #thêm province vào lprovince
    if 'province' in key and key.rfind('province') == 0:
        start = key.rfind('(') + 1
        end = key.rfind(')')
        lprovince.append(key[start:end])
    #thêm city vào lcity
    if 'city' in key and key.rfind('city') == 0:
        start = key.rfind('(') + 1
        end = key.rfind(')')
        lcity.append(key[start:end])
    #thêm district vào ldistrict
    if 'district' in key and key.rfind('district') == 0:
        start = key.rfind('(') + 1
        end = key.rfind(')')
        ldistrict.append(key[start:end])
    #thêm ward vào lward
    if 'ward' in key and key.rfind('ward') == 0:
        start = key.rfind('(') + 1
        end = key.rfind(')')
        lward.append(key[start:end])
    #thêm commune vào lcommune
    if 'commune' in key and key.rfind('commune') == 0:
        start = key.rfind('(') + 1
        end = key.rfind(')')
        lcommune.append(key[start:end])
    #thêm include vào linclude
    if 'include' in key and key.rfind('include') == 0:
        start = key.rfind('(') + 1
        dau = key.rfind(',')
        end = key.rfind(')')
        linclude.append((key[start:dau], key[dau+1:end]))
#tạo lincludeleft lưu lại vế trái của linclude
lincludeleft = []
for i in range(len(linclude)):
    lincludeleft.append(linclude[i][0])
#tạo lincluderight lưu lại vế phải của linclude
lincluderight = []
for i in range(len(linclude)):
    lincluderight.append(linclude[i][1])

#hàm kiểm tra quốc gia có tồn tại trong cơ sở tri thức
def country(Name):
    if Name in lcountry:
        return True
    return False

#hàm kiểm tra khu vực có tồn tại trong cơ sở tri thức
def region(Name):
    if Name in lregion:
        return True
    return False

#hàm kiểm tra tỉnh có tồn tại trong cơ sở tri thức
def province(Name):
    if Name in lprovince:
        return True
    return False

#hàm kiểm tra thành phố có tồn tại trong cơ sở tri thức
def city(Name):
    if Name in lcity:
        return True
    return False

#hàm kiểm tra huyện có tồn tại trong cơ sở tri thức
def district(Name):
    if Name in ldistrict:
        return True
    return False

#hàm kiểm tra phường có tồn tại trong cơ sở tri thức
def ward(Name):
    if Name in lward:
        return True
    return False

#hàm kiểm tra xã có tồn tại trong cơ sở tri thức
def commune(Name):
    if Name in lcommune:
        return True
    return False

#Hàm kiểm tra xem A có bao gồm B(dưới 1 cấp)
# ví dụ : thành phố A có bao gồm phường B hay không?

def include(A, B):
    temp = []
    #nếu (A,B) trong list linclude thì trả về true
    if (A, B) in linclude:
        return True
    #Nếu A không nằm trong list lincludeleft
    elif A not in lincludeleft:
        #duyệt từng phần tử trong list linclude
        for name in linclude:
            #nếu B trùng với phần tử  1
            if B == name[1]:
                fw.write('\t' + A + ' = ' + name[0] + '\n')
        return temp
    #Nếu B không nằm trong list lincluderight
    elif B not in lincluderight:
        #duyệt từng phần tử trong list linclude
        for name in linclude:
            #nếu A trùng với phần tử 0
            if A == name[0]:
                fw.write('\t' + B + ' = ' + name[1] + '\n')
        return True
    return False

#Hàm kiểm tra A có thuộc B hay không(trên 1 cấp hành chính)
#ví dụ: tỉnh A  có thuộc khu vực B hay không
def belongto(A, B):
    if include(B, A):
        return True
    return False

#hàm kiểm tra A có bao gồm C hay không(dưới nhiều cấp hành chính)
#ví dụ: khu vực A có bao gồm xã C hay không
def includes(A, C):
    for name in linclude:
        if (name[1], C) in linclude:
            return True
        if (A, name[1]) in linclude:
            include(name[0], C)
            includes(name[1], C)
            return False
    return False

#hàm kiểm tra A có thuộc C hay không(dưới nhiều cấp hành chính)
#ví dụ: xã A có thuộc khu  vực C hay không
def belongsto(A, C):
    for name in linclude:
        if (C, name[0]) in linclude:
            return True
        if (name[0], A) in linclude:
            belongto(name[1], C)
            belongsto(name[0], C)
            return False
    return False

#hàm kiểm tra A,B có thuộc cùng 1 khu vực hành chính hay không
#xã A và xã B có thuộc cùng một huyện hay không?
def sibling(A, B):
    for name in linclude:
        if (name[0], A) in linclude:
            linclude.remove((name[0], A))
            include(name[0], B)
            linclude.append((name[0], A))
            if B == 'X' or B == 'x':
                return False
            else:
                return True
    return False

#Bộ câu hỏi test
fopen = open('20-Questions_2.txt', 'r')
any_questions = fopen.readlines()
fopen.close()
any_questions[len(any_questions)-1] += '\n'
#hàm ghi kết quả xuống file
def writeFile(answer, fwrite):
    if answer == False:
            fwrite.write(f'\tfalse.\n')
    else:
        if answer == True:
            fwrite.write(f'\ttrue.\n')
        else:
            for key in answer:
                fwrite.write(f'\tX = {key[0]}\n')
#file chứa kết quả
fw = open("Answer3_2.txt", "w")
def handleFile(questions, fwrite):
    count = 1
    for key in questions:
        start=key.rfind('(') + 1
        dau = key.rfind(',')
        end = key.rfind(')')
        if key[3:start-1] == "include":

            fwrite.write(f'{count}. {key}')
            answer = include(key[start:dau],key[dau+1:end])
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "includes":

            fwrite.write(f'{count}. {key}')
            answer = includes(key[start:dau],key[dau+1:end])
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "belongto":

            fwrite.write(f'{count}. {key}')
            answer = belongto(key[start:dau],key[dau+1:end])
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "belongsto":

            fwrite.write(f'{count}. {key}')
            answer = belongsto(key[start:dau],key[dau+1:end])
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "sibling":

            fwrite.write(f'{count}. {key}')
            answer = sibling(key[start:dau],key[dau+1:end])
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "country":

            fwrite.write(f'{count}. {key}')
            answer = (key[start:dau],key[dau+1:end])
            count += 1
            writeFile(answer,fwrite)
    fwrite.close()


handleFile(any_questions,fw)

