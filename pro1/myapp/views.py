from django.shortcuts import render
from django.http import HttpResponse
#from .models import Jp
# Create your views here.

def index(request):
	"""if requests.method == 'POST':
        name = requests.POST.get('name')
        email = requests.POST.get('email')
        message = requests.POST.get('message')

        ent = Jp(name=name,email=email,message=message)
        ent.save()

        msg = "\n\nName is :- " + name + "\n\nEmail is :- " + email + "\n\nMessage is :- " + message

        from django.core.mail import send_mail

        send_mail(
            'New Enquiry - CV',
            msg,
            'pateljineshkumar.imscit20@gmail.com',
            ['pateljineshkumar.imscit20@gmail.com'],
            fail_silently=False,
        )

    else:
        pass"""

	return render(request,'index.html')