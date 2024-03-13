#File Creation
with open("my_file.txt", "w") as file:
 file.write("Hello World!")
 file.write(" Here's some more text\n")
 file.write("This is the year 2024\n")
 file.write("These are even numbers 2,4,6,8")

# File Reading and Display
 with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())

# File Appending
with open("my_file.txt", "a") as file:
        file.write("We're appending 3 additional lines of text\n")
        file.write("1,089 X 9 = 9,801\n")
        file.write("Most people fall asleep in seven minutes\n")        

#Error Handling
try:
    with open("my_file.txt", "a") as file:
        file.write("We're appending 3 additional lines of text\n")
        file.write("1,089 X 9 = 9,801\n")
        file.write("Most people fall asleep in seven minutes\n")
except FileNotFoundError:
    print("File not found!")
except PermissionError:
    print("Permission denied to append to the file!")
except Exception as e:
    print("An error occurred while appending to the file:", e)
finally:
    print("File operations completed.")      
 