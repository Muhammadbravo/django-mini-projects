from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Post

# all_posts = [
#     {
#         "slug": "first-world",
#         "title": "First World!",
#         "image": "dp.jpeg",
#         # "image": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
#         "author": "Musa Doe",
#         "date": date(2022, 3, 7),
#         "excerpt": "Lorem ipsum dolor",
#         "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
#     },
#     {
#         "slug": "second-world",
#         "title": "Second World!",
#         "image": "dp.jpeg",
#         # "image": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
#         "author": "Anas Doe",
#         "date": date(2022, 3, 17),
#         "excerpt": "Lorem ipsum dolor sit amet,",
#         "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
#     },
#     {
#         "slug": "third-world",
#         "title": "Third World!",
#         "image": "dp.jpeg",
#         # "image": "https://images.unsplash.com/photo-1518791841217-8f162f1e1131?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60",
#         "author": "John Bravo",
#         "date": date(2022, 3, 14),
#         "excerpt": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#         "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
#     }
# ]



# Create your views here.
def index(request):
    latest_post = Post.objects.all().order_by('-date')[:3]
    # sorted_post = sorted(all_posts, key=lambda k: k['date'])
    # latest_post = sorted_post[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_post,
    }) 

def posts(request):
    all_posts =  Post.objects.all().order_by("-date")
    return render(request, 'blog/posts.html', {
        "all_post": all_posts,
    })

def view_post(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    # identified_post = [post for post in all_posts if post['slug'] == slug]
    return render(request, 'blog/post-detail.html', {
        "post": identified_post,
        'post_tags': identified_post.tags.all()
    })