from django.urls import path
from django.conf.urls import url
from myapp import views


urlpatterns = [
    path('', views.index, name='homepage'),
    path('addpost/', views.addpost, name='add post'),
    path('upvote/<int:id>/', views.upvote),
    path('downvote/<int:id>/', views.downvote),
    path('boasts/', views.boast_posts, name='boasts'),
    path('roasts/', views.roast_posts, name='roasts'),
    path('votes/', views.vote_posts, name='votes'),
    path('post/<int:id>/', views.post_info, name="post info"),
    url(r'^(?P<id>\w+)/delete/$', views.posts_delete_view, name='delete'),
    # path('post_success/', views.post_success, name="post success")
]
