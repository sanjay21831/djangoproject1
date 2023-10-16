from django.contrib import admin
from django.urls import path
from curdapp import views
urlpatterns = [
    path("homepage/",views.homepage,name='homepage'),
    path('admin/', admin.site.urls),
    path('add_student',views.add_student,name="add_student"),
    path('update_student/<id>',views.update_student,name="update_student"),
    path('delete_student/<id>',views.delete_student,name='delete_student')
]
