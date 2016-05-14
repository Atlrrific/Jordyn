from django.conf.urls import url
from Backend import views

urlpatterns = [
    url(r'^instruction/$', views.InstructionList.as_view()),
    url(r'^instruction/(?P<pk>[0-9]+)/$', views.InstructionDetail.as_view()),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
