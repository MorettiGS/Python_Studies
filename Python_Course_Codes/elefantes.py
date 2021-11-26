def incomodam(n):
    if n < 1:
        return ""
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    if n < 1:
        return ""
    else:
        if n == 1:
            return "Um elefante incomoda muita gente\n"
        if n == 2:
            return elefantes(n-1) + str(n) + " elefantes " + incomodam(n) + "muito mais\n"
        if n > 2:
            return elefantes(n-1) + str(n-1)+ " elefantes incomodam muita gente\n" + str(n) + " elefantes " + incomodam(n) + "muito mais\n"