from django.urls import path


from . import views


urlpatterns = [
    path("", views.index_view, name="index_view"),
    path("<int:month>", views.monthly_challenge_view_by_num),
    path("<str:month>", views.monthly_challenge_view, name="monthly-challenge")
]
