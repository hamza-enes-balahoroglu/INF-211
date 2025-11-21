# Quiz_1
def common_count(list1, list2):
    
    common = ""
    
    for i in list1:
        if i in list2 and not str(i) in common.split(","):
            common += str(i)
            common += ","
            pass
    
    return common.split(",")[:-1]

liste_1 = [1, 3, 2, 10, 10]
liste_2 = [1, 2, 3, 2, 10]

commons = common_count(liste_1, liste_2)

print(commons)
print(len(commons))