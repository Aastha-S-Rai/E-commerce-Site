from django.db import models


class User(models.Model):
    uname = models.CharField(max_length=30)
    uemail = models.EmailField()
    uaddress = models.CharField(max_length=100)
    ugender = models.CharField(max_length=10, default="other")
    upassword = models.CharField(max_length=30)
    condition = models.IntegerField(default=0)

    def register(self):
        self.save()

    def isvalid(self):
        if User.objects.filter(uemail=self.uemail).filter(upassword=self.upassword):
            return True
        else:
            return False

    @staticmethod
    def email_login(email):
        try:
            return User.objects.get(uemail=email)
        except:
            return False

