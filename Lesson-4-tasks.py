# Lesson 4 home tasks
# Task №1
"""პროგრამამ უნდა მოგვთხოვოს სახელის შეყვანა,
არასწორი სახელის შეყვანის შემთხვევაში,
უნდა დაწეროს "არ გიცნობთ" და ისევ უნდა
მოგვთხოვოს სახელის შეყვანა,სწორი სახელის
შეყვანის შემთხვევეში უნდა დაწეროს "გიცნობთ"
და დაასრულოს მუშაობა. """
name = input("Write your name: ")
while True:
    if name == "Giorgi":
        print("I know you")
        break
    elif name == "q":
        print("bye")
        break
    else:
        name = input("I don't know you, try again or write 'q' to exit the program: ")
print("------------------------------------")

# Task №2
"""პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა.
დაბეჭდოს შეყვანილი სტრიქონის ყველა
კენტი ინდექსის მქონე სიმბოლო."""
text = input("Write some text: ")
print(text)
odds = ""
for i in range(len(text)):
    if i % 2 != 0:
        odds += text[i]
    else:
        odds += " "
print(odds)
print("------------------------------------")

# Task №3
"""პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა.
დაბეჭდოს შეყვანილი სტრიქონის ყველა ლუწი
ინდექსის მქონე სიმბოლო, გარდა "e"- სიმბოლოსი."""
txt = input("Write some text: ")
print(txt)
even = ""
for i in range(len(txt)):
    if i % 2 == 0:
        if txt[i] != "e":
            even += txt[i]
    else:
        even += " "
print(even)
print("------------------------------------")

# Task №4
"""პროგრამამ უნდა შეგვაყვანინოს სიტყვა და
დაბეჭდოს ამ სიტყვიდან მხოლოდ თანხმოვანი ასოები.
"""
txt4 = input("Write text and I'll print it without vowels: ")
vowels = "aeiouyAEIOUY"
print("Vowels -", vowels)
print(f"Entered text:\n -->{txt4}")
consonants = ""
for i in range(len(txt4)):
    if txt4[i] not in vowels:
        consonants += txt4[i]
print(f"Text without vowels:\n -->{consonants}")
print("------------------------------------")

# Task №5
"""პროგრამამ მოგვთხოვოს სახელის და გვარის შეყვანა
თუ ორივეს სწორად შევიყვანთ დაწეროს
"თქვენ იდენტიფიცირებული ხართ",
თუ არასწორია - დაწეროს "ჩითერი ხარ",
სამჯერ არასწორად შეყვანის შემთხვევაში
დაასრულოს მუშაობა.
"""
tries = 2
while True:
    user_name = input("Enter your name: ")
    user_surname = input("Enter your surname: ")
    if tries == 0:
        print("You are cheater!")
        break
    elif user_name == "Giorgi" and user_surname == "Beridze":
        print("You are identified!")
        break
    else:

        print(f"Wrong credentials! you've left {tries} more tries!")
        tries -= 1
print("------------------------------------")

# Task №6
"""პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს
ბოლო, პირველი და ბოლოდან მეორე ასოები 5-ჯერ while ლუპით.
"""
word = input("Write a word: ")
print(word)
while True:
    for i in range(3):
        print(f"{i+1} - Last Letter - {word[-1]}")
    for i in range(3):
        print(f"{i+1} - Firs Letter - {word[0]}")
    for i in range(3):
        print(f"{i+1} - Penultimate Letter - {word[-2]}")
    break
