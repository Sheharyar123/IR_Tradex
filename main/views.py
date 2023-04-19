from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from .forms import ContactForm
from .utils import send_contact_email


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm
        context = {"form": form}
        return render(request, "main/index.html", context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            message = request.POST.get("message")
            context = {
                "message": message,
                "name": name,
                "email": email,
            }
            mail_subject = "Contact Email From IR Tradex"
            mail_template = "main/emails/send_contact_email.html"
            messages.success(request, "Your message was sent successfully!")
            send_contact_email(mail_subject, mail_template, context)
        else:
            messages.error(request, "There was a problem sending your email.")
        return redirect("home")
