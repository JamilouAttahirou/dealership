from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Car, Photo, Financing, Message, User
from .forms import CarForm, FinancingForm, MessageForm, MyUserCreationForm
from .forms import PhotoFormSet

# Create your views here.


# View for login Page
def loginPage(request):
    page = 'login';

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
           messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
           login(request, user)
           return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist')

    context = {'page': page}
    return render(request, 'user/login_register.html', context)


# views for the logout
def logoutUser(request):
    logout(request)
    return redirect('home')

# View for register page
def registerPage(request):
    registration_form = MyUserCreationForm()

    if request.method == 'POST':
        registration_form = MyUserCreationForm(request.POST)
        if registration_form.is_valid():
            user = registration_form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'registration_form': registration_form}    
    return render(request, 'user/login_register.html', context)



# View for the home page
def home(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'user/home.html', context)


# View for the inventory room
def inventory(request):
    cars = Car.objects.all()

    # filter car by year if selected
    year = request.GET.get('year')
    if year:
        cars = cars.filter(year=year)
    
    # filter car by make if selected
    make = request.GET.get('make')
    if make:
        cars = cars.filter(make=make)

    # filter car by model if selected
    model = request.GET.get('model')
    if model:
        cars = cars.filter(model__icontains=model)

    # filter car by price if selected
    price = request.GET.get('price')
    if price:
        if price == 'Under $5k':
            cars = cars.filter(price__lt=5000)
        elif price == '$5000-$10000':
            cars = cars.filter(price__gte=5000, price__lt=10000)
        elif price == '$10000-$19999':
            cars = cars.filter(price__gte=10000, price__lt=20000)
        elif price == '$20000-$29999':
            cars = cars.filter(price__gte=20000, price__lt=30000)
        elif price == '$30000-$39999':
            cars = cars.filter(price__gte=30000, price__lt=40000)
        elif price == '$40000-$49999':
            cars = cars.filter(price__gte=40000, price__lt=50000)
        elif price == '$50000-$59999':
            cars = cars.filter(price__gte=50000, price__lt=60000)

    context = {'cars':cars}
    return render(request, "user/inventory.html", context)


# View for the inventory car
def car(request, car_id):
    car = Car.objects.get(id=car_id)

    if request.method == 'POST':
        formset = PhotoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data: # Only save if the form has data
                    photo = form.save(commit=False)
                    photo.car = car
                    photo.save()
            return redirect('car', car_id=car.id) # Redirect to the car detail page
    else:
        formset = PhotoFormSet(queryset=Photo.objects.none()) # Empty formset  or objects.fiter(car=ar) to show already upload pics

    context = {'car': car, 'formset': formset}
    return render(request, 'user/car.html', context)


# View for the service room
def service(request):
    return render(request, "user/service.html")


# View to create financing applications in financing room
def financing_room(request):
    financing_form = FinancingForm()

    if request.method == 'POST':
        financing_form = FinancingForm(request.POST)
        if financing_form.is_valid():
            financing_form.save()
            # return redirect('financing')
            return render(request, "user/financingRoom.html", {
                "financing_form": FinancingForm(),  # empty form
                "popup": True  # flag to show the popup
            })
        
    context = {'financing_form': financing_form}
    return render(request, "user/financingRoom.html", context)

# View for all financing applications
def all_financing_applications(request):
    financings = Financing.objects.all()
    print(financings)  # Check if any records are returned
    context = {'financings': financings}
    return render(request, "user/allFinancingApplications.html", context)

# View for a single financing application
def financing_application(request, pk):
    financing = Financing.objects.get(id=pk)
    context = {'financing': financing}
    return render(request, "user/financingApplication.html", context)


# View to create meassage in contact room
def contact(request):
    message_form = MessageForm()

    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            message_form.save()
            # return redirect('contact')
            return render(request, "user/contact.html", {
                "message_form": MessageForm(),  # empty form
                "popup": True  # flag to show the popup
            })
        
    context = {'message_form': message_form}
    return render(request, "user/contact.html", context)

# View for all messages
def all_messages(request):
    messages = Message.objects.all()
    context = {'messages': messages}
    return render(request, "user/allMessages.html", context)


# View for a single message
def message(request, pk):
    message = Message.objects.get(id=pk)
    context = {'meassage': message}
    return render(request, "user/message.html", context)
    return render(request, "user/message.html", context)




# View for the 'About Us' room
def aboutUs(request):
    return render(request, "user/aboutUs.html")


# View for the homepage
def direction(request):
    context = {}
    return render(request, 'user/direction.html', context)


# View for the cover images section room
def carSearchBar(request):
    return render(request, "user/carSearchBar.html")

# View for the cover images section room
def coverPageImages(request):
    return render(request, "user/coverPageImages.html")

# View for the display room
def display(request):
    return render(request, "user/display.html")


# View for the info room
def info(request):
    return render(request, "user/info.html")


# View for the store_hours room
def store_hours(request):
    return render(request, "user/store_hours.html")


# View for creating car room
@login_required(login_url='home')
def createCarRoom(request):
    car_form = CarForm()

    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES)
        if car_form.is_valid():
            car_form.save()
            return redirect('inventory')

    context = {'car_form': car_form}
    return render(request, "user/car_form.html", context)


# View for updating car room
@login_required(login_url='home')
def updateCarRoom(request, car_id):
    car = Car.objects.get(id=car_id)
    car_form = CarForm(instance=car)

    if request.method == 'POST':
        car_form = CarForm(request.POST, request.FILES , instance=car)
        if car_form.is_valid():
            car_form.save()
            return redirect('inventory')

    context = {'car_form': car_form}
    return render(request, "user/car_form.html", context)


#view for deleting car room
@login_required(login_url='home')
def deleteCarRoom(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('inventory')
    
    return render(request, 'user/delete.html', {'obj': car})