def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    #Take the dollar sign off
    d = float(str.strip(d, "$"))
    return d



def percent_to_float(p):
    # TODO
    #Take the percentage sign off and divide it by 100 to get the percent multiplier
    p = float(str.strip(p, "%")) / 100
    return p


main()
