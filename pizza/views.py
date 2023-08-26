from rest_framework.decorators import action
from .models import Pizza, Order, ToppingChoices, BaseChoices, CheeseChoices
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import timedelta
from django.utils import timezone

class Orders:
    queryset = Order.objects.all()

    @csrf_exempt
    def create_order(request):
        if request.method == 'POST':
            try:
                data = json.loads(request.body)
                if len(data)!=1 and 'pizza' not in data:
                    raise ValidationError('Invalid input data')
                pizza_data = data.get('pizza', [])
                
                if not isinstance(pizza_data, list) or len(pizza_data) == 0:
                    raise ValidationError('Pizzas should be provided as a non-empty list.')
                order = Orders.create_order_from_pizzas(pizza_data)
                return JsonResponse(order, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'error': 'bad_request'}, status=status.HTTP_404_NOT_FOUND)

    def create_order_from_pizzas(pizza_data):
        order = Order.objects.create()
        pizza_list=[]
        for pizza_info in pizza_data:
            if len(pizza_info)!=3 and 'toppings' not in pizza_info and 'pizza_base' not in pizza_info and 'cheese' not in pizza_info:
                raise ValidationError('Invalid pizza data')
            if not isinstance(pizza_info['toppings'], list) or not Orders.is_sublist(pizza_info['toppings'], ToppingChoices.TOPPING_LIST) or len(pizza_info['toppings']) != 5:
                raise ValidationError('Toppings should be a list and should contain valid choices.')

            value= ', '.join(pizza_info['toppings'])
            if not isinstance(pizza_info['cheese'], str):
                raise ValidationError('Cheese should be a string')
            if not isinstance(pizza_info['pizza_base'], str):
                raise ValidationError('Base should be a string')

            pizza = Pizza.objects.create(base=pizza_info['pizza_base'],
                                         cheese=pizza_info['cheese'],
                                         toppings=value,
                                         order=order)
            pizza_list.append(pizza)

        return {'order': order.order_number}

    def choice(request):
        toppings = ToppingChoices.TOPPING_LIST
        pizza_bases = BaseChoices.BASE_LIST
        cheeses = CheeseChoices.CHEESE_LIST
        response_data = {
            'toppings': toppings,
            'pizza_base': pizza_bases,
            'cheese': cheeses,
        }
        return JsonResponse(response_data, status=status.HTTP_200_OK)

    @csrf_exempt
    @action(detail=True, methods=['post'])
    def getting_status(request):
        try:
            data = json.loads(request.body)
            order_number = data.get('order_number', None)
            order = Order.objects.get(order_number=order_number)
            Orders.update_status(order)
            pizza_data = list(Pizza.objects.values_list('base', 'cheese', 'toppings').filter(order=order))
            pizza_list_of_dicts = []
            for base, cheese, toppings in pizza_data:
                pizza_dict = {
                    'base': base,
                    'cheese': cheese,
                    'toppings': toppings,
                }
                pizza_list_of_dicts.append(pizza_dict)

            return JsonResponse(
                {
                    'order_number': order.order_number,
                    'status': order.status,
                    'pizza':pizza_list_of_dicts,
                },
                status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)},
                                status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def update_status(order):
        current_time = timezone.now()
        elapsed_time = current_time - order.timestamp
        if order.status == 'Placed'  and timedelta(
                minutes=1) < elapsed_time <=timedelta(
                minutes=2):
            order.status = 'Accepted'
        elif order.status == 'Accepted' and timedelta(
                minutes=2) < elapsed_time <= timedelta(
                minutes=5):
            order.status = 'Preparing'
        elif order.status == 'Preparing' and timedelta(
                minutes=5) < elapsed_time <= timedelta(
                minutes=10):
            order.status = 'Dispatched'
        elif order.status == 'Dispatched' and timedelta(
                minutes=10) < elapsed_time:
            order.status = 'Delivered'
        order.save()
      
    @staticmethod
    def is_sublist(sublist, main_list):
        sub_len = len(sublist)
        for i in range(len(main_list) - sub_len + 1):
            if main_list[i:i+sub_len] == sublist:
                return True
        return False
