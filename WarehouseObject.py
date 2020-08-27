"""
Object to store warehouse name and inventory.
hold and restore functions are designed to stage data and "undo"
operations on the object when orders fail.

Since the inventories are maintained in these objects, when an
InventoryAllocator object successfully ships out of a warehouse,
the inventory is affected for the next shipment.

@author: Laurel Dernbach
@date: August 27, 2020
"""


class WarehouseObject(object):
    def __init__(self, warehouse_name, inventory_map):
        self.name = warehouse_name  # string
        self.inventory = inventory_map  # map {product:quantity}
        self.temp = inventory_map

    # remember the initial state of inventory before attempting
    # to process a shipment
    def hold(self):
        self.temp = self.inventory.copy()

    # restore to original state if order cannot be processed
    def restore(self):
        self.inventory = self.temp


