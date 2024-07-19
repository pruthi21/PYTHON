set1 ={1,2,3,'hello',6}
set2 =([3,4,5,'hello',6])
print(set1)
print(set2)

elements =[1,2,3,4,5]
my_set =set(*[elements])
print(my_set)
print()

empty_set = set()
print(empty_set)
print()

unique_set ={1,2,3,4,4,4,5,6}
print(unique_set)

my_set ={6,2,4,5,1}
print(my_set)


my_set ={1,2,3}
my_set.add(4)
my_set.remove(2)
print(my_set)

set1 ={1,2,3,4,'hello',5}
for i in set1:
    print(i)