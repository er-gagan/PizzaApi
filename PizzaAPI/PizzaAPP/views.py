from .models import Pizza
from rest_framework import status
from rest_framework.response import Response
from .serializers import Pizza_Serializers
from rest_framework.views import APIView
from rest_framework.reverse import reverse

# Create your views here.

class pizzas(APIView):
    def get(self, request, format = None):
        reg = Pizza.objects.all()
        serializer = Pizza_Serializers(reg, many=True)
        return Response(serializer.data)
    
    def post(self, request, format = None):
        serializer = Pizza_Serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class pizza_Detail(APIView):
    def get_object(self, pk):
        try:
            return Pizza.objects.get(Id=pk)
        except Pizza.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk, format = None):
        pizza = self.get_object(pk)
        serializer = Pizza_Serializers(pizza)
        return Response(serializer.data)
    
    def put(self, request, pk, format = None):
        pizza = self.get_object(pk)
        serializer = Pizza_Serializers(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format = None):
        pizza = self.get_object(pk)
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Regular(APIView):
    def get(self, request, format = None):
        regular = Pizza.objects.filter(Category__iexact="Regular").all()
        serializer = Pizza_Serializers(regular, many=True)
        return Response(serializer.data)
    
class Square(APIView):
    def get(self, request, format = None):
        square = Pizza.objects.filter(Category__iexact="Square").all()
        serializer = Pizza_Serializers(square, many=True)
        return Response(serializer.data)
    
class Small_Size(APIView):
    def get(self, request, format = None):
        small = Pizza.objects.filter(Size__iexact="Small").all()
        serializer = Pizza_Serializers(small, many=True)
        return Response(serializer.data)
    
class Medium_Size(APIView):
    def get(self, request, format = None):
        medium = Pizza.objects.filter(Size__iexact="Medium").all()
        serializer = Pizza_Serializers(medium, many=True)
        return Response(serializer.data)

class Large_Size(APIView):
    def get(self, request, format = None):
        large = Pizza.objects.filter(Size__iexact="Large").all()
        serializer = Pizza_Serializers(large, many=True)
        return Response(serializer.data)

class ApiRoot(APIView):
    def get(self, request, format = None):
        return Response({
            'List All Pizza': reverse('all',request=request, format=format),
            'List All Regular Pizza': reverse('Regular',request=request, format=format),
            'List All Square Pizza': reverse('Square',request=request, format=format),
            'List All Small Size Pizza': reverse('Small',request=request, format=format),
            'List All Medium Size Pizza': reverse('Medium',request=request, format=format),
            'List All Large Size Pizza': reverse('Large',request=request, format=format),
        })