from django.shortcuts import render, get_object_or_404
from blog.models import Post

def home(request):

    # postlar = Post.objects.all()

    yayinlanmis_postlar = Post.objects.filter(yayinla=True)


    context = {
        'postlar' : yayinlanmis_postlar
    }
    return render(request, 'blog_list.html', context)

def post_detay(request, post_link):
    # post = Post.objects.get(link =post_baslik, yayinla=True)

    post = get_object_or_404(Post, link=post_link, yayinla=True)

    context = {
        'post' : post
    }
    return render(request, 'blog_detay.html', context)

# def post(request, post):
#     post_detay = Post.object.get()