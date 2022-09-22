from django.shortcuts import render, redirect

from exam_prep_expenses_tracker.web.models import Profile


def get_profile():
    profile = Profile.objects.all()
    return profile


def show_home(request):
    profile = get_profile()

    if profile:
        return render(request, 'home-with-profile.html')
    else:
        return redirect('create profile')


def create_expense(request):
    return render(request, 'expense-create.html')


def edit_expense(request):
    return render(request, 'expense-edit.html')


def delete_expense(request):
    return render(request, 'expense-delete.html')


def show_profile(request):
    return render(request, 'profile.html')


def create_profile(request):
    return render(request, 'home-no-profile.html')


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, 'profile-delete.html')
