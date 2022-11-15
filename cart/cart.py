from decimal import Decimal

from myshop.models import Product
from shop import settings


class Cart:
    def __init__(self, request):
        """Cart initialization."""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        # If session exists cart contains session_id, else None
        self.cart = cart

    def add(self, product: Product, quantity=1, update_quantity=False):
        """Add a product to the cart or update its quantity."""
        product_id = str(product.id)  # JSON only supports string keys

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save()

    def save(self):
        """Set session's attribute 'modified' to True"""
        self.session.modified = True

    def remove(self, product: Product):
        """Remove product from cart."""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """Iterating through the items in the cart and getting the products from the database."""
        products_ids = self.cart.keys()
        # get Product's objects and add them in a cart
        products = Product.objects.filter(id__in=products_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Counting all items in the cart."""
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """Calculate the cost of items in the shopping cart."""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """ Delete cart from session"""
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
