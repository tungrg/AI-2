# Doc File
fopen = open('cayphahe.pl', 'r')
a = fopen.readlines()
fopen.close()
#Các list lưu các vị từ cơ bản
lmale = []
lfemale = []
lparent = []
lmarried = []
ldivorced = []
#tạo cơ sở tri thức từ từng dòng trong file ban đầu
for key in a:
    #Thêm male vào list lamle
    if 'male' in key and key.rfind('male') == 0:
        start = key.rfind('(') + 1
        end = key.rfind(')')
        lmale.append(key[start:end])
    #thêm female vào list lfemale
    if 'female' in key and key.rfind('female') == 0:
        start = key.rfind('(') + 1
        end = key.rfind(')')
        lfemale.append(key[start:end])
    #them parent vào list lparent
    if 'parent' in key and key.rfind('parent') == 0:
        start = key.rfind('(') + 1
        dau = key.rfind(',')
        end = key.rfind(')')
        lparent.append((key[start:dau],key[dau+1:end]))
    #Thêm những người đã cưới vào list lmarried
    if 'married' in key and key.rfind('married') == 0:
        start = key.rfind('(') + 1
        dau = key.rfind(',')
        end = key.rfind(')')
        lmarried.append((key[start:dau], key[dau+1:end]))
    #them những người đã li dị vào list ldivorced
    if 'divorced' in key and key.rfind('divorced') == 0:
        start = key.rfind('(') + 1
        dau = key.rfind(',')
        end = key.rfind(')')
        ldivorced.append((key[start:dau], key[dau+1:end]))
#hàm kiểm tra Person có là nam trong cơ sở tri thức hay không
def male(Person):
    if Person in lmale:
        return True
    return False
#hàm kiểm tra Person có là nữ trong cơ sở tri thức hay không
def female(Person):
    if Person in lfemale:
        return True
    return False
#hàm kiểm tra Person có là người trong cơ sở tri thức hay không
def checkPerson(Person):
    #kiểm tra bằng cách xét người đó có trong list lmale hay lfemale hay không
    list_people = []
    list_people = lmale+lfemale
    if Person in list_people:
        return True
    return False
#Hàm kiểm tra Person1 và Person có kết hôn hay không
#hoặc tìm người đã kết hôn với Person2
def married(Person1, Person2):
    #Kiểm tra xem thử có phải yêu cầu tìm người không
    if Person1 == 'X' or Person1 == 'x':
        list = []
        #xét trong danh sách những người đã kết hôn để tìm người kia
        for couple in lmarried:
            if couple[0] == Person2:
                list.append((couple[1],couple[0]))
                return list
            if couple[1] == Person2:
                list.append((couple[0],couple[1]))
                return list
        return False
    #đối với yêu cầu kiểm tra thì xét trong danh sách những người đã kết hôn để trả về kết quả
    else:
        if (Person1,Person2) in lmarried:
            return True
        else:
            return False

#hàm kiểm tra Person1 có phải là cha/mẹ của Person2 hay không
#hoặc tìm con của Person1
#hoặc tìm cha/mẹ của Person2
def parent(Person1, Person2):
    #Nếu là tìm cha/mẹ của Person1
    if Person1 == 'X' or Person1 == 'x':
        count = 0
        list = []
        #duyệt list lparent để tìm
        for couple in lparent:
            if couple[1] == Person2:
                
                list.append((couple[0], couple[1]))
                count += 1
        #nếu không tìm thấy bất kỳ ai là cha/mẹ của Person1 thì trả về 0
        if count == 0:
            return 0
        else:
            return list
    #Nếu là tìm cha/mẹ của Person2
    if Person2 == 'X' or Person2 == 'x':
        count = 0
        list = []
        #duyệt list lparent để tìm
        for couple in lparent:
            if couple[0] == Person1:

                list.append((couple[0], couple[1]))
                count += 1
        #nếu không tìm thấy bất kỳ ai là cha/mẹ của Person2 thì trả về 0        
        if count == 0:
            return 0
        else:
            return list
    #Nếu là yêu cầu kiểm tra
    else:
        #Kiểm tra trong list lparent để đưa ra kết quả
        if (Person1, Person2) in lparent:
            return True
        else:
            return False
