def main():
    camelCase = input("camelCase: ").strip()
    camel_to_snake = snake_name(camelCase)
    print("snake_name: ", camel_to_snake)

def snake_name(camel_name):
    snake = ""

    for char in camel_name:
        if char.isupper():
            snake += "_" + char
        else:
            snake += char
    return snake.lower()

main()
