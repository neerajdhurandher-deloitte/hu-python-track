try:
    file = open("testFile.txt", "r")
    print("file open")
    print("file reading..")
    file_str = file.readlines()
    max_len_str = ""
    for items in file_str:
        lst = items.split(" ")
        temp = max(lst, key=len)

        if len(max_len_str) < len(temp):
            max_len_str = temp
    print("longest word in file :- ", max_len_str)

except FileNotFoundError as e:
    print(e)
finally:
    file.close()
    print("file close")
