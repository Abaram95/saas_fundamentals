from django.shortcuts import render

from visits.models import PageVisit

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    my_title = "SaaS"
    my_context = {
        "page_title": my_title,
        "queryset": queryset.count()

    }
    http_template = "base.html"
    PageVisit.objects.create()
    return render(request, http_template, my_context)