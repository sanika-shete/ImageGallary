from django.shortcuts import render


def MY_GALLERY(request):
    return render(request, 'images.html')