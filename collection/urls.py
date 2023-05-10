from django.urls import path

from collection.views import CollectionsView
from collection.views import ComicCollectionView

urlpatterns = [
    path('', CollectionsView.as_view(), name='collections'),
    path('<slug:collection_slug>/', ComicCollectionView.as_view(), name='comic-collections'),
]
