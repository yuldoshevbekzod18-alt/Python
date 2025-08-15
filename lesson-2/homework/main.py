#Write a Python program to ask for a user's name and year of birth, then calculate and display their age.
name=input('ismingizni kiriting:')
year=int(input('yilingizni kiriting:'))
age=2025-year
print(f'{name} sizning yoshingiz {age}')

#Extract car names from the following text:
txt = 'LMaasleitbtui'
print(txt[::2])
print(txt[1::2])


#Extract car names from the following text:
txt = 'MsaatmiazD'
print(txt[::2])


#Extract the residence area from the following text:
txt = "I'am John. I am from London"
residence=txt.split('from')[-1]
print(residence)

#Write a Python program that takes a user input string and prints it in reverse order.
user=input('ozgaruvchini kiriting:')
print(user[::-1])


#Write a Python program that counts the number of vowels in a given string.
word = input("Soz kiriting: ").lower()
vowels = "aeiou"
count = sum(1 for letter in word if letter in vowels)

print(f"Unli harflar soni: {count}")

#Write a Python program that takes a list of numbers as input and prints the maximum value.
royhat=list(map(float,input("Sonlarni vergul bilan kiriting:").split(',')))
royhat_max=max(royhat)
print(royhat_max)


#Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
word=input("soz kiriting:")
if word==word[::-1]:
    print('palindrom')
else:
    print('palindrom emas')


#Write a Python program that extracts and prints the domain from an email address provided by the user.
email=input('emailni kiriting:')
if "@" in email:
    domain = email.split("@")[1]
    print(f"Domen: {domain}")
else:
    print("Bu email manzilida '@' belgisi yo'q.")
