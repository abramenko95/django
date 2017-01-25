from django.shortcuts import render

def about_me(request):
    return render(request, 'blog/about_me.html')
def about_group(request):
    return render(request, 'blog/about_group.html')
def about_univer(request):
    return render(request, 'blog/about_univer.html')