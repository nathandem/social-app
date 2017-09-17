from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from django.views import generic
from django.http import Http404

from braces.views import SelectRelatedMixin

from . import models
from . import forms

# a way to get attrib from the User object, when one is logged-in
from django.contrib.auth import get_user_model
User = get_user_model()


class PostList(SelectRelatedMixin,generic.ListView):
    model = models.Post
    select_related = ('user','group')


class UserPosts(generic.ListView):
    model = models.Post
    template_name = 'post/user_post_list.html'

    def get_queryset(self):
        try:
            # post_user is a normal var we assign as attribute to self
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
            # username is a field of the User built-in model
            # prefetch_related takes data from the relationship ; more here: https://stackoverflow.com/questions/31237042/whats-the-difference-between-select-related-and-prefetch-related-in-django-orm
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class PostDetail(SelectRelatedMixin,generic.DetailView):
    model = models.Post
    # select_related caches foreignkeys of an object so that we don't have to hit the DB twice when we want to get object in the ForeignKey
    select_related = ('user','group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
        # seems like it's implicit that the queryset is on Post


class CreatePost(LoginRequiredMixin,SelectRelatedMixin,generic.CreateView):
    fields = ('message','group')
    model = models.Post

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeletePost(LoginRequiredMixin,SelectRelatedMixin,generic.DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)
