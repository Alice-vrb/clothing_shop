# Use in console:
# python manage.py shell < seed_products.py - For Linux/macOS
# Get-Content seed_products.py | python manage.py shell - For Windows

from shop.models import Product

products = [
    Product(
        name="Classic White T-Shirt",
        description="Comfortable cotton T-shirt with a regular fit. Perfect for everyday wear.",
        price=19.99,
        category="T-Shirts",
        in_stock=True
    ),
    Product(
        name="Oversized Black Hoodie",
        description="Warm oversized hoodie made from soft cotton fabric. Features a front kangaroo pocket.",
        price=49.99,
        category="Hoodies",
        in_stock=True
    ),
    Product(
        name="Blue Denim Jeans",
        description="Classic straight-leg denim jeans with five pockets and a comfortable fit.",
        price=59.90,
        category="Jeans",
        in_stock=True
    ),
    Product(
        name="Beige Summer Dress",
        description="Lightweight summer dress with a floral pattern. Ideal for warm weather.",
        price=45.50,
        category="Dresses",
        in_stock=False
    ),
    Product(
        name="Leather Biker Jacket",
        description="Stylish black biker jacket with a front zipper and multiple pockets.",
        price=129.99,
        category="Jackets",
        in_stock=True
    )
]

Product.objects.bulk_create(products)
