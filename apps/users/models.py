from django.db import models

from werkzeug.security import check_password_hash


class User(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=100)
    addtime = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.name

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)
