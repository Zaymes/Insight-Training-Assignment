from django.urls import path

from .views import List, Detail

app_name = 'blog'
urlpatterns =[
    path('blog/', List.as_view(), name='blog-home'),
    path('detail/<int:id>', Detail.as_view(), name='blog-detail')
]