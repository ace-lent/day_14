name = "asdfkiloveustill"
user = input("Enter word: ")

index = name.index(user)
if index != "yaks":
    print(f"The starting index is {index} and it ends at index {index + len(user) - 1}")
else:
    print("word not found")