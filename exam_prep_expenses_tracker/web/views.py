from django.contrib import messages
from django.shortcuts import render, redirect

from exam_prep_expenses_tracker.web.forms import CreateExpenseForm, CreateProfileForm, EditExpenseForm, \
    DeleteExpenseForm
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
        budget_left = budget - sum(e.price for e in expenses)

        context = {
            'budget': budget,
            'expenses': expenses,
            'budget_left': budget_left,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        return redirect('create profile')


def create_expense(request):
    context = {}

    if request.method == 'POST':
        form = CreateExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your expense was successfully added!')
        else:
            messages.error(request, 'Error saving data!')
        return redirect('home')

    form = CreateExpenseForm()

    context['form'] = form

    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    context = {
        'expense': expense
    }

    if request.method == 'POST':
        form = EditExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your expense was successfully edited!')
        else:
            messages.error(request, 'Error saving data!')
        return redirect('home')

    form = EditExpenseForm(instance=expense)

    context['form'] = form

    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    context = {
        'expense': expense
    }

    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, request.FILES, instance=expense)

        if form.is_valid():
            expense.delete()
            messages.success(request, 'Your expense was successfully deleted!')
        else:
            messages.error(request, 'Error deleting data!')
        return redirect('home')

    form = DeleteExpenseForm(instance=expense)

    context['form'] = form
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()

    if profile:
        profile = profile[0]

        budget = profile.budget
        expenses = Expense.objects.all()
        items_count = len(expenses)
        budget_left = budget - sum(e.price for e in expenses)

        context = {
            'profile': profile,
            'budget': budget,
            'expenses': expenses,
            'budget_left': budget_left,
            'items_count': items_count,
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('create profile')


def create_profile(request):
    context = {}

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully created!')
        else:
            messages.error(request, 'Error saving data!')
        return redirect('home')

    form = CreateProfileForm()

    context['form'] = form

    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    return render(request, 'profile-edit.html')


def delete_profile(request):
    return render(request, 'profile-delete.html')
