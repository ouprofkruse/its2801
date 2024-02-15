def pprint(my_string):
    msg = ""
    x = 0
    y = 0
    try:
        parts = my_string.split()
        x = float(parts[0])
        y = float(parts[1])
        # print(s)
    except:
        msg = "Error"
    return [msg,[x,y]]


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
