import os

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from exam_prep_expenses_tracker.web.forms import CreateExpenseForm, CreateProfileForm, EditExpenseForm, \
    DeleteExpenseForm, EditProfileForm, DeleteProfileForm
from exam_prep_expenses_tracker.web.models import Profile, Expense


def get_profile():
    profile = Profile.objects.all().first()
    return profile


def show_home(request):
    profile = get_profile()

    if profile:
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
    if request.method == 'POST':
        form = CreateExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateExpenseForm()

    context = {
        'form': form
    }

    return render(request, 'expense-create.html', context)


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form
    }

    return render(request, 'expense-edit.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'POST':
        form = DeleteExpenseForm(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            expense.delete()
            return redirect('home')
    else:
        form = DeleteExpenseForm(instance=expense)

    context = {
        'expense': expense,
        'form': form,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()

    if profile:
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
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }
    return render(request, 'home-no-profile.html', context)


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST' and profile:
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()

    if request.method == 'POST' and profile:
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            image_path = profile.image.path
            os.remove(image_path)
            profile.delete()
            expenses.delete()
            return redirect('home')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }

    return render(request, 'profile-delete.html', context)
