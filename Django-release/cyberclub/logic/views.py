from django.shortcuts import render

# Create your views here.

def menu():
    context = {
        "main": "Главная",
        "club": "О клубе",
        "team": "Команда",
        "blog": "Блог",
    }
    return context

def menu_page(request):
    return render(request, "html-templates/menu.html", menu())

def main_page(request):
    return render(request, "html-templates/main_page.html", menu())

def club_page(request):
    return render(request, "html-templates/club_page.html", menu())

def team_page(request):
    return render(request, "html-templates/team_page.html", menu())
