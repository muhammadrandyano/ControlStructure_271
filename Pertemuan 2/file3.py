def fibonacci_series():
    n = int(input("Masukkan nilai n: "))
    
    a, b = 0, 1
    count = 0
    
    print(f"Deret Fibonacci sampai {n} terms:")
    
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()  

fibonacci_series()