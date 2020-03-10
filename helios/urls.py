# -*- coding: utf-8 -*-
from django.conf import settings
from django.urls import path, re_path, include

from . import views, url_names as names

urlpatterns = [
  path('testcookie', views.test_cookie, name=names.COOKIE_TEST),
  path('testcookie_2', views.test_cookie_2, name=names.COOKIE_TEST_2),
  path('nocookies', views.nocookies, name=names.COOKIE_NO),
  path('stats/', include('helios.stats_urls')),

  # election shortcut by shortname
  re_path(r'^e/(?P<election_short_name>[^/]+)$', views.election_shortcut, name=names.ELECTION_SHORTCUT),
  re_path(r'^e/(?P<election_short_name>[^/]+)/vote$', views.election_vote_shortcut, name=names.ELECTION_SHORTCUT_VOTE),

  # vote shortcut
  re_path(r'^v/(?P<vote_tinyhash>[^/]+)$', views.castvote_shortcut, name=names.CAST_VOTE_SHORTCUT),

  # trustee login
  re_path(r'^t/(?P<election_short_name>[^/]+)/(?P<trustee_email>[^/]+)/(?P<trustee_secret>[^/]+)$', views.trustee_login,
      name=names.TRUSTEE_LOGIN),

  # election
  path('elections/params', views.election_params, name=names.ELECTIONS_PARAMS),
  path('elections/verifier', views.election_verifier, name=names.ELECTIONS_VERIFIER),
  path('elections/single_ballot_verifier', views.election_single_ballot_verifier, name=names.ELECTIONS_VERIFIER_SINGLE_BALLOT),
  path('elections/new', views.election_new, name=names.ELECTIONS_NEW),
  path('elections/administered', views.elections_administered, name=names.ELECTIONS_ADMINISTERED),
  path('elections/voted', views.elections_voted, name=names.ELECTIONS_VOTED),

  re_path(r'^elections/(?P<election_uuid>[^/]+)', include('helios.election_urls')),
]

if "localhost" in settings.URL_HOST or "127.0.0.1" in settings.URL_HOST:
  urlpatterns.append(path('autologin', views.admin_autologin))
  import logging
  if not settings.TESTING:
    logging.error("Autologin path for admin is enabled, even if not a TESTING environment.")
  else:
    logging.warning("Autologin path for admin is enabled.")
