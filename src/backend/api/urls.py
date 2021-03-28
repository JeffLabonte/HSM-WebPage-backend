from backend.api.scripts.views import ScriptCreateView

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path("scripts/", ScriptCreateView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
