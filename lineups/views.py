from django.shortcuts import render

# Create your views here.
from .models import Player, Position


# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page
def index(request):
    num_players = Player.objects.all().count()
    players = Player.objects.all()

    context = {
        'num_players': num_players,
        'players': players,
    }

    return render(request, 'index.html', context=context)


def lineups(request):
    num_players = Player.objects.all().count()
    players = Player.objects.all()
    # Logic to create generated lineup
    generated_lineup = Player.objects.all()[:6]

    # ensure one hitter, one middle blocker, one setter, and one libero
    # FUN BUSINESS LOGIC

    context = {
        'num_players': num_players,
        'generated_lineup': generated_lineup,
        'players': players,
    }

    return render(request, 'lineups.html', context=context)
