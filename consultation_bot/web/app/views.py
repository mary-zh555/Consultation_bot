from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


menu = {
    "Зв'язатись з менеджером": "manager",
    "Підібрати подарунок": "praktyka",
    "Повернення товару": "praktyka",
    "Підібрати товар": "product",
    "Нормальна практика": "praktyka",
}


def index(request):
    list_items = ""
    options = list(menu.keys())
    for option in options:
        capitalised_action = option.capitalize()
        option_path = reverse("menu-firstchoice", args=[option])
        list_items += f'<li><a href="{option_path}">{capitalised_action}</a></li>'
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def web_by_num(request, option):
    options = list(menu.keys())
    if option > len(options):
        return HttpResponseNotFound("Invalid")
    redirect_option = options[option - 1]
    redirect_path = reverse("menu-firstchoice", args=[redirect_option])
    return HttpResponseRedirect(redirect_path)


def web(request, option):
    try:
        text = menu[option]
        response_data = f"<h1>{text}</h1>"
    except:
        return HttpResponseNotFound("<h1>This option is not supported</h1>")
    return HttpResponse(response_data)
