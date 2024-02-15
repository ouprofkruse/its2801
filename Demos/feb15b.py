def pprint(my_string):
    msg = ""
    s = ""
    try:
        x = float(my_string)
        s = f"Value = {x:.3f}"
        # print(s)
    except ValueError:
        msg = "Error"
    return [msg,s]


while True:
    s = input("> ")
    if s == "q":
        break
    return_value = pprint(s)
    print(return_value)
    if return_value[0] == "":
        print("OK", return_value[1])
        break
    else:
        print("Try Again")
        continue
