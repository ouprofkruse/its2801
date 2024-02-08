num = [128,256,1024]

while True:
    answer = input("> ")
    tokens = answer.split()
    if tokens[0][0].lower() == "q":
        break
    else:
        # print(answer.isnumeric())
        # print(answer.isdecimal())
        # print(answer.isdigit())
        try:
            print(num[int(tokens[0])]/float(tokens[1]))
        except ValueError:
            print("Not a number!")
            continue
        except IndexError:
            print("Index must be 0 to",len(num)-1)
            continue
        except ZeroDivisionError:
            print("Yoou can't divide by zero!")
            continue
    # print("Again")

