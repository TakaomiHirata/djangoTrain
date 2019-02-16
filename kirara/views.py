from django.shortcuts import render
from django.views.generic import DetailView,ListView
from .models import Chara
# Create your views here.
class CharaListView(ListView):
    model=Chara

class CharaDetailView(DetailView):
    model=Chara