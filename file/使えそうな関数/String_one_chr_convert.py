# 文字列の一文字を変更する関数
def str_assignment(s: str, idx: int, convert: str):
    
    # String Variable
    string = s
    
    # Creating list of String elements
    lst = list(string)
    
    # Assigning value to the list
    lst[idx] = convert
    
    # use join function to convert list into string
    new_String = "".join(lst)
    
    return new_String