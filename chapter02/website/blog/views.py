from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render

from .models import Post

PAGE = 3


# Create your views here.
def post_list(request):
    post_list = Post.published.all()

    # Pagination with 3 post per page
    paginator = Paginator(post_list, PAGE)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer get the first page.
        posts = paginator.page(1)
    except EmptyPage:
        # if page_number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)

    return render(
        request,
        'blog/post/list.html',
        {'posts': posts},
    )


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post found")

    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
