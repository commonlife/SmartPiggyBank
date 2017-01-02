from .models import Product

class ShockingDealController:
    def __init__(self):
        pass

    def get_basic_list(self):
        return Product.objects.all().filter(category='shocking_deal').order_by('price')