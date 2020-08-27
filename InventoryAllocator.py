"""
Object to process an order based on the warehouses it can ship from.
If an empty list is returned, the order could not be completed.

@author: Laurel Dernbach
@date: August 27, 2020
"""


class InventoryAllocator(object):
    def __init__(self, order, inventory):
        self.order = order  # map {product:quantity}
        self.inventory = inventory  # list of WarehouseObjects

    def allocate(self):
        allocation = {}
        # "copy" the warehouse inventory information to restore in the case of a failed order
        for warehouse in self.inventory:
            warehouse.hold()
        for product in self.order:
            quantity_needed = self.order[product]
            for warehouse in self.inventory:
                # move onto next product in order
                if quantity_needed == 0:
                    break
                if product in warehouse.inventory:
                    # no need to split product across warehouses
                    if quantity_needed <= warehouse.inventory[product]:
                        warehouse.inventory[product] -= quantity_needed
                        if warehouse.name in allocation:
                            allocation[warehouse.name].append({product: quantity_needed})
                        else:
                            allocation[warehouse.name] = [{product: quantity_needed}]
                        quantity_needed = 0
                    # attempt to split across warehouses
                    else:
                        if warehouse.inventory[product] > 0:
                            quantity_needed -= warehouse.inventory[product]
                            if warehouse.name in allocation:
                                allocation[warehouse.name].append({product: warehouse.inventory[product]})
                            else:
                                allocation[warehouse.name] = [{product: warehouse.inventory[product]}]
                            warehouse.inventory[product] = 0
            if quantity_needed > 0:
                print("ERROR: not enough inventory")
                # restore original inventory before order fails
                for warehouse in self.inventory:
                    warehouse.restore()
                return []

        return allocation






