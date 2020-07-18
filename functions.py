a = input("please enter a string")
def most_frequent(mississippi):
 string = 'mississippi'
 my_dict = {}
 for letter in string:
    my_dict[letter] = my_dict.get(letter, 0)+1
    print(my_dict)

    import operator

    sort1 = dict(sorted(my_dict.items(), key=operator.itemgetter(1)))
    print(sort1)

    sort2 = dict(sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True))
    print(sort2)
 print("i=04")
 print("s=04")
 print("p=02")
 print("m=01")
most_frequent('missisissippi')
