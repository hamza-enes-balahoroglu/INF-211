# ================================================================
# INF211 Project 1: 4-Band Resistor Decoder
# Student Name: Hamza Enes Balahoroğlu
# Student ID  : 240102002088
# ================================================================


def is_upper_letter(ch):
    """Check if a character is uppercase.

    Args:
        ch (string): A single character.

    Returns:
        bool: True if the character is uppercase, otherwise False.
    """
    
    # letters we consider as upper case
    upper_letters = (
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z"
    )
    
    # check if ch is in upper_letters and return True or False
    return ch in upper_letters

def parse_four_bands(line):
    """Convert a string with 4 bands into a list of bands.

    Args:
        line (string): Input text that includes 
        4 bands separated by '-'.

    Returns:
        list: A list with 4 bands.
    """
    
    # this is the symbol that splits the line
    SEPARATOR = '-'  
    
    # list to keep 4 bands
    bands_list      = ['','','','']
    
    # keep track of which band we fill
    bands_index     = 0  
    
    # string for current band
    band            = ""  

    for i in range(0,len(line)):
        if bands_index == 3:
            bands_list[3] = line[i:]  # last band takes the rest
            break

        elif line[i] == SEPARATOR:
            bands_list[bands_index] = band  # save current band
            bands_index += 1  # go to next band
            band = ""  # reset current band
            continue

        else:
            band += line[i]  # add character to current band
            
    return bands_list  # return all 4 band

def color_to_value(color):
    """Convert a color band to its numeric value.
    
    Args:
        color (string): Band color (must be uppercase).

    Returns:
        int: Value of the color (0-9). Returns -1 if color is not valid.
    """
    color_map = (
    "BLACK",    # 0
    "BROWN",    # 1
    "RED",      # 2
    "ORANGE",   # 3
    "YELLOW",   # 4
    "GREEN",    # 5
    "BLUE",     # 6
    "VIOLET",   # 7
    "GREY",     # 8
    "WHITE"     # 9
    )
    
    if not (color in color_map): # Invalid color input
        return -1 
    
    for i in range(0, len(color_map)):
        if color == color_map[i]:
            return i # return index as value
    pass

def color_to_multiplier_and_tolerance(mult_color, tol_color):
    """Convert color bands to multiplier and tolerance values.

    Args:
        mult_color (string): Color of the 
        3rd band (multiplier).
        tol_color (string): Color of the 
        4th band (tolerance).

    Returns:
        tuple: (exp, tol) where exp is the power 
        of 10, and tol is tolerance in percent.
    """
    
    # colors for multiplier (3rd band)
    multiplier_colors = (
        ("GOLD",   -1),
        ("SILVER", -2),
        ("BLACK",   0),
        ("BROWN",   1),
        ("RED",     2),
        ("ORANGE",  3),
        ("YELLOW",  4),
        ("GREEN",   5),
        ("BLUE",    6),
        ("VIOLET",  7),
        ("GREY",    8),
        ("WHITE",   9)
    )
    
    # find exponent value from 3rd band
    exp = 0
    
    for col_val in multiplier_colors:
        if col_val[0] == mult_color:
            exp = col_val[1]
            break
    
    # find tolerance value from 4th band
    tolerance_colors = (
        ("GOLD",    5),
        ("SILVER",  10),
        ("BROWN",   1),
        ("RED",     2),
        ("ORANGE",  3),
        ("YELLOW",  4),
        ("GREEN",   0.5),
        ("BLUE",    0.25),
        ("VIOLET",  0.1),
        ("GREY",    0.05)
    )
    
    # find tolerance value from 4th band
    tol = 0
    
    for col_val in tolerance_colors:
        if col_val[0] == tol_color:
            tol = col_val[1]
            break
    
    # return both values as a tuple
    return (exp, tol)

def compute_resistor_value(d1, d2, exp, tol):
    """Compute resistor value and its tolerance range.

    Args:
        d1 (int): First band value.
        d2 (int): Second band value.
        exp (int): Power of 10 from the 3rd band.
        tol (float): Tolerance percent from the 4th band.

    Returns:
        tuple: (resistor, r_min, r_max)
    """
    # calculate main resistor value
    resistor = ((d1 * 10) + d2) * (10 ** exp)
    
    # calculate minimum value with tolerance
    r_min = resistor - resistor * tol / 100
    
    # calculate maximum value with tolerance
    r_max = resistor + resistor * tol / 100
    
    # return all values
    return (resistor, r_min, r_max)

def main():
    """main 
    
    Reads user input, parses color bands, and
    calculates the resistor value with its
    tolerance range.
    
    Args:
        None

    Returns:
        None
    """
    
    # all valid color names 
    colors = (
    "GOLD",     # -2 
    "SILVER",   # -1 
    "BLACK",    # 0
    "BROWN",    # 1
    "RED",      # 2
    "ORANGE",   # 3
    "YELLOW",   # 4
    "GREEN",    # 5
    "BLUE",     # 6
    "VIOLET",   # 7
    "GREY",     # 8
    "WHITE"     # 9
    )
    
    # get user input
    raw_input = input("Input : ")
    
    # count number of '-' symbols
    count_hyphen = 0
    for i in raw_input:
        if i == '-':
            count_hyphen += 1
    
    # check basic format: must have 3 '-' and not end with '-'
    if not (count_hyphen == 3) or (raw_input[-1] == "-"):
        print("Invalid format or missing colors!")
        return
    
    # split input into 4 bands
    parsed = parse_four_bands(raw_input)
    
    # check if all letters are uppercase
    for i in parsed:
        for j in i:
            if is_upper_letter(j) != True:
                print("Invalid input! Please use uppercase letters (A–Z). ")
                return
    
    # black cannot be first or last band
    if parsed[0] == "BLACK" or parsed[3] == "BLACK":
        print("Invalid color code!")
        return

    # check if all bands are valid colors
    for i in parsed:
        if not i in colors:
            print("Invalid color code!")
            return


    # if wrong direction, reverse the order
    if  parsed[0] in ("GOLD", "SILVER") or \
        parsed[1] in ("GOLD", "SILVER") or \
        parsed[3] in ("WHITE"):
        parsed = parsed[::-1]
        
        # second check after reversing to avoid invalid order
        if  parsed[0] in ("GOLD", "SILVER") or \
            parsed[1] in ("GOLD", "SILVER") or \
            parsed[3] in ("WHITE"):
            print("Invalid color code!")
            return
        
        print("WRONG ORDER, TURN THE RESISTOR AROUND")
    
    # convert first two bands to digits
    d1 = color_to_value(parsed[0])
    d2 = color_to_value(parsed[1])
    
    # get multiplier and tolerance
    exp_tol = color_to_multiplier_and_tolerance(parsed[2], parsed[3])
    exp = exp_tol[0]
    tol = exp_tol[1]
    
    # compute resistor value
    resistor_values = compute_resistor_value(d1, d2, exp, tol)
    resistor = resistor_values[0]
    r_min    = resistor_values[1]
    r_max    = resistor_values[2]
    
    # print all results
    print(f"Value: {resistor:.2f} Ω")
    print(f"Tolerance: ±{tol:.2f}%")
    print(f"Min: {r_min:.2f} Ω")
    print(f"Max: {r_max:.2f} Ω")
    pass


if __name__ == "__main__":
    main()
