from django.shortcuts import render
from django.http import Http404

from blog.models import Post

"""
Function for customised rendering of posts. But how does Django know when
to use this??
"""
def post_list_view(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail_view(request, post_id):
    # Or use get_object_or_404() but the function name is ugly
    try:
        post = Post.published.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Post(id={0}) not found".format(post_id))
    
    return render(request, 'blog/post/detail.html', {'post': post})