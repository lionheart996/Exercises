path = input().split("\\")

file_name = path[-1].split(".")[0]
file_extension = path[-1].split(".")[1]

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
