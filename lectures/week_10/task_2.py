def task2(text: str) -> list:
    items = str(text).lower()
    result = []
    print(items)
    for i in items:
        item = i
        result.append(item)
        
        for j in items:
            item += j
            result.append(item)
        pass
    
    return result

print(task2("AB"))
    