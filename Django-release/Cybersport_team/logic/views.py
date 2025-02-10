from django.shortcuts import render

# Create your views here.
def menu_context():
    return {
        'main': 'Главная',
        'team': 'Команда',
        'club': 'О клубе',
        'blog': 'Блог'
    }

def main_page(request):
    context = {
        'main': 'Главная',
        'team': 'Команда',
        'club': 'О клубе',
        'blog': 'Блог',
        'shop': 'Магазин'
    }
    return render(request, 'html-templates/main_page.html', context)

def team_page(request):
    context = {
        'cs2': 'CS2',
        'dota': 'DOTA 2'
    }
    return render(request, 'html-templates/team_page.html', context)

def club_page(request):
    return render(request, 'html-templates/club_page.html')

def blog_page(request):
    return render(request, 'html-templates/blog.html')