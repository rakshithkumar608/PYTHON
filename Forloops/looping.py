name = "Rakshith"
for index,  letter in  enumerate(name):
    print(letter*(index+1))


l = [12, 39, 45, 78]
for index, num in enumerate(l):
    print(f"{num} is in {index}th index")  


d = {"name": "Rakshith", "age": 19, "city": "Bengaluru"}    
for key, value in d.items():
    print(key, " ", value)