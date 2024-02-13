input_file = open("Demos/sample.txt")
# data = input_file.read()

# for i in range(2):

# while True:
#     data = input_file.readline()
#     if data == "":
#         break
for data in input_file:
    print(data.strip())
    # print(repr(data))

input_file.close()
