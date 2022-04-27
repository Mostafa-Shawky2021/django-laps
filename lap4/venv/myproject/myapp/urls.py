from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('home/', views.home,name='home' ), # the third paramter is alias
    path('show/<std_id>', views.show,name='show' ), # std_id to hold the variable attached to url
    path('delete/<std_id>', views.delete,name='delete' ) # std_id to hold the variable attached to url

]