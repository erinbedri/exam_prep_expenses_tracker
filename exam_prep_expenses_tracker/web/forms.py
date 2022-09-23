from django import forms

from exam_prep_expenses_tracker.web.models import Expense, Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')


class CreateExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')