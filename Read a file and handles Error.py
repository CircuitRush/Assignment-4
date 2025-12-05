try:
    with open("sample.txt") as file:
        print("File content:")
        for i, line in enumerate(file, 1):
            print(f"Line {i} : {line.rstrip()}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' doesnt exists.")