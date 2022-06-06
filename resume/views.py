from django.shortcuts import render

def home(request):
    from resume.names import myname
    names = ["Lucas", "Lasse", "Rasmus", "Simon"]
    return render(request, "home.html", {'names': names, 'myname': myname})

def about(request):
    f_name = "Lucas"
    l_name = "sandby"
    return render(request, "about.html", {'first_name': f_name, 'last_name': l_name})

def resume(request):
    return render(request, "resume.html", {})
