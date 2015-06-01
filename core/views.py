# -*- encoding: utf-8 -*-
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView, ListView
from core.forms import NewsForm, EventForm, ProductForm, ClassificationForm
from core.models import News, Tag, Event, Product, Classification
from django.http import JsonResponse
import json
# Create your views here.


class NewsCreate(CreateView):
    model = News
    form_class = NewsForm
    template_name = "news_form.html"
    success_url = '/noticias/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        news = form.save(commit=False)
        news.save()
        tags_arr = []
        for tag in self.request.POST.getlist('tags', []):
            tags_arr.append(Tag.objects.get_or_create(name=tag)[0])
        news.tags = tags_arr
        news.save()
        form.save_m2m()
        return redirect('/noticias/')


class NewsUpdate(UpdateView):
    model = News
    form_class = NewsForm
    template_name = "news_form.html"
    success_url = '/noticias/'

    def form_valid(self, form):
        news = form.save(commit=False)
        news.save()
        #Tags actualmente
        tags = news.tags.all().values_list('id', flat=True)
        tags_arr = []
        for tag in self.request.POST.getlist('tags', []):
            tags_arr.append(Tag.objects.get_or_create(name=tag)[0])
        tags_id_arr = [t.id for t in tags_arr]
        #Nuevos..
        add_list = set(tags_id_arr) - set(tags)
        for tag_id in add_list:
            o_tag = Tag.objects.get(id=tag_id)
            news.tags.add(o_tag)
        #Quitar..
        remove_list = set(tags) - set(tags_id_arr)
        for tag_id in remove_list:
            o_tag = Tag.objects.get(id=tag_id)
            news.tags.remove(o_tag)
        return redirect('/noticias/')


class EventCreate(CreateView):
    model = Event
    form_class = EventForm
    template_name = "event_form.html"
    success_url = '/eventos/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EventCreate, self).form_valid(form)


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = '/productos/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ProductCreate, self).form_valid(form)


class ClassificationList(ListView):
    template_name = 'classification.html'
    context_object_name = 'all_root_elems'

    def get_queryset(self):
        return Classification.objects.filter(level=1)


#Clasificaciones
def add_classification(request):
    if request.method == "POST":
        formulario = ClassificationForm(request.POST, request.FILES)
        if formulario.is_valid():
            form = formulario.save()
    return JsonResponse({'id': form.id, 'name': form.name})


def save_classification(request, id):
    name = request.POST.get('name')
    try:
        o_classif = Classification.objects.get(id=id)
    except Classification.DoesNotExist:
        print 'error'
    else:
        o_classif.name = name
        o_classif.save()
        return JsonResponse({'response': 'ok'})


def delete_classification(request, id):
    try:
        o_classif = Classification.objects.get(id=id)
    except Classification.DoesNotExist:
        print 'error'
    else:
        o_classif.delete()
        return JsonResponse({'response': 'ok'})


def traverse(data, father=None, level=1):
    for i in data:
        is_edit, o_classif = False, Classification.objects.get(id=i['id'])
        if level != o_classif.level:
            o_classif.level, is_edit = level, True
        if o_classif.category_father_id != father:
            o_classif.category_father_id, is_edit = father, True
        if is_edit:
            o_classif.save()
        if 'children' in i:
            traverse(i['children'], i['id'], level + 1)


def synchronize_classification(request):
    data = json.loads(request.POST.get('data'))
    traverse(data)
    return JsonResponse({'response': 'ok'})











