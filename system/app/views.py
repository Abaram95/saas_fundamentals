from django.shortcuts import render

from visits.models import PageVisit

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)
   
def about_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    my_title = "SaaS"
    my_context = {
        "page_title": my_title,
        "queryset": qs.count(),
        "page_count": page_qs.count()

    }
    http_template = "base.html"
    PageVisit.objects.create(path = request.path)

    return render(request, http_template, my_context)
