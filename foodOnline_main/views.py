

from django.http import HttpResponse
from django.shortcuts import render
from menu.models import FoodItem
from django.db.models import Prefetch,Q
from vendor.models import Vendor


def home(request):
  vendors_origin=Vendor.objects.filter(is_approved=True,user__is_active=True).order_by('created_at')
  vendors=vendors_origin[:4]

 # vendor fast food
  fetch_vendors_by_fast_food=FoodItem.objects.filter(food_title__icontains="chicken",is_available=True).values_list('vendor',flat=True)
  vendors_fast_food=Vendor.objects.filter(Q(id__in=fetch_vendors_by_fast_food) | Q(vendor_name__icontains="chicken",is_approved=True,user__is_active=True)).order_by('created_at')[:4]

 # vendor pizza
  fetch_vendors_by_pizza=FoodItem.objects.filter(food_title__icontains="pizza",is_available=True).values_list('vendor',flat=True)
  vendors_pizza=Vendor.objects.filter(Q(id__in=fetch_vendors_by_pizza) | Q(vendor_name__icontains="pizza",is_approved=True,user__is_active=True)).order_by('created_at')[:4]

 # vendor hamburger
  fetch_vendors_by_hamburger=FoodItem.objects.filter(food_title__icontains="hamburger",is_available=True).values_list('vendor',flat=True)
  vendors_hamburger=Vendor.objects.filter(Q(id__in=fetch_vendors_by_hamburger) | Q(vendor_name__icontains="hamburger",is_approved=True,user__is_active=True)).order_by('created_at')[:4]

 # vendor drink
  fetch_vendors_by_drink=FoodItem.objects.filter(food_title__icontains="drink",is_available=True).values_list('vendor',flat=True)
  vendors_drink=Vendor.objects.filter(Q(id__in=fetch_vendors_by_drink) | Q(vendor_name__icontains="drink",is_approved=True,user__is_active=True)).order_by('created_at')[:4]

  context={
    'vendors':vendors,
    'vendors_pizza':vendors_pizza,
    'vendors_fast_food':vendors_fast_food,
    'vendors_hamburger':vendors_hamburger,
    'vendors_drink':vendors_drink,
  }
  return render(request,'home.html',context)