from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.TodoList.as_view(), name='list'),
    path('create/', views.TodoCreate.as_view(), name='create'),
    path('detail/<int:pk>/', views.TodoDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.TodoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.TodoDelete.as_view(), name='delete'),
]
