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

