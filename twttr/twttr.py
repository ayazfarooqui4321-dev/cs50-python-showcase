def main():
    text = input("Input: ").strip()
    print("Output", no_vowels(text))

def no_vowels(text):

    vowels = ['a', 'e', 'i', 'o', 'u']
    text_without_vowels = ""

    for char in text:
        if char.lower() not in vowels:
            text_without_vowels += char
    return text_without_vowels

main()
