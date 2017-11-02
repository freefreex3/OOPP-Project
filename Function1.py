def is_valid_nric(s):

    if len(s)==9 and ((s)[0]=="t" or (s)[0]=="s") and (s)[-1].isalpha() and (s)[1:-1].isdigit():
     valid = True
    else:
        valid = False

    return valid



print(is_valid_nric('t2323213t'))
print(is_valid_nric('s12323232'))
print(is_valid_nric('s'))

