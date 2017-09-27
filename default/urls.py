from django.conf.urls import url

from . import views

app_name = 'default'

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^home$', views.home, name="home"),
    url(r'^register$', views.register, name="register"),
    url(r'^profile$', views.profile, name="profile"),
    url(r'^profile/update$', views.profile_update, name="profile_update"),
    url(r'^(?P<user_id>[0-9]+)/thanks$', views.thanks, name="thanks"),
    url(r'^author/conferences$', views.author_conferences, name="author_conferences"),
    url(r'^author/submissions$', views.author_submissions, name="author_submissions"),
    url(r'^papers/$', views.papers, name="papers"),
    url(r'^author/submissions/(?P<conf_id>[0-9]+)/upload$', views.author_submissions_upload, name="author_submissions_upload"),
    url(r'^author/submission/info/(?P<submission_id>[0-9]+)$', views.author_submissions_info, name="author_submissions_info"),
    url(r'^support$', views.support_index, name="support_index"),
    url(r'^news$', views.news_index, name="news_index"),
    url(r'^author/reviews$', views.author_reviews, name="author_reviews"),
    url(r'^conference/search$', views.conference_search, name="conference_search"),
    url(r'^conference/register$', views.conference_register, name="conference_register"),
    url(r'^conference/info/(?P<conf_id>[0-9]+)$', views.conference_info, name="conference_info"),
    url(r'^conference/thanks/(?P<conf_id>[0-9]+)$', views.conference_thanks, name="conference_thanks")
]
