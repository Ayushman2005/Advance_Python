#QUES-1
text = input("Enter a string: ")
print("Reversed string:", text[::-1])

#QUES-2
text = input("Enter a string: ")
upper = 0
lower = 0
for char in text:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print(f"Uppercase: {upper}, Lowercase: {lower}")

#QUES-3
text = input("Enter a string: ")
if text.isdigit():
    print("Contains only digits.")
else:
    print("Does not contain only digits.")

#QUES-4
text = input("Enter a string: ")
print("Result:", text.replace(" ", "_"))

#QUES-5
text = input("Enter a string: ")
counts = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1
print("Frequency:", counts)

#QUES-6
text = input("Enter a string: ")
if text:
    first = text[0]
    last = text[-1]
    print(f"First '{first}': {text.count(first)} times")
    print(f"Last '{last}': {text.count(last)} times")
else:
    print("String is empty.")

#QUES-7
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
result = ""
for char in text:
    if char not in vowels:
        result += char
print("No vowels:", result)

#QUES-8
s1 = input("First string: ")
s2 = input("Second string: ")
if sorted(s1) == sorted(s2):
    print("They are anagrams.")
else:
    print("They are not anagrams.")

#QUES-9
text = input("Enter a string: ")
print("Capitalized:", text.title())

#QUES-10
text = input("Enter a string: ")
clean_text = text.replace(" ", "").lower()
if clean_text == clean_text[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")