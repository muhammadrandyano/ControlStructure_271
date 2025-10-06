def number_pattern():
    n = int(input("Masukkan nilai n: "))
    
    print("Pola angka:")
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()  

number_pattern()