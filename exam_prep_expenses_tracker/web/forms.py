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


class EditExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')


class DeleteExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title', 'description', 'image', 'price')

    title = forms.CharField(
        disabled=True,
    )
    image = forms.URLField(
        disabled=True,
    )

    price = forms.FloatField(
        disabled=True,
    )

    description = forms.CharField(
        disabled=True,
    )


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('budget', 'first_name', 'last_name', 'image')


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()