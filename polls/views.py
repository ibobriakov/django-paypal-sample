from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from paypal.standard.forms import PayPalPaymentsForm


from django.conf import settings


# Create your views here.
from django.http import HttpResponse

def index(request):
    paypal_dict = {
	    "cmd": "_xclick-subscriptions",
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "a1": "0", # trial price 
        "p1": 1, # trial duration, duration of unit defaults to month 
        "a3": "29.95", # yearly price 
        "p3": 1, # duration of each unit (depends on unit) 
        "t3": "M", # duration unit ("M for Month") 
        "src": "1", # make payments recur 
        "sra": "1", # reattempt payment on payment error 
        "no_note": "1",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": "http://localhost" + 'paypal-ipn',
        "return_url": "https://www.example.com/your-return-location/",
        "cancel_return": "https://www.example.com/your-cancel-location/",

    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict, button_type="subscribe")
    context = {"form": form}
    template = loader.get_template('polls/index.html')
	#context = RequestContext(request, {
    #    'igor': 'test2',
    #})
    return render_to_response('polls/index.html',context)