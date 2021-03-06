def check_string(str1):
    """
        Checka string against the 
        following criteria:
        * type(str1)==str
        * len(str1) is odd
        * len(str1) >= 7

        Parameters
        ----------
        str1: str    
    """
    if type(str1) != str:
        raise ValueError(f'The input {str1} is not type of {str1}!')
    elif len(str1) % 2 == 0:
        raise ValueError(f'The input {str1} is not odd !')
    elif len(str1) < 7:
        raise ValueError(f'The number is not >=7 !')
    else:
        pass
def string_middle(str1):
    """
    Extract the middle characters of
    a string

        Parametrs
        ---------
        str1: str

        Return 
        ------
        y: str
    """ 
    check_string(str1)
    beg= (len(str1)//2)-1
    end= (len(str1)//2)+2
    newstr=str1[beg:end]
    return newstr
str1 = "JhonDipPeta"
str2 = "JaSonAy"
print(string_middle(str1))
print(string_middle(str2))                                                                                                                                                                      

