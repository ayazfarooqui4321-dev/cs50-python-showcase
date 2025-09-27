def main():
    expr = input("Expression: ").strip()
    result = calc(expr)
    if result is not None:
        print(f"{result:.1f}")
    else:
        print("Invalid Operator")


def calc(expr):
      x, y, z = expr.split()
      x = float(x)
      z = float(z)

      match y:
          case '+':
              return x + z
          case '-':
              return x - z
          case '*':
              return x * z
          case '/':
              return x / z
          case _:
              return None
main()



