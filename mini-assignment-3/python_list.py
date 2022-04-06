# question 1
def get_duplicates(input_list):
    duplicates = []
    for list_item in input_list:
        if input_list.count(list_item) > 1:
            if duplicates.count(list_item) == 0:
                duplicates.append(list_item)

    return duplicates


# question 2
def merge_list(list1, list2):
    new_list = []
    # assume that length of both lists are equal
    for index in range(len(list1)):
        new_item = list1[index] + " " + list2[index]
        new_list.append(new_item)
    return new_list


# question 3
def add_in_nested_list():
    given_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
    add = ["h", "i", "j"]
    given_list[2][1][2].extend(add)
    print(given_list)


# question 4
def create_map_ascending(key, value):
    # assume that length of both lists are equal
    dict = {}

    for index in range(len(key)):
        mapped = map(key[index], value[index])
        dict.update(mapped)

    print(dict)


# question 5
def merge_map(dict1, dict2):
    dict3 = dict1.copy()

    for key, value in dict2.items():
        dict3[key] = value
    print(dict3)


# question 6
def rename_key(dict, oldKey, newKey):
    dict[newKey] = dict.pop(oldKey)
    print(dict)


# question 7
def dict_to_list(input_dict):
    new_dict = list(input_dict.items())
    print(new_dict)


# question 1
# numbers = [1, 2, 3, 2, 5, 3, 3, 5, 6, 3, 4, 5, 7]
# duplicates_items = get_duplicates(numbers)
# print("duplicates_items :-", duplicates_items)

# question 2
# list1 = ["a", "c"]
# list2 = ["b", "d"]
# mergedList = merge_list(list1, list2)
# print("merged list is  :-", mergedList)

# question 3
# add_in_nested_list()

# question 4
# keys = ['Ten', 'Twenty', 'Thirty']
# value = [10, 20, 30]
# create_map_ascending(keys, value)

# question 5
# given_dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# given_dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
# merge_map(given_dict1, given_dict2)

# question 6
# sampleDict = {
#   "name": "Kelly",
#   "age": 25,
#   "salary": 8000,
#   "city": "New york"
# }
#
# oldKey = "city"
# newKey = "location"
# rename_key(sampleDict, oldKey, newKey)

# question 7
# given_dict = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
# dict_to_list(given_dict)
