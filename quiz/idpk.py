import string
# create the algorithm to rank objects
letter = ['5','6','7','d','e','f','g','h','i','o','p','q','r','s','t','u','8','9','a','b','c','v','w','k','l','m','n','U','T','3','4','S','R','Q','P','O','N','M','L','K','J','I','H','G','F','E','D','x','y','z','Z','Y','B','A','0','1','2','X','W','V','j','C']
#create a function that will convert the django id to a string of character
def getDigit(id : int):
    digit = []
    while id > 0:
        rem = id % len(letter)
        digit.append(rem)
        id //= len(letter) 

    return digit


product = 1
summation = 0
def convert(id : int):
    new_id = ''
    global product
    global summation
    for element in getDigit(id):
        new_id += letter[element]
        product *= element
        summation += element
    return new_id

def productConvert(id : int):
    new_id = ''
    for element in getDigit(id):
        new_id += letter[element]
    return new_id

def summationConvert(id : int):
    new_id = ''
    for element in getDigit(id):
        new_id += letter[element]
    return new_id

def finalConvert(id : int):
    return convert(id) + productConvert(product) + summationConvert(summation)


print(finalConvert(23))