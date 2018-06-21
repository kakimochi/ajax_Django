from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test_ajax_response(request):
    input_text = request.POST.getlist("name_input_text")
    hoge = "Ajax Response: " + input_text[0]

    return HttpResponse(hoge)

def test_ajax_app(request):
    hoge = "Hello Django!!"

    return render(request, "test_ajax_app/test_ajax_app.html", {
        "hoge": hoge,
    })
