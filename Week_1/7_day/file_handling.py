# Write
# file = open("notes.txt", "w")
# file.write("Welcome h Python File Handling!\n")
# file.write("This is a new file.\n")
# file.close()

#Read
# file = open("notes.txt", "r")
# content = file.read()
# print("File Content:\n", content)
# file.close()

#Append
# file = open("notes.txt", "a")
# file.write("Adding a new line")
# file.close()

#With

# with open("notes.txt","r") as file:
#     for line in file:
#         print(line.strip())

#Example

# feedback = input("Enter your feedback: ")

# with open("feedback_log.txt", "a") as log:
#     log.write(feedback + "\n")

# print("Thanks for your feedback")


# with open("file.txt") as f:
#     while True:
#         line = f.readline()
#         if not line:
#             break
#         if "ERROR" in line:
#             print("Found error:", line.strip())

with open("file.txt") as f:
    for _ in range(10):
        print(f.readline().strip())