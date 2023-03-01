from django.urls import path
from . import views

app_name = 'quoteapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
    path('quote/', views.quote, name='quote'),
    path('authoradd/', views.author, name='author'),
    path('detail/<int:quote_id>', views.detail, name='detail'),
    path('delete/<int:quote_id>', views.delete_quote, name='delete'),
    path("author/<str:fullname>", views.author_page, name="author"),
]
