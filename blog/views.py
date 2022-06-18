from django.shortcuts import render

# Create your views here.
def blogview(request):
    return render(request, 'blog/blog.html')