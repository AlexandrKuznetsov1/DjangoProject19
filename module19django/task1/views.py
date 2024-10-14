from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import ContactForm
from .models import Buyer, Game


class myplatform(TemplateView):
    template_name = 'my_platform.html'


def shop(request):
    Games = Game.objects.all()
    paginate_by = request.GET.get('paginate_by', 1) or 1  # значение 1 установлено для наглядности
    paginator = Paginator(Games, paginate_by)
    page_number = request.GET.get('page')
    try:
        page_games = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_games = paginator.page(1)
    except EmptyPage:
        page_games = paginator.page(paginator.num_pages)
    context = {"Games": Games, 'page_games': page_games, }
    return render(request, 'my_shop.html', context)


def basket(request):
    return render(request, 'basket.html')


info = {}


# Использование класса Django:
def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #  обработка данных формы:
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data["age"]
            subscribe = form.cleaned_data["subscribe"]

            print(f"'Name' {name}")
            print(f"'password' {password}")
            print(f"'repeat_password' {repeat_password}")
            print(f"'age' {age}")
            print(f"'subscribe' {subscribe}")
            if password == repeat_password:
                buyer_name = Buyer.objects.filter(name=name)
                if buyer_name:
                    info['error'] = f'Пользователь {name} уже существует'
                    return HttpResponse(f"Ошибка, {info['error']}!")
                Buyer.objects.create(name=name, balance=0, age=age)
                return HttpResponse(f"Приветствуем, {name}!")
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(f"Ошибка, {info['error']}!")
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})


# Использование шаблона html:
def sign_up_by_html(request):
    if request.method == "POST":
        # получаем данные со стороны пользователя:
        name = request.POST.get('name')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        subscribe = request.POST.get('subscribe') == 'on'

        print(f"'Name' {name}")
        print(f"'password' {password}")
        print(f"'repeat_password' {repeat_password}")
        print(f"'age' {age}")
        print(f"'subscribe' {subscribe}")
        # http ответ пользователю
        if password == repeat_password and age >=18:
            buyer_name = Buyer.objects.filter(name=name)
            if buyer_name:
                info['error'] = f'Пользователь {name} уже существует'
                return HttpResponse(f"Ошибка, {info['error']}!")
            Buyer.objects.create(name=name, balance=0, age=age)
            return HttpResponse(f"Приветствуем, {name}!")
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return HttpResponse(f"Ошибка, {info['error']}!")
        if age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
            return HttpResponse(f"Ошибка, {info['error']}!")
    # если это Get-запрос:
    return render(request, 'registration_page.html', context=info)
