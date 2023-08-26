from django.db import models


class ToppingChoices:
    PEPPERONI = 'pepperoni'
    MUSHROOM = 'mushroom'
    ONION = 'onion'
    OLIVE = 'olive'
    TOMATO = 'tomato'
    BELL_PEPPER = 'bell-pepper'
    JALAPENO = 'jalapeno'

    TOPPING_CHOICES = [
        (PEPPERONI, 'Pepperoni'),
        (MUSHROOM, 'Mushroom'),
        (ONION, 'Onion'),
        (OLIVE, 'Olive'),
        (TOMATO, 'Tomato'),
        (BELL_PEPPER, 'Bell Pepper'),
        (JALAPENO, 'Jalapeno'),
    ]

    TOPPING_LIST = [
        PEPPERONI, MUSHROOM, ONION, OLIVE, TOMATO, BELL_PEPPER, JALAPENO
    ]


class BaseChoices:
    THIN_CRUST = 'Thin Crust'
    NORMAL = 'Normal'
    CHEESE_BURST = 'Cheese Burst'

    BASE_CHOICES = [
        (THIN_CRUST, 'Thin Crust'),
        (NORMAL, 'Normal'),
        (CHEESE_BURST, 'Cheese Burst'),
    ]

    BASE_LIST = [THIN_CRUST, NORMAL, CHEESE_BURST]


class CheeseChoices:
    MOZZARELLA = 'Mozzarella'
    CHEDDAR = 'Cheddar'
    PARMESAN = 'Parmesan'
    BLUE_CHEESE = 'Blue Cheese'

    CHEESE_CHOICES = [
        (MOZZARELLA, 'Mozzarella'),
        (CHEDDAR, 'Cheddar'),
        (PARMESAN, 'Parmesan'),
        (BLUE_CHEESE, 'Blue Cheese'),
    ]

    CHEESE_LIST = [MOZZARELLA, CHEDDAR, PARMESAN, BLUE_CHEESE]


class StatusChoices:
    PLACED = 'Placed'
    ACCEPTED = 'Accepted'
    PREPARING = 'Preparing'
    DISPATCHED = 'Dispatched'
    DELIVERED = 'Delivered'

    STATUS_CHOICES = [
        (PLACED, 'Placed'),
        (ACCEPTED, 'Accepted'),
        (PREPARING, 'Preparing'),
        (DISPATCHED, 'Dispatched'),
        (DELIVERED, 'Delivered'),
    ]

    STATUS_LIST = [PLACED, ACCEPTED, PREPARING, DISPATCHED, DELIVERED]


class Pizza(models.Model):
    base = models.CharField(max_length=20, choices=BaseChoices.BASE_CHOICES)
    cheese = models.CharField(max_length=20,
                              choices=CheeseChoices.CHEESE_CHOICES)
    toppings = models.CharField(max_length=500)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)

    def __str__(self):
        return f"Pizza - Order #{self.order.order_number}"


class Order(models.Model):
    status = models.CharField(max_length=20,
                              choices=StatusChoices.STATUS_CHOICES,
                              default=StatusChoices.PLACED)
    timestamp = models.DateTimeField(auto_now_add=True)
    order_number = models.AutoField(primary_key=True)

    def __str__(self):
        return f"Order - Order #{self.order_number}"
