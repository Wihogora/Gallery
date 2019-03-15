from django.conf.urls import url
from . import views

#.........
urlpatterns=[
    #......
    url('^today/$',views.galery_of_day,name='galeryToday')
]