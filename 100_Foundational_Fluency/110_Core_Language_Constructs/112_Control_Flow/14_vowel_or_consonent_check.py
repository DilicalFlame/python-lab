# Check if a character is a vowel or consonant

def check_vowel_or_consonant(c):
    vowels = 'aeiouAEIOU'
    if c.isalpha():  # Check if the input is an alphabet
        if c in vowels:
            return f"{c} is a vowel."
        else:
            return f"{c} is a consonant."
    else:
        return "Invalid input. Please enter an alphabet."

char = input("Enter a character: ")
result = check_vowel_or_consonant(char)
print(result)