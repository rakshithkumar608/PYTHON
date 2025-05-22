sheep_count = 1
while sheep_count <= 10:
    print(f"sheep{sheep_count}")
    sheep_count += 1


# i = 1
# while i <= 5:
#     print(i)


is_failed = True
i = 1 #attempt

while is_failed:
    if i%2!=0: # is not even
        i += 1
        continue
    print(f"Try {i}")
    i += 1
    if i>=100:
        break

print("I gave up")

# i = 0

# while i<=10:
#     x = 0
#     while x<i:
#         print("Rakshith")
#         x +=1
#         i +=1