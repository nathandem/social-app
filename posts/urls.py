from django.conf.urls import url
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$',views.PostList.as_view(),name='all'),
    url(r'^new/$',views.CreatePost.as_view(),name='create'),
    url(r'^by/(?P<username>[-\w]+)/$',views.UserPosts.as_view(),name='for_user'),
    # username is a parameter of the UserPosts view, it's one of the fields of the User model which is linked to the Post model
    # \d refers to digit
    # [...] means any character in bracket, \w means any word character (A-Za-z0-9_), - means dash, + (outside) means one of more times
    # so [-\w] means any word character and dash, one or N times
    url(r'^by/(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.PostDetail.as_view(),name='single'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeletePost.as_view(),name='delete'),
]
