from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Order,Profile
from django.contrib.auth.models import User

class Home(ListView):
    model = Order
    template_name = 'app/home.html'
    context_object_name = 'orders'
    ordering = ['-created_at']

class CreateOrder(CreateView):
    model = Order
    fields = ['position', 'price', 'quantity']


    def form_valid(self, form):
        form.instance.profile = Profile.objects.filter(user=User.objects.get(username=self.request.user))[0]
        if form.instance.position == 'BUY':
            sell_orders = Order.objects.filter(position='SELL').filter(done='NOT COMPLETED').filter(price__lte=form.instance.price).filter(~Q(profile=form.instance.profile))
            if sell_orders:
                form.instance.done = 'COMPLETED'
                sell_orders[0].done = 'COMPLETED'

                wallet_seller = float(sell_orders[0].profile.wallet)
                wallet_buyer = float(form.instance.profile.wallet)
                quantity = float(form.instance.quantity)

                # new wallet
                sell_orders[0].profile.wallet = wallet_seller - form.instance.quantity
                form.instance.profile.wallet = wallet_buyer + quantity

                # new quantity
                BTC_left = sell_orders[0].quantity - form.instance.quantity
                if BTC_left == 0:
                    sell_orders[0].done = 'COMPLETED'
                elif BTC_left < 0:
                    return HttpResponseRedirect('/error/')
                else:
                    sell_orders[0].quantity = BTC_left
                    sell_orders[0].done = 'NOT COMPLETED'


                # profit
                sell_orders[0].profile.profit += sell_orders[0].profile.wallet - wallet_seller
                form.instance.profile.profit += form.instance.profile.wallet - wallet_buyer


                sell_orders[0].save()
                sell_orders[0].profile.save()
                form.instance.profile.save()

            else:
                form.instance.done = 'NOT COMPLETED'

        return super().form_valid(form)


class Profit(ListView):
    model = Profile
    template_name = 'app/profit-and-loss.html'
    context_object_name = 'profiles'

def Error(request):
    return render(request, 'app/error.html')
