from django.shortcuts import render

from django.contrib.auth import get_user_model

User = get_user_model()

def register_view(request):
    print(request.POST)
    if request.method == "POST":
        username = request.POST.get("username") or None
        email = request.POST.get("email") or None
        password = request.POST.get("password") or None
        # Django Forms
        # username_exist = User.objects.filter(username__iexact=username).exists()
        # email_exist = User.objects.filter(email__iexact=email).exists()
        try:
            User.objects.create_user(
                username,
                email=email,
                password=password
            )
        except:
            pass
    return render(request, "auth/register.html", {})