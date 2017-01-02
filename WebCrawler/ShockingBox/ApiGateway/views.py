from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from .models import Money
from Crawler11st.controller_product import ShockingDealController

class MoneySaveView(View):
    def get(self, request):
        result = {'result': 'ok'}
        user_id = request.GET.get('id', 'default')
        money_for_save = request.GET.get('money', 'none')
        count_of_500 = request.GET.get('500', 0)
        count_of_100 = request.GET.get('100', 0)
        print("{} : {}".format(user_id, money_for_save))

        if Money.objects.filter(user=user_id).exists():
            money = Money.objects.get(user=user_id)
            money.user = user_id
            money.money = int(money_for_save)
            money.won_100 = int(count_of_100)
            money.won_500 = int(count_of_500)
            money.save()
        else:
            money = Money()
            money.user = user_id
            money.money = int(money)
            money.won_100 = int(count_of_100)
            money.won_500 = int(count_of_500)
            money.save()

        print(result)
        return JsonResponse(result, safe=False)

class MoneyView(View):
    def get(self, request):
        result = {'result': 'ok'}
        user_id = request.GET.get('id', 'default')
        print("User ID : {}".format(user_id))
        result['id'] = user_id
        if Money.objects.filter(user=user_id).exists():
            mondey_obj = Money.objects.get(user=user_id)
            result['money'] = mondey_obj.money
            result['500'] = mondey_obj.won_500
            result['100'] = mondey_obj.won_100
            print(result)
            return JsonResponse(result, safe=False)
        else:
            result['money'] = 0
            result['500'] = 0
            result['100'] = 0
            print(result)
            return JsonResponse(result, safe=False)

class ShockingDealView(View):
    def get(self, request):
        shocking_controller = ShockingDealController()
        shocking_deal_list = shocking_controller.get_basic_list()
        print("list length : {}".format(len(shocking_deal_list)))

        result_list = []
        for item in shocking_deal_list:
            result_list.append({
                'pid': item.product_id,
                'name': item.name,
                'link': item.link,
                'thumb_image': item.thumb_image,
                'price': item.price,
                'delivery': item.delivery,
                'category': item.category,
            })
        print(result_list)
        return JsonResponse(result_list, safe=False)