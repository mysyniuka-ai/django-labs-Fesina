from django.shortcuts import render

def home_view(request):
    context = {
        'title': 'Головна сторінка',
        'header': 'Вітаємо в нашому магазині ігор!',
        'content': 'Це головна сторінка сайту. Оберіть потрібний розділ нижче:',
        'is_home': True
    }
    return render(request, 'shop/base.html', context)

def page_one_view(request):
    context = {
        'title': 'Сторінка 1',
        'header': 'Каталог ігор',
        'content': 'Тут буде список доступних ігор та ключів активації.',
        'is_home': False
    }
    return render(request, 'shop/base.html', context)

def page_two_view(request):
    context = {
        'title': 'Сторінка 2',
        'header': 'Контакти та підтримка',
        'content': 'Зв\'яжіться з нами у разі виникнення проблем з активацією ключів.',
        'is_home': False
    }
    return render(request, 'shop/base.html', context)