def maximum_number(*numbers):
    largest = float('-inf')
    
    for number in numbers:
        if(number > largest):
            largest = number
            
    return largest