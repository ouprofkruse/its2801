# Used for testing of small code snippets

msg = """ Welcome to
 !!! Turtle Control !!!"""
print(msg)

while True:
    answer = input("> ")
    tokens = answer.split(",")
    if tokens[0].lower() == "q":
        break
    try:
        print(tokens[0],int(tokens[1]))
    except:
        print("Whoops")
        continue


# print(answer.isnumeric())
# print(answer.isdecimal())
# print(answer.isdigit())

# print(answer,type(answer))


#print(int(answer))

# x = 3 * float(answer)
# print(x)

