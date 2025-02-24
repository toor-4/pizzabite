from django.shortcuts import render
from . models import Menu, Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    menu = Menu.objects.all()
    return render(request, 'pizza/index.html', {'menu': menu})

def about(request):
    return render(request, 'pizza/about.html')

def menu(request):
    menu = Menu.objects.all()
    return render(request, 'pizza/menu.html', {'menu': menu})

def menu_item(request,pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    
        return render(request, 'pizza/menu_item.html', {'menu_item': menu_item} )

def booking_form(request):
    form = ReservationForm() 
    success_message = None

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Booking successful! Thank you."  # Message to show
            form = ReservationForm()  # Reset the form to empty
            # return redirect("booking_form")  # Redirect to a success page
            return render(request, 'pizza/booking_form.html', {'form': form, 'success_message': success_message})

    context = {'form': form, 'success_message': success_message}

    if form.errors:
        print(form.errors)  # Print form errors to the console for debugging
    return render(request, 'pizza/booking_form.html', context)