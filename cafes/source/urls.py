from django.urls import path
from .views import * 

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('cafes/', CafeList.as_view(), name='cafe'),
    path('add-cafe/', AddCafe.as_view(), name='addcafe'),
    # path('edit-cafe/<int:pk>', UpdateCafe.as_view(), name='update'),
]
