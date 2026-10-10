Class Customer:
def __init__(self, customer_id, name):
    self.customer_id = customer_id
    self.name = name

Class Product:
def __init__(self, product_id, name, technology):
    self.name =name 
    self.product_id = product_id
    self.technology = technology

# ProductOffer: offer ID, offer name, product and discount percentage.
Class ProductOffer:
def __init__(self, offer_id, offer name, product, discount_percentage):
    self.offer_id = offer_id
    self.offer_name = offer_name    
    self.product = product
    self.discount_percentage = discount_percentage
# BillingOffer: billing offer name and monthly discount amount.  
Class BillingOffer:
def __init__(self, billing_offer_name, monthly_discount_amount):    
    self.billing_offer_name = billing_offer_name
    self.monthly_discount_amount = monthly_discount_amount
    self.billing_offer_name = billing_offer_name

    def discounted_price(self, price):
        return price * (1 - self.discount_percent / 100)


product = Product("P101", "5G Mobile Plan", "5G")
offer = ProductOffer("O101", "Festival Offer", product, 10)

print(offer.product.name)
print(offer.discounted_price(499))