# Writing to a file
with open("student.txt", "w") as f:
    f.write("Waseem, 20, CS\n")
    f.write("Ali, 21, IT\n")


# Reading from a file
with open("student.txt", "r") as f:
    data = f.read()
    print(data)