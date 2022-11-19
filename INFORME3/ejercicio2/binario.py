

def convertirADecimal(n: str):
    
    b=str(int(n,2))
    return b


def convertirAOctal(n:str):
    a=int(convertirADecimal(n))
    b=str(oct(a))
    return b[2:]


def convertirAHexadecimal(n: str):
    a=int(convertirADecimal(n))
    b=str(hex(a))
    
    return b[2:]

if __name__ == "__main__":
    conversionDecimal= convertirADecimal(n)
    conversionOctal= convertirAOctal(n)
    conversionHexadecimal = convertirAHexadecimal(n)
