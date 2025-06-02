# 1.Multiples of 3:

# Write a for loop that prints all multiples of 3 between 1 and 30.

for i in range(1, 11):
    print(f"3X{i}={3*i}")

#2.Sum of First 10 Numbers:

# Write a program using a for loop that calculates the sum of numbers from 1 to 10.  
sum_of_numbers = 0
for i in range(1, 11):
    sum_of_numbers += i  
print(f"The sum of numbers from 1 to 10 is: {sum_of_numbers}")


#3. Print Your Name Letter by Letter:

# Write a program that takes your name as input and prints each letter of your name using a for loop.

name = "Rakshith"
for letter in name:
    print(letter)

# 4. Count Vowels in a String:

# Write a program that counts how many vowels are in a given string using a for loop.   

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)