#Hàm kiểm tra Person1 và Person2 có li dị không
#hoặc tìm người đã li dị với Person1
def divorced(Person1, Person2):
    #Nếu là tìm người đã li dị với Person2
    if Person1 == 'X' or Person1 == 'x':
        list = []
        #Duyệt list ldivorced để đưa ra kết quả
        for couple in ldivorced:
            if couple[0] == Person2:
                list.append((couple[1],couple[0]))
                return list
            if couple[1] == Person2:
                list.append((couple[0],couple[1]))
                return list
        #nếu không tìm thấy ai phù hợp trong list ldivorced thì trả về false
        return False
    #Nếu là yêu cầu kiểm tra
    else:
        #Xét list ldivorced để đưa ra kết quả
        if (Person1,Person2) in ldivorced:
            return True
        else:
            return False
#Hàm kiểm tra Person có phải chồng của Wife hay không
#hoặc tìm  chồng của Wife
def husband(Person, Wife):
    #Nếu Wife không phải là female thì trả về false
    if female(Wife) == False:
        return False
    #Nếu là yêu cầu tìm chồng của Wife
    if Person =='X'or Person == 'x':
        list =[]
        if female(Wife):
            #tìm người đã kết hôn với Wife
            temp = married(Person,Wife)
            #nếu không tìm thấy thì trả về false
            if temp == False:
                return False
            else:
                list.append(temp[0])
                return list
    #nếu là yêu cầu kiểm tra
    #kiểm tra  wife có phải là female hay không
    #kiểm tra Person của phải là male không
    #kiểm tra 2 người đó đã kết hôn chưa
    if female(Wife) and married(Person, Wife) and male(Person):
        return True
    return False
#hàm kiểm tra Person của phải vợ của Husband hay không
#hoặc tìm vợ của Husband
def wife(Person, Husband):
    #Nếu husband không phải là male thì trả về false
    if male(Husband) == False:
        return False
    #Nếu là yêu cầu tìm wife của husband
    
    if Person =='X'or Person == 'x':
        list = []
        if male(Husband):
            #tìm người đã kết hôn với husband
            temp = married(Person, Husband)
            if temp == False:
                return False
            else:
                list.append(temp[0])
                return list
    #nếu là yêu cầu kiểm tra
    #kiểm tra  husband có phải là male hay không
    #kiểm tra Person của phải là female không
    #kiểm tra 2 người đó đã kết hôn chưa
    if male(Husband) and married(Person, Husband) and female(Person):
        return True
    return False
#Hàm kiểm tra Children có phải con của Parent hay không
#hoặc tìm Child ren của Parent
def child(Children,Parent):
    #nếu là yêu cầu tìm kiếm
    if Children =='X'or Children == 'x':
        #tìm parent của Children
        temp = parent(Parent,Children)
        #nếu không thì tìm thấy thì trả về false
        if temp == 0:
            return False
        list = []
        #nếu tìm thấy thì trả về list chứa parent của child
        for key in temp:
            list.append((key[1],key[0]))
        return list
    #nếu là yêu cầu kiểm tra thì kiểm tra hàm parent(Parent,Children) rồi trả kết quả về
    if parent(Parent,Children):
        return True
    return False
#hàm kiểm tra Parent có phải bố của child hay không
#hoặc tìm father của Child
def father(Parent, Child):
    #Nếu là yêu cầu tìm father của child
    if Parent == 'x' or Parent == 'X':
        #tìm Parent của child
        temp = parent(Parent, Child)
        if temp == 0:
            return False
        count = 0
        list = []
        #trong list parent của child xét những người là male thì thêm vào kết quả trả về
        for key in temp:
            if male(key[0]):
                list.append(key)
                count += 1
        if count == 0:
            return False
        return list
    #Nếu là yêu cầu kiểm tra thì
    #kiểm tra Parent có phải là male không
    #kiểm tra Parent có phải bố/mẹ của child ko
    if male(Parent) and parent(Parent, Child):
        return True
    return False
