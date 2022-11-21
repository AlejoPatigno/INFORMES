
def convertirADecimal(n: str):
    
    b=str(int(n,8))
    return b


def convertirABinario(n:str):
    a=int(convertirADecimal(n))
    b=str(bin(a))
    return b[2:]


def convertirAHexadecimal(n: str):
    a=int(convertirADecimal(n))
    b=str(hex(a))
    
    return b[2:]

if __name__ == "__main__":
    n="5"
    conversionDecimal= convertirADecimal(n)
    conversionBinaria= convertirABinario(n)
    conversionHexadecimal = convertirAHexadecimal(n)