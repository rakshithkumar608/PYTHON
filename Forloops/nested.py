for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()  # To print an empty line after each table

## multiplication of 2
for i in range(1, 11):
    print(f"2X{i}={2*i}")    


## multiplication of 2 to 10
for i in range(2, 11):
    for j in range(1, 11):
        print(f"{i}X{j}={i*j}", end=" ")
        print()