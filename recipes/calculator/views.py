from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recip_info(request):
    name = request.GET.get("name", 'omlet')
    quantity = request.GET.get("servings", 1)
    recipe={}
    for ing, am in DATA[name].items():
        recipe[ing] = am*float(quantity)
    context = {'recipe': recipe}

    #return HttpResponse('Hello')
    return render(request, 'calculator/index.html', context)
    #return TemplateResponse(request, "calculator/index.html", data)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