#hàm kiểm tra Parent có phải mẹ của child hay không
#hoặc tìm mẹ của Child
def mother(Parent, Child):
    #Nếu là yêu cầu tìm mother của child
    if Parent == 'x' or Parent == 'X':
        #tìm Parent của child
        temp = parent(Parent, Child)
        if temp == 0:
            return False
        count = 0
        list = []
        #trong list parent của child xét những người là female thì thêm vào kết quả trả về
        for key in temp:
            if female(key[0]):
                list.append(key)
                count += 1
        if count == 0:
            return False
        return list
    #Nếu là yêu cầu kiểm tra thì
    #kiểm tra Parent có phải là female không
    #kiểm tra Parent có phải bố/mẹ của child ko
    if female(Parent) and parent(Parent, Child):
        return True
    return False
#hàm kiểm tra Child có phải con trai của Parent hay không
#hoặc tìm con trai của Parent
def son(Child, Parent):
    #nếu là yêu cầu tìm son của Parent
    if Child == 'X' or Child == 'x':
        #tìm child của Parent
        temp = child(Child,Parent)
        if temp == False:
            return False
        list=[]
        count = 0
        #xét trong list child của Parent những người là male thì thêm vào kết quả trả về
        for key in temp:
            if male(key[0]):
                list.append(key)
                count += 1
        if count == 0:
            return False
        else:
            return list
    #nếu là yêu cầu kiểm tra thì
    #kiểm tra Child có phải là male không
    #kiểm tra child có phải con của Parent hay không
    if male(Child) and child(Child,Parent):
        return True
    return False
#hàm kiểm tra Child có phải con gái của Parent hay không
#hoặc tìm con gái của Parent
def daughter(Child, Parent):
    #nếu là yêu cầu tìm son của Parent
    if Child == 'X' or Child == 'x':
        #tìm child của Parent
        temp = child(Child,Parent)
        if temp == False:
            return False
        list=[]
        count = 0
        #xét trong list child của Parent những người là female thì thêm vào kết quả trả về
        for key in temp:
            if female(key[0]):
                list.append(key)
                count += 1
        if count == 0:
            return False
        else:
            return list
    #nếu là yêu cầu kiểm tra thì
    #kiểm tra Child có phải là female không
    #kiểm tra child có phải con của Parent hay không
    if female(Child) and child(Child,Parent):
        return True
    return False
#hàm kiểm tra GP có phải grandparent của GC hay không
#hoặc tìm grandparent của GC
def grandparent(GP, GC):
    #tìm parent của GC
    temp = parent('x', GC)
    #nếu GC không có cha mẹ thì trả về false
    if temp == 0:
        return False
    list = []
    #xét cha và mẹ của GC
    for key in temp:
        #tìm Parent của người đó
        temp1 = parent('x', key[0])
        #Nếu không tìm thấy parent của cha/mẹ GC
        if temp1 == 0:
            continue
        #nếu là yêu cầu tìm kiếm grandparent của GC
        if GP == 'X' or GP == 'x':
            count = 0
            #thêm những người trong list parent của cha/mẹ GC 
            for key in temp1:
                list.append((key[0], GC))
                count += 1
            if count == 0:
                continue
            else:
                return list
        #Nếu là yêu cầu kiểm tra thì kiểm tra trong list parent của cha/mẹ GC để trả về kết quả
        else:
            for key in temp1:
                if key[0] == GP:
                    return True
            return False

#hàm kiểm tra GM có phải grandmother của GC hay không
#hoặc tìm grandmother của GC
def grandmother(GM,GC):
    #tìm grandparent của GC
    temp = grandparent(GM,GC)
    #nếu không tìm thấy thì trả về false 
    if temp == False:
        return False
    #Nếu tìm thấy và yêu cầu ban đầu là yêu cầu kiểm tra thì xem thử GM có phải là female hay không
    if temp == True:
        if female(GM):
            return True
        else:
            return False
    #nếu là yêu cầu tìm grandmother của GC
    list=[]
    #Xét female trong list grandparent của GC để thêm vào list kết quả trả về
    for key in temp:
        if female(key[0]):
            list.append(key)
    return list
