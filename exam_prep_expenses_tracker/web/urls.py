from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from exam_prep_expenses_tracker.web import views

urlpatterns = [
    path('', views.show_home, name='home'),

    path('create/', views.create_expense, name='create expense'),
    path('edit/<int:pk>/', views.edit_expense, name='edit expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete expense'),

    path('profile/', views.show_profile, name='show profile'),
    path('profile/create/', views.create_profile, name='create profile'),
    path('profile/edit/', views.edit_profile, name='edit profile'),
    path('profile/delete/', views.delete_profile, name='delete profile')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
