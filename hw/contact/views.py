from django.shortcuts import render, redirect

from .models import Category, ContactMessage


def index(request):
    categories = Category.objects.all()
    context = {'categories': categories}

    return render(request, 'contact/index.html', context)


def create_category(request):
    name = request.POST.get('category_name')
    description = request.POST.get('category_description')

    category = Category(name=name, description=description)
    category.save()
    return redirect('index')


def create_message(request):
    category_id = request.POST.get('category_id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    category = Category.objects.get(pk=category_id)

    message = ContactMessage(
        category=category,
        name=name,
        email=email,
        message=message
    )
    message.save()
    return redirect('congratulation')


def congratulation(request):
    return render(request, 'contact/congratulation.html')