#hàm kiểm tra GF có phải grandfather của GC hay không
#hoặc tìm grandfather của GC
def grandfather(GF,GC):
    #tìm grandparent của GC
    temp = grandparent(GF,GC)
    #nếu không tìm thấy thì trả về false 
    if temp == False:
        return False
    #Nếu tìm thấy và yêu cầu ban đầu là yêu cầu kiểm tra thì xem thử GM có phải là male hay không
    if temp == True:
        if male(GF):
            return True
        else:
            return False
    #nếu là yêu cầu tìm grandmother của GC
    list = []
    #Xét male trong list grandparent của GC để thêm vào list kết quả trả về
    for key in temp:
        if male(key[0]):
            list.append(key)
    return list
#hàm kiểm tra GC có phải grandchild của GP hay không
#hoặc tìm grandchild của GP
def grandchild(GC, GP):
    #tìm child của GP
    temp = parent(GP,'x')
    #Nếu GP không có child thì trả về false
    if temp == 0:
        return False
    list = []
    for key in temp:
        #Tìm child của con GP
        temp1 = parent(key[1],'x')
        if temp1 == 0:
            continue
        #Nếu là yêu cầu tìm grandchild của GP
        if GC == 'X' or GC == 'x':
            count = 0
            #xét child của con GP để thêm vào list kết quả trả về
            for key in temp1:
                list.append((key[1],GP))
                count += 1
            if count == 0:
                continue
            else:
                return list
        #Nếu là yêu cầu kiểm tra
        else:
            #Duyệt trong list con của Child của GP để cho ra kết quả
            for key in temp1:
                if key[1] == GC:
                    return True
            return False
#hàm kiểm tra GC có phải grandson của GP hay không
#hoặc tìm grandson của GP
def grandson(GS,GC):
    #gọi hàm tìm grandchild
    temp = grandchild(GS,GC)
    if temp == False:
        return False
    if temp == True:
        #nếu là yêu cầu kiểm  tra thì xét xem thử GS có phải là male không
        if male(GS):
            return True
        else:
            return False
    #Nếu là yêu cầu tìm kiếm
    list = []
    count = 0
    #duyệt từng grandchild trong list để xét những ai là male thì thêm vào list kết quả trả về
    for key in temp:
        if male(key[0]):
            list.append(key)
            count += 1
    if count == 0:
        return False
    else:
        return list
#hàm kiểm tra GC có phải granddaughter của GP hay không
#hoặc tìm granddaughter của GP
def granddaughter(GD,GP):
    #gọi hàm tìm grandchild
    temp = grandchild(GD,GP)
    if temp == False:
        return False
    if temp == True:
        #nếu là yêu cầu kiểm  tra thì xét xem thử GD có phải là female không
        if female(GD):
            return True
        else:
            return False
    #Nếu là yêu cầu tìm kiếm
    list = []
    count = 0
    #duyệt từng grandchild trong list để xét những ai là female thì thêm vào list kết quả trả về
    for key in temp:
        if female(key[0]):
            list.append(key)
            count += 1
    if count == 0:
        return False
    else:
        return list
#hàm kiểm tra Person1 và Person2 có phải sibling hay không
#hoặc tìm sibling của người đã cho
def sibling(Person1,Person2):
    #tìm cha của Person2
    temp = father('x',Person2)
    #nếu Person2 không có cha thì trả về false
    if temp == False:
        return False
    #tìm con của cha của Person2
    temp1 = child('x',temp[0][0])
    list = []
    count = 0
    #tìm trong list của của cha của Person2
    #nếu người đó khác Person2 thì thêm vào list
    for key in temp1:
        if key[0] != Person2:
            list.append((key[0],Person2))
            count += 1
    if count == 0:
        return False
    #Nếu yêu cầu là tìm kiếm thì trả về list
    if Person1 == 'x' or Person2 == 'X':
        return list
    #nếu yêu cầu là kiểm tra
    else:
        #duyệt từng người trong list kiểm tra có ai là Person1 không
        for key in list:
            if Person1 == key[0]:
                return True
    return False
