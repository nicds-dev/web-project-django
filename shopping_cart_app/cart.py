class Cart(models.Model):
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart", {})

    def add_product(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "product_id": product.id,
                "name": product.name,
                "quantity": 0,
                "price": str(product.price),
                "image": product.image.url
            }
        if update_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity
        self.save()

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True