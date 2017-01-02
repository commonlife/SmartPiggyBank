from django.shortcuts import render
from django.views.generic import View
from .crawler import Collector
from .models import Product


class CrawlingView(View):
    def get(self, request):
        collector = Collector()
        product_list = collector.get_basic_info()
        for p in product_list:
            pid = p['id']
            if Product.objects.filter(product_id=pid).exists():
                pass
            else:
                p_orm = Product()
                p_orm.product_id = pid
                p_orm.name = p['name']
                p_orm.link = p['link']
                p_orm.thumb_image = p['thumb_image']
                p_orm.price = int(p['price'])
                p_orm.delivery = p['delivery']
                p_orm.category = 'shocking_deal'
                p_orm.save()
        context = {}
        return render(request, 'main.html', context)

    def check_pid_product(self, pid):
        return Product.objects.filter(product_id=pid).exists()