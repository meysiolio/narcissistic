def narcissistic( value ):
    # Code away
    number_of_digits = len(str(value))
    total = 0
    
    for i in range(number_of_digits):
        total += int(str(value)[i]) ** number_of_digits
        
    if total == value:
        return True
    else:
        return False
