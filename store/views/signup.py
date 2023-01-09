from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from store.models.user import User
from django.contrib.auth.hashers import make_password

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        data = request.POST
        uname = data.get('uname')
        uemail = data.get('uemail')
        uaddress = data.get('uaddress')
        ugender = data.get('ugender')
        upassword = data.get('upassword')
        condition = data.get('condition')
        err_msg = None
        newuser = User(uname=uname,
                       uemail=uemail,
                       uaddress=uaddress,
                       ugender=ugender,
                       upassword=upassword,
                       condition=condition)

        emailvalid = newuser.isvalid()
        if emailvalid:
            err_msg = "Enter valid email"
        elif len(uname) < 4:
            err_msg = "Invalid name length"
        elif len(uaddress) < 10:
            err_msg = "Please enter proper address"
        elif len(upassword) < 6:
            err_msg = "Password length should greater then 5"

        if err_msg is None:
            newuser.upassword = make_password(newuser.upassword)
            newuser.register()
            return redirect('homepage')
        else:
            return render(request, 'signup.html', {'err_msg': err_msg})