#hàm kiểm tra Person và SibLing có phải brother hay không
#hoặc tìm brother của  Sibling
def brother(Person,Sibling):
    #gọi hàm tim sibling của Sibling
    temp = sibling('x',Sibling)
    #nếu không tìm thấy thì trả về false
    if temp == False:
        return False
    list = []
    count = 0
    #Duyệt trong list sibling, xét những người là male thì thêm vào list kết quả
    for key in temp:
        if male(key[0]):
            list.append(key)
            count += 1
    if count == 0:
        return False
    else:
        #nếu là yêu cầu tìm kiếm thì trả về list kết quả
        if Person == 'X' or Person == 'x':
            return list
        #nếu là yêu cầu kiểm tra
        else:
            #duyện từng người trong list kết quả để kiểm tra có ai là Person không
            for key in list:
                if key[0] == Person:
                    return True
        return False
#hàm kiểm tra Person và SibLing có phải sister hay không
#hoặc tìm sister của  Sibling
def sister(Person,Sibling):
    #gọi hàm tim sibling của Sibling
    temp = sibling('x',Sibling)
    #nếu không tìm thấy thì trả về false
    if temp == False:
        return False
    list = []
    count = 0
    #Duyệt trong list sibling, xét những người là male thì thêm vào list kết quả
    for key in temp:
        if female(key[0]):
            list.append(key)
            count += 1
    if count == 0:
        return False
    else:
        #nếu là yêu cầu tìm kiếm thì trả về list kết quả
        if Person == 'X' or Person == 'x':
            return list
        #nếu là yêu cầu kiểm tra
        else:
            #duyện từng người trong list kết quả để kiểm tra có ai là Person không
            for key in list:
                if key[0] == Person:
                    return True
        return False
#hàm kiểm tra Person có phải là aunt của NieceNephew hay không
#hoặc tìm aunt của NieceNephew
def aunt(Person,NieceNephew):
    #tìm parent của NieceNephew
    temp = parent('x',NieceNephew)
    #nếu không tìm thấy thì trả về false
    if temp == False:
        return False
    list = []
    #duyệt từng người trong list parent của NiecNephew
    for key in temp:
        #tìm list chị gái của người đó
        temp1 = sister('x',key[0])
        if temp1 == False:
            continue
        count = 0
        #Thêm list chị gái của người đó vào list kết quả
        for key1 in temp1:
            list.append((key1[0],NieceNephew))
            count+= 1
        if count == 0:
            continue
    #nếu là yêu cầu tìm kiếm thì trả về list kết quả
    if Person == 'x' or Person == 'X':
        if len(list) == 0:
            return False
        else:
            return list
    #nếu là yêu cầu kiểm tra
    for key in list:
        #duyệt từng người trong list kết quả để kiểm tra có ai là Person không
        if Person == key[0]:
            return True
    return False
#hàm kiểm tra Person có phải là uncle của NieceNephew hay không
#hoặc tìm uncle của NieceNephew
def uncle(Person,NieceNephew):
    #tìm parent của NieceNephew
    temp = parent('x',NieceNephew)
    #nếu không tìm thấy thì trả về false
    if temp == False:
        return False
    list = []
    #duyệt từng người trong list parent của NiecNephew
    for key in temp:
        #tìm list anh trai của người đó
        temp1 = brother('x',key[0])
        if temp1 == False:
            continue
        count = 0
        #Thêm list anh trai của người đó vào list kết quả
        for key1 in temp1:
            list.append((key1[0],NieceNephew))
            count+= 1
        if count == 0:
            continue
    #nếu là yêu cầu tìm kiếm thì trả về list kết quả
    if Person == 'x' or Person == 'X':
        if len(list) == 0:
            return False
        else:
            return list
    #nếu là yêu cầu kiểm tra
    for key in list:
        #duyệt từng người trong list kết quả để kiểm tra có ai là Person không
        if Person == key[0]:
            return True
    return False
