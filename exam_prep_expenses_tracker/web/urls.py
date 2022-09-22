from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from exam_prep_expenses_tracker.web import views

urlpatterns = [
    path('', views.show_home),

    path('create/', views.create_expense),
    path('edit/<int:pk>/', views.edit_expense),
    path('delete/<int:pk>/', views.delete_expense),

    path('profile/', views.show_profile),
    path('profile/create/', views.create_profile),
    path('profile/edit/', views.edit_profile),
    path('profile/delete/', views.delete_profile)

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
