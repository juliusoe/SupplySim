class Product:
    def __init__(self, product_id, name, quantity):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity

    def update_quantity(self, amount):
        """Update the product quantity when stock is added or removed."""
        self.quantity += amount

    def __str__(self):
        return f"Product(ID: {self.product_id}, Name: {self.name}, Quantity: {self.quantity})"
