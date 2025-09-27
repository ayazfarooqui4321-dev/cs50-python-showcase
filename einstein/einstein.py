def main():
    Mass = int(input("Please Enter mass as an integer (in kilograms): "))
    Energy = ConvertToEnergy(Mass)
    print(Energy)
def ConvertToEnergy(Mass):
    return Mass * pow(300000000, 2)
main()
