from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from selfApp.forms import *
from .models import *


menua = [
    {'title':'О сайте', 'url_name':'about'},
    {'title':'Добавить статью', 'url_name':'addpage'},
    {'title':'Обратная связь', 'url_name':'contact'},
    {'title':'Войти', 'url_name':'login'}
]


class ActorHome(ListView):
    model = Actor
    template_name = 'selfApp/index.html'
    context_object_name = 'actors'
    paginate_by = 4
    extra_context = {'title':'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['menu'] = menua
        context['title'] = 'Главная страница'
        context['categories'] = Category.objects.all()
        context['cat_selected'] = 0
        return context
    
    def get_queryset(self):
        return Actor.objects.filter(is_published=True)


def about(request):
    actors = Actor.objects.all()
    menu = menua  
    page_obj = Paginator(actors, 3).get_page(request.GET.get('page'))


    return render(request, 'selfApp/about.html', locals())



class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'selfApp/addpage.html'
    success_url = reverse_lazy('homepage')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Добавление статьи'
        context['menu'] = menua
        return context
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')

#     else:
#         form = AddPostForm()


    # return render(request,'selfApp/addpage.html', {'form':form, 'menu':menu, 'title':'Добавление статьи'})













def contact(request):
    return HttpResponse('Обратная связь...')

def login(request):
    return HttpResponse('Авторизация')


class ActorCategory(ListView):
    model = Actor
    context_object_name = 'actors'
    template_name = 'selfApp/index.html'

    def get_queryset(self):
        #первое он аддресуется к его категории после с двумя нижними подчеркиваниями к его атрибуту, а то что slug это мы указали на urls.py
        return Actor.objects.filter(category__url = self.kwargs['urlpost_slug'], is_published = True) 

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Категория " + str(context['actors'][0].category)
        context['menu'] = menua
        context['categories'] = Category.objects.all()
        context['cat_selected'] = 1

        return context



# class ShowPost(DetailView):
#     model = Actor
#     template_engine = 'selfApp/post.html'
#     context_object_name = 'post'
#     slug_url_kwarg = 'post_slug'

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context = context['post'].title
    #     context['menu'] = menu
    #     context['categories'] = Category.objects.all()
    #     context['cat_selected'] = 1


def show_post(request, post_slug):
    post = get_object_or_404(Actor, url=post_slug)

    categories = Category.objects.all()
    context = {
        'post':post,
        'menu':menua,
        'title':post.title,
        'categories':categories,
        'cat_selected':post.category.url,
    }
    return render(request, 'selfApp/post.html', context )

