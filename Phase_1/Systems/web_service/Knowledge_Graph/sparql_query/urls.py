from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
    # url(r'^output/(?P<text>\w+)/$',views.index, name='index'))

]
