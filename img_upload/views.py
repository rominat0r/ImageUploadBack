from django.http import JsonResponse
from .models import Product 
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework import status
import os
from django.conf import settings
from django.http import HttpResponse, Http404

@api_view(['GET', 'POST'])
def product_list(request):
    if request.method == 'GET':
        drinks = Product.objects.all()
        serializer = ProductSerializer(drinks, many = True)
        return JsonResponse({'drinks':serializer.data})

    if request.method == 'POST':
        print(request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def model_list(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'models/my_ssd_mobnet.zip')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404