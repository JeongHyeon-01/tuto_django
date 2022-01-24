from re import template
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
# Create your views here.

class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html'
    ordering = '-pk'
'''
 FBV 로 작성한 문서 (아래)
'''
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         'blog/index.html',{
#             'posts':posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)

#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post':post,
#         }
#     )