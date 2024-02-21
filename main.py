from Counter import Counter


text = input("Enter text: ")
print("Number of vowels:", Counter.count(text))
text = input("Enter text: ")
print("Text without repeated characters:", Counter.remove_repeated(text))
