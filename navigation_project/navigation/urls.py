from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_view, name='main'),
    path('detail/', views.detail, name='detail'),
    # path('input/', views.route_input, name='route_input'),
    path('result/<int:page_id>', views.detail_route, name='route_result')
]