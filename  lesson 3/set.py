from PIL.ImageChops import difference

my_set = {1,2,3}

my_set = set([4,5,6])

my_set =set()

my_set = {1,2,2,3,3,3}
print(my_set)

set1 = {1,2,3}
set2 = {3,4,5}

union_result_method = set1.union(set2)
union_result_operator = set1 | set2

print("rezultati i unionit: ",union_result_method)
print("rezultati i operiminit 2",union_result_operator)

intersection_result_method = set1.intersection(set2)
intersection_result_operator = set1 & set2

print("intersection of set 1 and set 2 using intersection method: ",intersection_result_method)
print("intersection of set 1 and set 2 using operator method: ",intersection_result_operator)

difference_result_method = set1.difference(set2)
difference_result_operator = set1 - set2

print("diffrence of set 1 and 2 using diffference method: ",difference_result_method)
print("diffrence of set 1 and 2 using operator method: ",difference_result_operator)

symmetric_difference_method = set1.symmetric_difference(set2)
symmetric_difference_operator = set1 ^ set2

print("symmetric diffrence of set 1 and 2 using symmetric diffference method",symmetric_difference_method)
print("symmetric diffrence of set 1 and 2 using symmetric diffference operator",symmetric_difference_operator)

my_set = {1,2,3}

my_set.add(7)

my_set.remove(3)

my_set.discard(8)

print(my_set)

my_set.clear()

print(my_set)