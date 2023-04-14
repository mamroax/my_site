from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Diet, Food


def home(request):
    context = {
        'food': Food.objects.all()
    }
    return render(request, 'food/home.html', context)


class FoodListView(ListView):
    model = Food
    template_name = 'food/home.html'
    context_object_name = 'food'
    ordering = ['-food_name']
    paginate_by = 5




class FoodDetailView(DetailView):
    model = Food


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    fields = ['food_name', 'description', 'calories', 'fat', 'proteins',
              'carbohydrates', 'glycemic_index', 'food_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class FoodUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Food
    fields = ['food_name', 'description', 'calories', 'fat', 'proteins',
              'carbohydrates', 'glycemic_index', 'food_image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return True


class FoodDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Food
    success_url = '/'

    def test_func(self):
        return True



def about(request):
    return render(request, 'food/about.html', {'title': 'О еде'})
