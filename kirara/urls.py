from django.urls import path
from . import views

urlpatterns=[
    path('<int:pk>/',views.CharaDetailView.as_view(),name='chara_detail'),
    path('',views.CharaListView.as_view()),
]