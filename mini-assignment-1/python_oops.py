from collections import Counter
from itertools import permutations


class StringClass:

    def __init__(self, inputString):
        self.string = inputString

    def lengthOfString(self):
        return len(self.string)

    def str2listConverter(self, inputStr):
        return [char for char in inputStr]


class SearchCommonElements(StringClass):

    def commonElements(self):
        d = dict(Counter(list(self.string)))
        res = []
        for j in d:
            if d[j] >= 2:
                res.append(j)
        return res


class PairsPossible(StringClass):
    def pairs(self):
        list = []

        list1 = StringClass.str2listConverter(self,self.string)
        for i in range(0,len(list1)):
            temp = ""
            for j in range(i+1,len(list1)):
                temp = list1[i]+list1[j]
                list.append(temp)
        return list


stringClass = StringClass("hello")
print("length of the string :- ", stringClass.lengthOfString())
print("String converted to list : - ", stringClass.str2listConverter("neeraj"))

pairPossible = PairsPossible("hello")
print("all possible pairs are :- ", pairPossible.pairs())

searchCommonElements = SearchCommonElements("ajfbafbah")
print("Common elements are :- ",searchCommonElements.commonElements())
