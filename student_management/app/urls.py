from django.urls import path
from . import views
from .views import UpdateData  


urlpatterns = [
    path('', views.index, name='index'),
    path('allstudents/', views.Allstudent, name='allstudent'),
    path('insert',views.insertData,name="insertData"),
     path('update/<int:id>/', UpdateData, name='updateData'),
      path('delete/<id>',views.DeleteData,name="DeleteData"),
]
