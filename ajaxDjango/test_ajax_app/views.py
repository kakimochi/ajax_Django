from django.shortcuts import render
from django.http import HttpResponse

import json

# Create your views here.
def test_ajax_response(request):
    # input_text = request.POST.getlist("name_input_text")
    # hoge = "Ajax Response: " + input_text[0]

    # json response
    data_dic = {
        "data": [
            ["Tiger Nixon", "System Architect", "Edinburgh", "5421", "2011/04/25", "$320,800"],
            ["Garrett Winters", "Accountant", "Tokyo", "8422", "2011/07/25", "$170,750"],
            ["Ashton Cox", "Junior Technical Author", "San Francisco", "1562", "2009/01/12", "$86,000"],
        ]
    }

    # data_dic = {
    #     "tr1": {
    #         "td1-1": "1-1",
    #         "td1-2": "1-2"
    #     },
    #     "tr2": {
    #         "td2-1": "2-1",
    #         "td2-2": "2-2"
    #     },
    #     "tr3": {
    #         "td3-1": "3-1",
    #         "td3-2": "3-2"
    #     }
    # }

    data = json.dumps(data_dic)

    return HttpResponse(data)
    # return HttpResponse(hoge)

def test_ajax_app(request):
    hoge = "Hello Django!!"

    return render(request, "test_ajax_app/test_ajax_app.html", {
        "hoge": hoge,
    })
