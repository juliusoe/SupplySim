class Warehouse:
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def add_product(self, product):
        """Add a product to the warehouse inventory."""
        self.inventory[product.product_id] = product

    def remove_product(self, product_id, quantity):
        """Remove a specified quantity of a product from the inventory."""
        if product_id in self.inventory:
            product = self.inventory[product_id]
            if product.quantity >= quantity:
                product.update_quantity(-quantity)
            else:
                print(f"Not enough stock to remove {quantity} of {product.name}.")
        else:
            print(f"Product ID {product_id} not found in inventory.")

    def get_product(self, product_id):
        """Retrieve a product by its ID."""
        return self.inventory.get(product_id, None)

    def __str__(self):
        return f"Warehouse({self.name}, Inventory: {len(self.inventory)} products)"
