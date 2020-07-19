from django.shortcuts import render, get_object_or_404

from .models import BlogPost

# Create your views here.

def render_landing_page(request):
    return render(request, 'blog/landing.html')


def render_blogs_list(request):
    data = BlogPost.objects.all()
    context ={
        'data': data
    }
    return render(request, 'blog/blogs.html', context=context)


def render_detail(request, blog_id):
    blog_obj = get_object_or_404(BlogPost, id=blog_id)
    return render(request, 'blog/detail.html',context={'blog_obj':blog_obj})
