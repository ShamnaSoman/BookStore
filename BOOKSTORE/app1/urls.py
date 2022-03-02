from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('home' , views.home ,name='home') ,
    path('add' ,views.add , name='add'),
    path('list',views.list , name='list'),
    path('delete/<int:id>',views.delete ,name='delete'),
    path('update/<int:id>',views.update , name='update'),
    path('online/<int:id>',views.online,name='online'),
    path('buy',views.buy,name="buy"),
    path('success',views.success,name='success'),
    path('image', views.image, name='image'),
    path('success', views.successful, name = 'success'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
