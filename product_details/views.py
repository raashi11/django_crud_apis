from django.shortcuts import render
from rest_framework import generics
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product


@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = request.POST.get('category')
        brand_name = request.POST.get('brand_name')
        image = request.FILES.get('image')
        product = Product.objects.create(name=name, category=category, brand_name=brand_name, image=image)
        return JsonResponse({'success': True, 'message': 'Product added successfully'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt
def update_product(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        product.name = request.POST.get('name')
        product.category = request.POST.get('category')
        product.brand_name = request.POST.get('brand_name')
        if request.FILES.get('image'):
            product.image = request.FILES.get('image')
        product.save()
        return JsonResponse({'success': True, 'message': 'Product updated successfully'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt
def delete_product(request, id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=id)
        product.delete()
        return JsonResponse({'success': True, 'message': 'Product deleted successfully'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})

class ProductSearchView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        category = self.request.query_params.get('category', '')
        brand_name = self.request.query_params.get('brand_name', '')
        queryset = Product.objects.filter(name__icontains=name, category__icontains=category, brand_name__icontains=brand_name)
        return queryset