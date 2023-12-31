class Cart():
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                "product_id": product.id,
                "name": product.title,
                "quantity": 1,
                "price": str(product.price),
                "image": product.image.url
            }
        else:
            self.cart[product_id]["quantity"] += quantity
            self.cart[product_id]["price"] = (float(self.cart[product_id]["price"]) + float(product.price))
        self.save()

    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def delete_one(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"] -= 1
            self.cart[product_id]["price"] = (float(self.cart[product_id]["price"]) - float(product.price))
            if self.cart[product_id]["quantity"] <= 0:
                self.delete(product)
        self.save()

    def delete_all(self):
        self.session["cart"] = {}
        self.session.modified = True

    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True