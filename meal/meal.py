def main():
    meal_time = input("What time is it in a 24 hr time format(eg, 13:00)? ").strip()
    meal_hour = convert(meal_time)

    if 7 <= meal_hour <= 8:
        print("breakfast time")
    elif 12 <= meal_hour <= 13:
        print("lunch time")
    elif 18 <= meal_hour <= 19:
        print("dinner time")
    else:
        print("It is not breakfast, lunch, or dinner time!")


def convert(meal_time):
    hrs, mins = meal_time.split(":")
    return int(hrs) + int(mins) / 60

if __name__== "__main__":
    main()
