from django.shortcuts import render, HttpResponse
from home.models import Student


# Create your views here.
def index(request):
    return render(request, "index.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        contact = request.POST["contact"]
        password = request.POST["password"]
        ins = Student(name=name, email=email, contact=contact, password=password)
        ins.save()
        print("The Data has been saved into your Database")
    return render(request, "contact.html")


def delete(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        Student.objects.filter(name=name, email=email, password=password).delete()
        print("The Data has been Deleted from your Database")
    return render(request, "delete.html")


def search(request):
    ans = None
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        if name and email:
            ans = Student.objects.filter(name=name, email=email)
    
    return render(request, "search.html", {"data": ans})


def update(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        old_password = request.POST["old_password"]
        new_password = request.POST["new_password"]
        Student.objects.filter(name=name, email=email, password=old_password).update(
            password=new_password
        )
        print("The Data Has been Successfully Updated")

    return render(request, "update.html")


# Show Data
def show(request):
    data = Student.objects.all()
    return render(request, "show_data.html",{"datas" :data})
































'''
# Fetch data from database(R)
def getdata(request):
    data = Contact.objects.all()

    # Method - 1
    # data1 = Contact.objects.filter(name="Lokesh Singh", password="1234")

    # Method- 2
    data1 = Contact.objects.all().filter(name="Lokesh Singh", password="1234")
    return render(request, "get_data.html", {"data": data, "data1": data1})
'''