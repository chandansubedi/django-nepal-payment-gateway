from django.shortcuts import render,get_object_or_404
from django_esewa  import EsewaPayment
from .models import Product, Transaction
import uuid


def index(request):
    products = Product.objects.all()
    context={
        'products': products
        }
    return render(request, 'product/index.html',context)

def buy(request, id):
    product = get_object_or_404(Product, id=id)
    uid = uuid.uuid4()
    transaction = Transaction.objects.create(
    product=product,
    transaction_uuid= str(uid),
    transaction_amount=product.price,
    transaction_status='pending'

    )
    # Create an instance of the EsewaPayment class with the necessary parameters
   
    epayment = EsewaPayment(
    product_code='EPAYTEST', 
    success_url= f'http://localhost:8000/esewa/success/{product.id}',
    failure_url= f'http://localhost:8000/esewa/failure/{product.id}',
    secret_key="8gBm/:&EnhH.1/q",
    amount=product.price,
    total_amount=product.price,
    transaction_uuid=transaction.transaction_uuid,
    )
    epayment.create_signature(transaction_uuid=transaction.transaction_uuid)
    
    context = {
        'product': product,
        'form': epayment.generate_form(),

    }
    return render(request, 'product/buy.html',context )