#hàm kiểm tra Person có phải là niece của AuntUncle hay không
#hoặc tìm niece của AuntUncle
def niece(Person,AuntUncle):
    #gọi hàm sibling để tìm sibling của AuntUncle
    temp = sibling('x', AuntUncle)
    #nếu không tìm thấy thì trả về false
    if temp == False:
        return False
    list = []
    count = 0
    #duyệt từng người trong list anh chị em của AuntUncle
    for key in temp:
        #tìm con gái của người đó
        temp1 = daughter('x',key[0])
        if temp1 == False:
            continue
        #thêm con gái của người đó vào list kết quả
        for key1 in temp1:
            list.append((key1[0],AuntUncle))
            count += 1
    #nếu là yêu cầu tìm kiếm thì trả về list kết quả
    if Person == 'x' or Person == 'X':
        if len(list) == 0:
            return False
        else:
            return list
    #nếu là yêu càu kiểm tra
    #duyệt từng người trong list kết quả để kiểm tra
    for key in list:
        if Person == key[0]:
            return True
    return False
#hàm kiểm tra Person có phải là niece của AuntUncle hay không
#hoặc tìm nephew của AuntUncle
def nephew(Person,AuntUncle):
    #gọi hàm sibling để tìm sibling của AuntUncle
    temp = sibling('x', AuntUncle)
    #nếu không tìm thấy thì trả về false
    if temp == False:
        return False
    list = []
    count = 0
    #duyệt từng người trong list anh chị em của AuntUncle
    for key in temp:
        #tìm con trai của người đó
        temp1 = son('x',key[0])
        if temp1 == False:
            continue
        #thêm con gái của người đó vào list kết quả
        for key1 in temp1:
            list.append((key1[0],AuntUncle))
            count += 1
    #nếu là yêu cầu tìm kiếm thì trả về list kết quả
    if Person == 'x' or Person == 'X':
        if len(list) == 0:
            return False
        else:
            return list
    #nếu là yêu càu kiểm tra
    #duyệt từng người trong list kết quả để kiểm tra
    for key in list:
        if Person == key[0]:
            return True
    return False
#Bộ câu hỏi test
fopen = open('20-Questions.txt', 'r')
any_questions = fopen.readlines()
fopen.close()
any_questions[len(any_questions)-1] += '\n'
#ghi kết quả xuống file
def writeFile(answer, fwrite):
    if answer == False:
            fwrite.write(f'\tfalse.\n')
    else:
        if answer == True:
            fwrite.write(f'\ttrue.\n')
        else:
            for key in answer:
                fwrite.write(f'\tX = {key[0]}\n')

fw = open("Answer3_1.txt", "w")
#Xử lý đọc bộ câu hỏi test
def handleFile(questions, fwrite):
    count = 1
    for key in questions:
        start=key.rfind('(') + 1
        dau = key.rfind(',')
        end = key.rfind(')')
        if key[3:start-1] == "grandparent":
            answer = grandparent(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "child":
            answer = child(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "grandmother":
            answer = grandmother(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "husband":
            answer = husband(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "wife":
            answer = wife(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "father":
            answer = father(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "mother":
            answer = mother(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "son":
            answer = son(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "daughter":
            answer = daughter(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "grandparent":
            answer = grandparent(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "grandfather":
            answer = grandfather(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "grandson":
            answer = grandson(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "granddaughter":
            answer = granddaughter(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "sibling":
            answer = sibling(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "brother":
            answer = brother(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "sister":
            answer = sister(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "aunt":
            answer = aunt(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "niece":
            answer = niece(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "uncle":
            answer = uncle(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "nephew":
            answer = nephew(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "married":
            answer = married(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "divorced":
            answer = divorced(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer,fwrite)
        elif key[3:start-1] == "parent":
            answer = parent(key[start:dau],key[dau+1:end])
            fwrite.write(f'{count}. {key}')
            count += 1
            writeFile(answer, fwrite)
    fwrite.close()
handleFile(any_questions,fw)