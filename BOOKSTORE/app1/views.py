from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Bookform
from .models import Books
import razorpay
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

price = 0
def home(request):
    return render(request,'Home.html')


def add(request):
    print(request.method)
    if request.method == 'POST':
        form = Bookform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = Bookform()
    return render(request,'Addbook.html',{'form':form})


def list(request):
    book = Books.objects.all()
    return render(request,'Booklist.html',{'book':book})


def delete(request,id):
    book = Books.objects.get(id=id)
    print('delete')
    book.delete()
    return redirect('/list')


def update(request,id):
    book = Books.objects.get(id=id)
    if request.method == 'POST':
        print(request.POST.get("qty"))
        book.Bstock = str(int(book.Bstock) + int(request.POST.get("qty")))
        book.save()
        return redirect('/list')
    else:
        form = Bookform()
    return render(request,'Bookedit.html',{'book':book})


def online(request,id):
    book = Books.objects.get(id=id)
    print(request.method)
    if request.method == 'POST':
        print('buying')
        price = int(book.Bprice) * int(request.POST.get("qty"))
        print(price)
        return redirect('/buy')

    return render(request,'Bookonline.html',{'book':book})


def buy(request):
    global price
    print(price)
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('price')

        client = razorpay.Client(
            auth=("rzp_test_KadYnmNZAFuKEg", "9mcPg3kEtzfcfALA5OTsiedi"))

        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request,'Transaction.html',)


@csrf_exempt
def success(request):
    return render(request, "Sucess.html")


def image(request):
    print('enter')
    if request.method == 'POST':
        form = Bookform(request.POST,request.FILES)
        if form.is_valid():
            print('$$$')
            form.save()
            return redirect('success')
    else:
        form = Bookform()
    return render(request, 'image.html', {'form':form})


def successful(request):
    return HttpResponse('successfully uploaded')


