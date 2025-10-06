def odd_numbers():
    n = int(input("Masukkan nilai n: "))
    
    print(f"Bilangan ganjil sampai {n}:")
    
    for i in range(1, n + 1):
        if i % 2 != 0:  
            print(i, end=" ")
    print()

def odd_numbers_simple():
    n = int(input("Masukkan nilai n: "))
    
    print(f"Bilangan ganjil sampai {n}:")
    for i in range(1, n + 1, 2):
        print(i, end=" ")
    print()

odd_numbers()