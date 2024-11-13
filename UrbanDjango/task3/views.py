from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ClassHome(TemplateView):
    template_name = 'third_task/platform.html'


class ClassShop(TemplateView):
    template_name = 'third_task/games.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь можно произвести какие-то действия для создания контекста.
        # Для примера в словарь просто передаются две строки
        context['title'] = 'Игры'
        context['products'] = (['AtomicHeart', 'Cyberpunc 2077', 'PayDay 2'])
        return context


def func_shop(request):
    context = {
            'title': 'Игры',
            "products": ['AtomicHeart', 'Cyberpunc 2077', 'PayDay 2']
        }
    return render(request, 'third_task/games.html', context=context)


class ClassBasket(TemplateView):
    template_name = 'third_task/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Здесь можно произвести какие-то действия для создания контекста.
        # Для примера в словарь просто передаются две строки
        context['title'] = 'Игры'
        context['products'] = (['AtomicHeart', 'Cyberpunc 2077', 'PayDay 2'])
        return context
