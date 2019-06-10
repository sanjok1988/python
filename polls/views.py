from django.shortcuts import render

# Create your views here.
def poll_view(request):
    return render(request, "polls/index.html", {})