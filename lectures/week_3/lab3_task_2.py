"""
Task 2 :  Write a function named “functionT2”  that will find and return the number with 
the given row (i-th) and column (j-th) index using the following rules. 

• i, and j show the row and column indexes respectively.  
• f(i, j) function is given as: f(i,j) = f(i−1, j−1) + f(i−1, j)  
• f(i=1, j=1) = 1  
• f(i, j=1) = 3 for i > 1  
• f(i, j=i) = 2 for i > 1  
• j <= i  

"""

def column_2(row):
    """column_2

    Args:
        row (int): Row valule where column is 2

    Returns:
        int : cell value
    """
    return (row - 2 - 1) * 3 + 2

def functionT2(row, column):
    
    ####################################
    # Verilen verilerin istenilen 
    # aralıkta olup olmadigini kontrol ettik
    ####################################
    
    if  not (0 < row    < 100) or \
        not (0 < column < 100) and \
        not (row >= column):
        return 0
    
    if row == 1 and column == 1:
        return 1
    
    if row > 1  and column == 1:
        return 3
    
    if row == column and row > 1:
        return 2 
    
    ####################################
    
    # Bir önceki kolonu hafızada saklamak için alan.
    previous_col = [] 
    
    for j in range(2, column + 1):
        col = []
        val = 2
        for i in range(j+1, row + 1):
            
            if j == 2:   # ilk kolondaysak
                val = 3 + val
            else:                
                val =  previous_col[i-(j+1)] + val

            col.append(val)     
            print(col)
                       
            if i == row and j == column:
                return val        
        pass
        previous_col = col
    pass



row     = int(input("Row".ljust(10, " ")    + ": "))

column  = int(input("Column".ljust(10, " ") + ": "))

print(functionT2(row, column))