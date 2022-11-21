
def convertirABinario(n: str):
    n=int(n)
    b=str(bin(n))
    return b[2:]


def convertirAOctal(n:str):
    n=int(n)
    b=str(oct(n))
    return b[2:]


def convertirAHexadecimal(n: str):
    n=int(n)
    b=str(hex(n))
    
    return b[2:]

if __name__ == "__main__":
    conversionBinaria= convertirABinario(n)
    conversionOctal= convertirAOctal(n)
    conversionHexadecimal = convertirAHexadecimal(n)