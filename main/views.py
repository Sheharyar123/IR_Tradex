from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .forms import ContactForm
from .utils import send_contact_email


class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm
        context = {"form": form}
        return render(request, "main/index.html", context)

    def post(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
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
                send_contact_email(mail_subject, mail_template, context)
                return JsonResponse({"status": "success"})

        return JsonResponse({"status": "failed"})
