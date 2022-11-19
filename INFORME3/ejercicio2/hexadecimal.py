

def convertirADecimal(n: str):
    
    b=str(int(n,16))
    return b


def convertirAOctal(n:str):
    a=int(convertirADecimal(n))
    b=str(oct(a))
    return b[2:]


def convertirABinario(n: str):
    a=int(convertirADecimal(n))
    b=str(bin(a))
    
    return b[2:]

if __name__ == "__main__":
    conversionDecimal= convertirADecimal(n)
    conversionOctal= convertirAOctal(n)
    conversionBinaria = convertirABinario(n)
