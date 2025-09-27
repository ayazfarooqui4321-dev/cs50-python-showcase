def main():
    UserInput = input()
    ConvertedText = Convert(UserInput)
    print(ConvertedText)

def Convert(EmotionsToEmoji):
    EmotionsToEmoji = str.replace(EmotionsToEmoji, ":)", "🙂")
    EmotionsToEmoji = str.replace(EmotionsToEmoji, ":(", "🙁")
    return EmotionsToEmoji

main()
