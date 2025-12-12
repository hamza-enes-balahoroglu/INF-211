def compress(s: str) -> tuple[str, int]:
    if not s:
        return "", 0

    compressed_string = ""
    original_length = len(s)
    i = 0 
    
    for i in range(original_length):
        if i > 0 and s[i] == s[i-1]:
            continue

        current_char = s[i]
        count = 0
        j = i 
        
        while j < original_length and s[j] == current_char:
            count += 1
            j += 1

        compressed_string += current_char
        
        if count > 1:
            compressed_string += str(count)


    compressed_length = len(compressed_string)
    saved_space = original_length - compressed_length
    

    if original_length > 0:
        compression_rate_percent = (saved_space / original_length) * 100
        compression_rate_rounded = int(round(compression_rate_percent))
    else:
        compression_rate_rounded = 0
    
    return compressed_string, compression_rate_rounded

print(compress("aaaabbbbbbbbbccdddddddeeeeeeeeeeeeeeeefffhkkklli"))