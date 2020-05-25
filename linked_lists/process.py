from list import IntegerList

list = IntegerList()
cell1 = list.shift(1)
cell2 = list.shift(2)
cell3 = list.shift(3)
cell4 = list.push(4)
cell5 = list.push(5)

print(list)
assert cell3.next == cell2
assert cell3.prev == list.top
assert cell4.next == cell5
assert cell4.prev == cell1
assert cell5.next == list.end
assert cell5.prev == cell4

finded_cell = list.find_cell(2)
assert finded_cell == cell2
finded_cell = list.find_cell_before(4)
assert finded_cell == cell1
new_cell = list.insert_before(finded_cell, 22)
assert new_cell.next == finded_cell
assert new_cell.prev == cell2
print(list)

new_list = list.copy()
print(new_list)

new_cell3 = new_list.find_cell(3)
new_cell2 = new_list.find_cell(2)
assert new_cell3.next == new_cell2
assert new_cell3.prev == new_list.top

sorted_list = list.insertion_sort()
print(sorted_list)
assert sorted_list.top.next.value == 1
cell1 = sorted_list.top.next
cell2 = cell1.next
cell3 = cell2.next
cell4 = cell3.next
cell5 = cell4.next
cell6 = cell5.next

assert cell1.next.value == 2
assert cell1.prev.value == None
assert cell2.next.value == 3
assert cell2.prev.value == 1
assert cell3.next.value == 4
assert cell3.prev.value == 2
assert cell4.next.value == 5
assert cell4.prev.value == 3
assert cell5.next.value == 22
assert cell5.prev.value == 4