def getHuruf(word):
    result = []

    for element in word:
        if element.isalpha():
            result.append(element)
    
    return result

def getKalimat(word, p):
    result = []

    for item in word:
        if item == p[0] or item == p[1] or item == p[2]:
            index = word.find(item)
            data = word[:index+1]
            result.append(data)
    
    return result
    
def getTandaBaca(word, tandaBaca):
    result = []

    for element in word:
        if element == tandaBaca:
            result.append(element)
    
    return result