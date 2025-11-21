#Quiz 2
def weighted_sum(x, w):
    sum1 = 0
    sum2 = 0
    for i in range(len(x)):
        sum1 += x[i] * w[i]
        sum2 += w[i]
        pass
    avarage = sum1 / sum2
    
    mapping = (
        ("Minella", 1, 2 ),
        ("Zokito", 2, 3),
        ("Lidia", 3, 4),
        ("Suedae", 4, 5),
        ("Hilo", 5, 10),        
    )
    mapped = ""
    for text, minimum, maximum in mapping:
        if minimum <= avarage < maximum:
            mapped = text
            break
        pass
    else:
        mapped = "Esenia"
        pass
    
    return [avarage , mapped]

print(weighted_sum([4, 5, 5],[1, 2 , 2]))
    