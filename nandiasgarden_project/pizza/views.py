from django.shortcuts import render
from .forms import PizzaForm

# Create your views here.
def home(request):
	return render(request, 'home.html')

def order(request):
	if request.method == 'POST':
		filled_form = PizzaForm(request.POST)
		if filled_form.is_valid():
			note = 'Thanks for Ordering %s %s %s Pizza' %(filled_form.cleaned_data['topping1'],
				filled_form.cleaned_data['topping2'],
				filled_form.cleaned_data['size'],)
			new_form = PizzaForm()
			return render(request, 'order.html', {'pizzaform':new_form, 'note':note})
	else:	
		form = PizzaForm()
		return render(request, 'order.html', {'pizzaform':form})
