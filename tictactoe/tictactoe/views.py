from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home')
        # return render(request, 'player/home.html')
    else:
        return render(request, 'tictactoe/welcome.html')
