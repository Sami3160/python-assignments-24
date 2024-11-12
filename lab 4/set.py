set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1.add(6)
set2.add(9)

set1.remove(1)
set2.discard(8)

union_set = set1.union(set2)

intersection_set = set1.intersection(set2)

difference_set = set1.difference(set2)

symmetric_difference_set = set1.symmetric_difference(set2)

is_subset = {4, 5}.issubset(set1)

is_superset = set1.issuperset({4, 5})

is_disjoint = set1.isdisjoint({10, 11})

set3 = set1.copy()

set3.clear()

length_set1 = len(set1)

is_member = 3 in set1

for item in set1:
    print(item)

set4 = {x * 2 for x in range(5)}

frozen_set = frozenset(set1)
