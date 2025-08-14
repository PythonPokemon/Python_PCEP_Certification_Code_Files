"""
wenn man im ersten promt 'kangaroo' eingibt sind das 8 Zeichen, dann wird das zeichen in referenz a gespeichert
im zweiten prompt '0' * 2 == 0, dann wird das zeichen in referenz b gespeichert
an schließend wird a mit 8 zeichen durch b geteilt und ausgegeben == 4
"""
try:
    # first_prompt = input("Enter the first value: ")
    first_prompt = "kangaroo"
    a = len(first_prompt)
    # second_prompt = input("Enter the second value: ")
    second_prompt = "0"
    b = len(second_prompt) * 2
    print(a/b)  # 4.0
except ZeroDivisionError:
    print("Do not divide by zero!")
except ValueError:
    print("Wrong value.")
except:
    print("Error.Error.Error.")
