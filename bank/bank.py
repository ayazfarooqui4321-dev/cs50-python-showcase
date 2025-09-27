greeting = input("Greeting: ")
greeting = greeting.lower().strip()

match greeting:
    case "hello" | "hello, newman":
        print("$0")
    case "hey" | "how you doing?" | "how's it going?":
        print("$20")
    case "what's happening?" | "what's up?":
        print("$100")
    case _:
        print("Please type expected greetings")
