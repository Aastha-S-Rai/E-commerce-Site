from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from store.models.user import User
from django.contrib.auth.hashers import make_password, check_password


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        data = request.POST
        uemail = data.get('uemail')
        upassword = data.get('upassword')
        details = User.email_login(uemail)
        err_msg = None
        if details:
            flag = check_password(upassword, details.upassword)
            if flag:
                request.session['user_id'] = details.id
                request.session['user_email'] = details.uemail
                request.session['user_name'] = details.uname
                return redirect('homepage')
            else:
                err_msg = "Incorrect Password !!!"
                return render(request, 'login.html', {'err_msg': err_msg})
        else:
            err_msg = "Invalid Email !!!"
            return render(request, 'login.html', {'err_msg': err_msg})


def logout(request):
    request.session.clear()
    return redirect('login')
