import random
# COLORS = ("black","blue","green","brown2","darkmagenta","darkorange","red")
# COLORS = ("black","blue","green")
COLORS = ("red","blue","green","brown2","darkmagenta")
c_len = len(COLORS)

n = 0
x = 0
while x <= 0.9:
    n += 1
    x = random.random()
print(n)


# n = 0
# while n<c_len:
#     print(COLORS[n])
#     n+=1


# for c in COLORS:
#     print(c)



# n = -1

# if n >= 0 and n <= c_len -1:
#     print(COLORS[n])


# if c_len < 5:
#     print("Only",c_len,"Colors")
# if c_len == 5 and "blue" in COLORS:
#     print("Blue!")
# elif c_len == 5:
#     print("Just enough colors")
#     if "black" in COLORS:
#         print("We have black")
#     else:
#         print("No Black")
# else:
#     print("Enough colors")

# == > < >= <= != in