
from django.urls import path
from . import views
app_name='mypcapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('mypc/<int:mypc_id>/',views.detail,name='detail'),
    path('add/',views.add_mypc,name='add_mypc'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
