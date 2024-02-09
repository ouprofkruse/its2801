# Used for testing of small code snippets

# msg = """ Welcome to
#  !!! Turtle Control !!!"""
# print(msg)

num = [128,256,1024]

while True:
    answer = input("> ")
    tokens = answer.split(",")
    if tokens[0].lower() == "q":
        break
    try:
        # print(tokens[0],int(tokens[1]))
        print(num[int(tokens[0])]/float(tokens[1]))
    except ValueError:
        print("Input not numeric or index not integer")
        continue
    except IndexError:
        print("Index not in range 0 to", len(num)-1)
        continue
    except ZeroDivisionError:
        print("Can't divide by zero")
        continue


# print(answer.isnumeric())
# print(answer.isdecimal())
# print(answer.isdigit())

# print(answer,type(answer))


#print(int(answer))

# x = 3 * float(answer)
# print(x)

