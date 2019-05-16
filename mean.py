def mean(num_list):
    try:
        if any(el.imag!=0 for el in num_list):
            return NotImplemented
    except AttributeError as detail:
        msg = "The algebraic mean of an non-numerical list is undefined.\
               Please provide a list of numbers."
        raise TypeError(detail.__str__() + "\n" +  msg)
        
    try:
        return sum(num_list)/len(num_list)
    except ZeroDivisionError :
        return 0

        
    
