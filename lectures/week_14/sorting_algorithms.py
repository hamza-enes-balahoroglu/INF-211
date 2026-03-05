def replace_at(text: str, new_char: str, index: int  = 0) -> str:
    temp_list = list(text)  # ['1', '1', '1', '1'] olur

    temp_list[index] = new_char      # ['1', '1', '0', '1'] olur

    text = "".join(temp_list) # Tekrar string yap: "1101"
    return text

def xor_by_index(upper_str: str, upper_index: int, lower_str: str, lower_index: int) -> str:

    new_char = ""
    if upper_str[upper_index] == lower_str[lower_index]:
        new_char = "0"
    else:
        new_char = "1"

    return replace_at(lower_str, new_char, lower_index)

def sliding_xor_process(binary_str: str) -> list[str]:
    # Gelen string ifadeyi (ör: "1001") tam sayıya çevir
    length = len(binary_str)
    original_num = int(binary_str, 2)

    # Sayının tersini al (NOT işlemi)
    # Python'da sonsuz bit olduğu için maskeleme yaparak sadece istediğimiz bit uzunluğunu alıyoruz.
    mask = (1 << length) - 1
    inverse_num = (~original_num) & mask
    inverse_binary = bin(inverse_num)[2:].zfill(length)

    print(f"Sayı:  {binary_str}")
    print(f"Tersi: {inverse_binary}")
    print("-" * 15)
    
    # Sonuçları saklayacağımız hafıza (liste)
    memory = []

    inverse_binary, binary_str = binary_str, inverse_binary
    
    for step in range(1, length + 1):

        for lower_index in range(0, step):
            upper_index = (length - step) + lower_index
            inverse_binary = xor_by_index(binary_str, upper_index, inverse_binary, lower_index)
            # print("upper : ", upper_index, "lower  : ", lower_index)
            
        memory.append(inverse_binary)
        dashes = "-" * (length - step)
        print(f"{dashes}{inverse_binary[:step]}")

    return memory

def binary_formating(numbers: list[str]) -> list[str]:
    restult = list()
    
    for i in range(0, len(numbers)):
        
        formated_binary = ""
        for j in range(0, len(numbers)):
            formated_binary += numbers[j][i]
        
        formated_binary = replace_at(formated_binary, "1", -1)
        restult.append(formated_binary)
    return restult

def xor_with_formating(binary_str: str) -> list[str]:
    # Gelen string ifadeyi (ör: "1001") tam sayıya çevir
    length = len(binary_str)
    original_num = int(binary_str, 2)

    # Sayının tersini al (NOT işlemi)
    # Python'da sonsuz bit olduğu için maskeleme yaparak sadece istediğimiz bit uzunluğunu alıyoruz.
    mask = (1 << length) - 1
    inverse_num = (~original_num) & mask
    inverse_binary = bin(inverse_num)[2:].zfill(length)

    print(f"Sayı:  {binary_str}")
    print(f"Tersi: {inverse_binary}")
    print("-" * 15)
    
    results = list()
    
    for i in range(len(inverse_binary)):
        new_item = ""
        for o in range(len((binary_str))):
            new_char = ""
            if binary_str[o] == inverse_binary[i]:
                new_char = "0"
            else:
                new_char = "1"
            inverse_binary =  replace_at(inverse_binary, new_char, i)
            new_item += new_char
            
        results.append(new_item)
    
    return results

# --- KULLANIM ---

a = 571
b = 331

number = (a * b)

giris_sayisi = format(number, "b")
sonuclar = sliding_xor_process(giris_sayisi)
formated = binary_formating(sonuclar)

# sonuclar = xor_with_formating(giris_sayisi)

print("A sayısı : ",format(a, "b"))
print("B sayısı : ",format(b, "b"))

print("\n--- Hafızadaki Veriler (Decimal & Binary) ---")
for i, val in enumerate(formated):
    print(f"Adım {i+1}: {int(val, 2)} (Binary: {val.zfill(len(giris_sayisi))})")