from django.db import models

class AdminUserManager(models.Manager):
    def get_queryset(self):
        return super(AdminUserManager, self).get_queryset().filter(type='admin')


class ReviewerUserManager(models.Manager):
    def get_queryset(self):
        return super(ReviewerUserManager, self).get_queryset().filter(type='reviewer')

class AuthorUserManager(models.Manager):
    def get_queryset(self):
        return super(ReviewerUserManager, self).get_queryset().filter(type='author')
