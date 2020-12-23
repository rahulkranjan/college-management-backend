from django.urls import path
from .views import *


urlpatterns = [
    path('college', CollegeAPIView.as_view()),
    path('college/<int:id>/', CollegeAPIView.as_view()),
    path('branches', BranchAPIView.as_view()),
    path('branches/<int:id>/', BranchAPIView.as_view()),
    # path('homeslide', HomeSlideAPIView.as_view()),



]
