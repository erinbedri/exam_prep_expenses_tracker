from django.shortcuts import render, redirect

from exam_prep_expenses_tracker.web.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all()
    return profile


def show_home(request):
    profile = get_profile()

    if profile:
        profile = profile[0]
        budget = profile.budget
        expenses = Expense.objects.all()
        budget_left = budget - sum(e for e in expenses)
        context = {
            'budget': budget,
            'expenses': expenses,
            'budget_left': budget_left,
        }
        return render(request, 'home-with-profile.html', context)
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
