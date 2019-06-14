
class IntegerCell:
    
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.value)


class IntegerList:

    def __init__(self):
        self.top =  IntegerCell(value=None, next=None, prev=None)
        self.end = IntegerCell(value=None, next=None, prev=self.top)
        self.top.next = self.end

    def shift(self, value: int):
        cell = IntegerCell(value, self.top.next, self.top)
        self.top.next.prev = cell
        self.top.next = cell
        return cell

    def push(self, value: int):
        new_cell = IntegerCell(value, next=self.end, prev=self.end.prev)
        self.end.prev.next = new_cell
        self.end.prev = new_cell
        return new_cell
    
    def insert_before(self, cell: IntegerCell, value: int):
        new_cell = IntegerCell(value, cell, cell.prev)
        cell.prev.next = new_cell
        cell.prev = new_cell
        return new_cell

    def find_cell(self, value: int):
        cell = self.top.next
        while cell is not self.end:
            if cell.value == value:
                return cell
            cell = cell.next
        return None

    def find_cell_before(self, value: int):
        cell = self.top.next
        while cell is not self.end:
            if cell.next.value == value:
                return cell
            cell = cell.next

        return None

    def copy(self):
        new_list = IntegerList()
        cell = self.top.next
        while cell != self.end:
            new_list.push(cell.value)
            cell = cell.next

        return new_list


    def __repr__(self):
        cell = self.top.next
        s = ""
        while cell is not self.end:
            s += " " + str(cell.value)
            cell = cell.next
        return s

