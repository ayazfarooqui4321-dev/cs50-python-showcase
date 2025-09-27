def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(p):
    #Rule 1: chars must be between 2 and 6 chars
    if not (2 <= len(p) <= 6):
        return False
    #Rule 2: Must start with first 2 letters
    if not (p[0].isalpha() and p[1].isalpha()):
        return False
    #Rule 3: No puntuation allowed
    if not p.isalnum():
        return False
    #Rule 4: Num must be at the end and NOT start with 0
    dig_found = False
    for i in range(len(p)):
        if p[i].isdigit():
            if not dig_found: #True condition
                if p[i] == '0': #Check for 0 at p[0], since it's not allowed
                    return False
                dig_found = True
        elif dig_found:
            return False #No letters allowed after digits
    return True

main()
