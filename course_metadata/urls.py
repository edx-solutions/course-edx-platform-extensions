from django.conf import settings
from django.conf.urls import patterns, url

from . import views

COURSE_ID_PATTERN = settings.COURSE_ID_PATTERN

urlpatterns = patterns(
    '',
    url(
        r'^{}/settings$'.format(COURSE_ID_PATTERN),
        views.CourseSettingView.as_view(),
        name='additional-course-settings',
    ),
)
