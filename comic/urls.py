from django.urls import path

from comic.views import ComicsView

urlpatterns = [
    path('',ComicsView.as_view(), name='comics'),
]
