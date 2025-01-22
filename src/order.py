class Order:
    def __init__(self, order_id):
        self.order_id = order_id
        self.products = {}  # {product_id: quantity}

    def add_product(self, product, quantity):
        """Add a product to the order."""
        if product.product_id in self.products:
            self.products[product.product_id] += quantity
        else:
            self.products[product.product_id] = quantity

    def __str__(self):
        return f"Order(ID: {self.order_id}, Products: {self.products})"
