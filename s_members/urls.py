from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.member_list, name='member_list'),
    path('members/create/', views.member_create, name='member_create'),
    path('members/update/<int:pk>/', views.member_update, name='member_update'),
    path('members/delete/<int:pk>/', views.member_delete, name='member_delete'),
    path("stepper-onboarding/", views.stepper_form_view, name="stepper_form"),

    # path('groups/', views.group_list, name='group_list'),
    # path('groups/create/', views.group_create, name='group_create'),
    # Additional URLs for group update and delete similar to member_update and member_delete
]
