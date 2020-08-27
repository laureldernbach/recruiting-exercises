from InventoryAllocator import InventoryAllocator
from WarehouseObject import WarehouseObject
"""
Test file for InventoryAllocator class which implements
WarehouseObject objects.

@author: Laurel Dernbach
@date: August 27, 2020
"""
wh1 = WarehouseObject("owd", {"apple": 1})
wh2 = WarehouseObject("owd", {"apple": 0})
wh3 = WarehouseObject("dm", {"apple": 5})
wh4 = WarehouseObject("owd", {"apple": 5})

# assignment example 1
test1 = InventoryAllocator({"apple": 1}, [wh1])
print("test1:", test1.allocate())
print("Expected: [{'owd': {'apple': 1}}]")

# assignment example 2
test2 = InventoryAllocator({"apple": 1}, [wh2])
print("test2:", test2.allocate())
print("Expected: []")

# assignment example 3
test3 = InventoryAllocator({"apple": 10}, [wh3, wh4])
print("test3:", test3.allocate())
print("Expected: [{'dm': {'apple': 5}}, {'owd': {'apple': 5}}]")

# some more complex cases
nashville = WarehouseObject("Nashville", {"drums": 100, "guitar": 30, "bass": 75, "keyboard": 17})
austin = WarehouseObject("Austin", {"drums": 54, "guitar": 63, "banjo": 21, "saxophone": 4})
losAngeles = WarehouseObject("Los Angeles", {"drums": 30, "guitar": 4, "bass": 57, "synthesizer": 400})

# test case: multiple products in order, all possible
test4 = InventoryAllocator({"drums": 30, "guitar": 50, "bass": 76, "saxophone": 2}, [nashville, austin, losAngeles])
print("test4:", test4.allocate())
print("Expected:{'Nashville': [{'drums': 30}, {'guitar': 30}, {'bass': 75}], 'Austin': [{'guitar': 20}, "
      "{'saxophone': 2}], 'Los Angeles': [{'bass': 1}]}")

# test case: multiple products in order, some not possible
test5 = InventoryAllocator({"drums": 75, "guitar": 13, "bass": 200, "banjo": 13}, [nashville, austin, losAngeles])
print("test5:", test5.allocate())
print("Expected: []")

# test case: does inventory replenish after a failed order?
test6 = InventoryAllocator({"drums":  20, "guitar": 3, "bass": 12, "synthesizer": 139}, [nashville, austin, losAngeles])
print("test6:", test6.allocate())
print("Expected: {'Nashville': [{'drums': 20}], 'Austin': [{'guitar': 3}], 'Los Angeles': [{'bass': 12}, "
      "{'synthesizer': 139}]}")

# test case: product in order not in any inventory
test7 = InventoryAllocator({"drums":  3, "guitar": 5, "bass": 1, "bongos": 4}, [nashville, austin, losAngeles])
print("test7:", test7.allocate())
print("Expected: []")