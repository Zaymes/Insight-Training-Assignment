from django.urls import path

from .views import render_landing_page, render_detail, render_blogs_list

urlpatterns = [
    path('', render_landing_page),
    path('bloglist/', render_blogs_list),
    path('detail/<int:blog_id>',render_detail)
]


