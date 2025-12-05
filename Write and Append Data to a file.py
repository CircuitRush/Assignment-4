# Step 1: Take user input and write to file
text = input("Enter text to write to the file : ")
with open("output.txt", "w") as file:
    file.write(text + "\n")

print("Data successfully written to file output.txt.\n")

# Step 2: Take additional text and append to the same file
append_text = input("Enter Additional text to append: ")
with open("output.txt", "a") as file:
    file.write(append_text + "\n")

print("Data successfully appended to output.txt.\n")

# Step 3: Read and display the final content
print("Final content of the file:")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)