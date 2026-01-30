data = input("Enter a number: ")

with open("output.txt", "w") as file:
    file.write(f"User entered: {data}\n")
with open("output.txt", "a") as file:
    file.write("This is additional data appended to the file.\n")
with open("output.txt", "r") as file:
    print("\nFinal content of the file:")
    for line in file:
        print(line.strip())
