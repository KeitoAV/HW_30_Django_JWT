from django.conf.urls.static import static

from django.urls import path

from HW_30_Django_JWT import settings
from ads.views.category import *
from ads.views.ad import *
from ads.views.selection import *

urlpatterns = [

    path("", root),

    path('ad/', AdListView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('ad/<int:pk>/upload_image/', AdImageView.as_view()),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view()),
    path('ad/create/', AdCreateView.as_view()),

    path('cat/', CategoryListView.as_view()),
    path('cat/<int:pk>/', CategoryDetailView.as_view()),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view()),
    path('cat/create/', CategoryCreateView.as_view()),

    path('selection/', SelectionListView.as_view()),
    path('selection/<int:pk>/', SelectionDetailView.as_view()),
    path('selection/create/', SelectionCreateView.as_view()),
    path('selection/<int:pk>/delete/', SelectionDeleteView.as_view()),
    path('selection/<int:pk>/update/', SelectionUpdateView.as_view()),

]

# images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
