from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.models import User
from core.forms import UserUpdateForm, UserForm, CategoryForm, EventForm, ProductForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from core.models import News, Category, Event, Product
from core.views import NewsCreate, NewsUpdate, EventCreate, ProductCreate, ClassificationList
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    url(r'^usuarios/$', login_required(ListView.as_view(template_name="users.html", model=User,
                                                        paginate_by=20)), name='users'),
    url(r'^agregar-usuario/$', login_required(CreateView.as_view(
        model=User, form_class=UserForm, template_name="user_form.html", success_url='/usuarios/')),
        name='create_user'),
    url(r'^modificar-usuario/(?P<pk>\d+)/$', login_required(UpdateView.as_view(
        model=User, form_class=UserUpdateForm, template_name="user_form.html", success_url='/usuarios/')),
        name='update_user'),
    url(r'^eliminar-usuario/(?P<pk>\d+)/$', login_required(DeleteView.as_view(
        model=User, success_url='/usuarios/')), name='delete_user'),
    url(r'^iniciar-sesion/$', auth_views.login, {'template_name': 'user/login_logout_register/sign-in.html'},
        name='auth_login'),
    url(r'^cerrar-sesion/$', auth_views.logout, {'next_page': '/iniciar-sesion/'},
        name='auth_logout'),
    #Noticias
    url(r'^noticias/$', login_required(ListView.as_view(template_name="news.html", model=News,
                                                        paginate_by=20)), name='news'),
    url(r'^agregar-noticia/$', login_required(NewsCreate.as_view()), name='create_news'),
    url(r'^modificar-noticia/(?P<pk>\d+)/$', login_required(NewsUpdate.as_view()), name='update_news'),
    url(r'^eliminar-noticia/(?P<pk>\d+)/$', login_required(DeleteView.as_view(
        model=News, success_url='/noticias/')), name='delete_news'),
    #Categorias
    url(r'^categorias/$', login_required(ListView.as_view(template_name="categories.html", model=Category,
                                                          paginate_by=20)), name='categories'),
    url(r'^agregar-categoria/$', login_required(CreateView.as_view(
        model=Category, form_class=CategoryForm, template_name="category_form.html", success_url='/categorias/')),
        name='create_category'),
    url(r'^modificar-categoria/(?P<pk>\d+)/$', login_required(UpdateView.as_view(
        model=Category, form_class=CategoryForm, template_name="category_form.html", success_url='/categorias/')),
        name='update_category'),
    url(r'^eliminar-categoria/(?P<pk>\d+)/$', login_required(DeleteView.as_view(
        model=Category, success_url='/categorias/')), name='delete_category'),
    #Eventos
    url(r'^eventos/$', login_required(ListView.as_view(template_name="events.html", model=Event,
                                                       paginate_by=20)), name='events'),
    url(r'^agregar-evento/$', login_required(EventCreate.as_view()), name='create_event'),
    url(r'^modificar-evento/(?P<pk>\d+)/$', login_required(UpdateView.as_view(
        model=Event, form_class=EventForm, template_name="event_form.html", success_url='/eventos/')),
        name='update_event'),
    url(r'^eliminar-evento/(?P<pk>\d+)/$', login_required(DeleteView.as_view(
        model=Event, success_url='/eventos/')), name='delete_event'),
    #Productos
    url(r'^productos/$', login_required(ListView.as_view(template_name="products.html", model=Product,
                                        paginate_by=20)), name='products'),
    url(r'^agregar-producto/$', login_required(ProductCreate.as_view()), name='create_product'),
    url(r'^modificar-producto/(?P<pk>\d+)/$', login_required(UpdateView.as_view(
        model=Product, form_class=ProductForm, template_name="product_form.html", success_url='/productos/')),
        name='update_product'),
    url(r'^eliminar-producto/(?P<pk>\d+)/$', login_required(DeleteView.as_view(
        model=Product, success_url='/productos/')), name='delete_product'),
    url(r'^productos/clasificaciones/$', login_required(ClassificationList.as_view()), name='classifications'),
    #Clasificaciones
    url(r'^agregar-clasificacion/$', 'core.views.add_classification', name='add_classification'),
    url(r'^modificar-clasificacion/(?P<pk>\d+)/$', 'core.views.save_classification', name='save_classification'),
    url(r'^eliminar-clasificacion/(?P<pk>\d+)/$', 'core.views.delete_classification', name='delete_classification'),
    url(r'^sincronizar-clasificacion/$', 'core.views.synchronize_classification', name='synchronize_classification'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^summernote/', include('django_summernote.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
