from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from django.views.generic import ListView , DetailView , CreateView




# Create your views here.
def home(request):
    context={
    'posts':post.objects.all()
    }
    return render(request,'blogapp/home.html',context)

class postview(ListView):
    model=post
    template_name='blogapp/home.html'
    context_object_name='posts'
    ordering=['-date_posted']


class detailview(DetailView):
    model=post



class createview(CreateView):
    model=post
    fields=['title','content','image']



def about(request):
    return render(request,'blogapp/about.html',{'title':'About'})
