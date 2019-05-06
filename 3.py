def func1(num):
    sum = 0
    for i in range(num):
        sum += i
        print i
    return sum


#print func1(1234)


def func2(num, num2):
    counter = 0
    for i in range(num, num2):
        print i
        counter += 1
    return counter


#func2(12,43)


def func3(machrozet):
    return machrozet[1:len(machrozet) - 1]


#print func3("temble")


def func4(s):
    return s[::-1]


#print  func4("ting")


def func5(dat):
    return dat[::-1]


def func6(st):
    if(st.isdigit() or st.islower() or st.isupper()):
        return True
    return False
#print func6("idk")


def func7(dat1,dat2):
    if len(dat1)==len(dat2):
        return True
    return False
#print func7([1,2,3,4],[1,2,3,4])


def func8(strin):
    if strin[len(strin)-2::] == "il":
        return True
    return False
print func8("www.google.co.il")
