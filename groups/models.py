from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.core.urlresolvers import reverse
# slugify allows to use str with spaces in our urls by replacing them with special caracters

import misaka # to use markdown in the posts

from django.contrib.auth import get_user_model
User = get_user_model() # call attributes from the current session

from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=128,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name

    # I guess save() is a special method always run when saving an object in a model and we're just partially overwriting it now
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    # that's like success_url but drier
    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    # basically, Metas in models are like extra-args for the model
    # all meta options: https://docs.djangoproject.com/en/1.11/ref/models/options/
    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships')
    # the related_name should be in plurial, because it's at "many" side of the OneToMany relation
    user = models.ForeignKey(User,related_name="user_groups")
    # seems like we can create relation in whatever app has been set up (here, User is not in this app)
    # impressive that GroupMember is sort of dynamically linked to User model, once the user is logged-in!

    def __str__(self):
        return self.user.username
        # username is a field from the user model (power of relation dbs!)
        # we can call the One side of the OneToMany relation just by writing down its name

    class Meta:
        unique_together = ('group','user')
