with open('numbers.txt', 'w') as f:
    for i in range(1, 101):
        print(f"{i},{i**2},{i**3}")
        f.write(f"{i},{i**2},{i**3}\n")