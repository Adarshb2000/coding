from typing import OrderedDict


def fetchItems(numOfItems: int, items: OrderedDict, sortParameter: int, sortOrder: int, itemsPerPage: int, pageNumber: int):
    items = [[i[0], i[1][0], i[1][1]] for i in items.items()]
    items = sorted(items, key=lambda x: x[sortParameter], reverse=sortOrder)
    print(items)
    return [item[0] for item in items[itemsPerPage * pageNumber : itemsPerPage * (pageNumber + 1)]]

print(fetchItems(2, OrderedDict([('p1', (1, 2)), ('p2', (2, 1))]),0 , 0, 1 ,0))