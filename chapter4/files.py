# try:
#     with open("file22.txt", "r") as file_local:
#         print(file_local.read())

# except FileNotFoundError as e:
#     print("File not found")


file_local = open("file.txt", "r")
file_local.
try:
    file_local.write("Hello, World!")

except IOError as ex:
    print("Unsupported operation")

except Exception as e:
    print("An error occurred")
    print(e)

finally:
    file_local.close()


# file_local = open('file.txt', 'r')

# print(file_local.readlines())

# print("-------------")
# print(file_local.read(2))
# print("----------------")


# for line in file_local:
#     print(line)

# print(file_local.closed)
# file_local.close()
# print(file_local.closed)


# local_file = open('file.txt', 'a')
# local_file.write('\nHello, World!')
# local_file.close()
