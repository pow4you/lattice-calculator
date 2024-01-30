def find_integer(numerator,denominator,modulo):
    for i in range(0,10**100):
        result = ((numerator+modulo*i)/denominator) % modulo
        if result % 1 == 0:
            return result
    return "Not found"

if __name__ == "__main__":
    print("Modular Arithmetic Inverse Division Script")
    while True:
        print("------------------------------------------------")
        print(f"Input:")
        numerator = int(input(f"  Numerator: "))
        denominator = int(input(f"  Denominator: "))
        modulo = int(input(f"  Modulo: "))
        print("------------------------------------------------")
        
        result = find_integer(numerator,denominator,modulo)
        
        print(f"Result: {result}")
    