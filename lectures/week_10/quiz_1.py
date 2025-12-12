def quiz1(liste: list, value: int, boolen: bool = False):
    result = []
    for i in liste:
        if list(liste).count(i) >= value and not i in result:
            result.append(i)
    result.sort()
    if boolen == True:
        return (result  , round((len(list(liste)) - len(result)) / len(liste) * 100 , 3))
    return result


a = [1,5,5,5,5,5,5,2,1,1,1,2,3,4,4,4]
print(quiz1(a, 2, True))