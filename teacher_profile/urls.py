from django.conf.urls import url

# from teacher_profile.views import
from teacher_profile.views import TeacherOnboarding

urlpatterns = [
    url(r'onboarding/$', TeacherOnboarding.as_view()),
]