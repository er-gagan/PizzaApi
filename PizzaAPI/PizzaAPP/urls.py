from django.urls import path
from .views import ApiRoot, pizzas,pizza_Detail,Regular,Square,Small_Size,Medium_Size,Large_Size
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',ApiRoot.as_view(), name='root'),
    path('all/',pizzas.as_view(), name='all'),
    path('all/<int:pk>/',pizza_Detail.as_view()),
    path('regular/',Regular.as_view(), name="Regular"),
    path('regular/<int:pk>/',pizza_Detail.as_view()),
    path('square/',Square.as_view(), name="Square"),
    path('square/<int:pk>/',pizza_Detail.as_view()),
    path('small/',Small_Size.as_view(), name="Small"),
    path('small/<int:pk>/',pizza_Detail.as_view()),
    path('medium/',Medium_Size.as_view(), name="Medium"),
    path('medium/<int:pk>/',pizza_Detail.as_view()),
    path('large/',Large_Size.as_view(), name="Large"),
    path('large/<int:pk>/',pizza_Detail.as_view()),
    path('<int:pk>/',pizza_Detail.as_view()),
]
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api'])