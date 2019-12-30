import datetime
# Create your views here.

# def index(request):
#     context = {
#         'title':'Just a title',
#         'des':'Just a descriton',
#         'score':'1.0'
#     }
#     return render(request, "index.html",context)

from django_web import models
from django.shortcuts import render
from django.shortcuts import redirect


# def insert(request):
#     user_id = request.POST.get("id", None)
#     user_name = request.POST.get("name", None)
#     test1 = models.MariadbTest.objects.create(user_id=id, user_name=name)
#     test1.save()
#     return render(request, 'index.html',)

def login(request):
    error_msg = ""
    if request.method == "POST":
        userName = request.POST.get('userName', None)
        userPass = request.POST.get('userPass', None)
        if userName == 'root' and userPass == 'yunzx@123':
            return redirect('/table/')
        else:
            error_msg = '用户或密码错误'
    return render(request, 'login.html', {'error_msg': error_msg})


def table_operate(request):
    if request.method == "POST":
        ip_address = request.POST.get("ip_address")
        server_location = request.POST.get("server_location")
        create_time = models.servertest.create_time
        update_time = models.servertest.update_time
        models.servertest.objects.create(
            ip_adress=ip_address,
            server_location=server_location,
            create_time=create_time,
            update_time=update_time,
        )
        print(ip_address, server_location, create_time, update_time)
    people_list = models.servertest.objects.all()
    return render(request, 'index.html', {"people_list": people_list})

# def create(request):
#
#         return render(request, "index.html", locals())
