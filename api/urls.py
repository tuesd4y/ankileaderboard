from . import views
from . import api
from . import api2
from django.urls import path, re_path
from django.http import HttpResponse

app_name = "main"
urlpatterns = [
    re_path(r'^robots.txt', lambda x: HttpResponse("User-Agent: *\nDisallow: /", content_type="text/plain"), name="robots_file"),
    # Website
	path("", views.reviews, name="reviews"),
    path("time/", views.time, name="time"),
    path("streak/", views.streak, name="streak"),
    path("retention/", views.retention, name="retention"),
    path(r'user/<username>/', views.user, name="user"),
	path('alpha/', views.alpha, name="alpha"),
	path('beta/', views.beta, name="beta"),
	path('gamma/', views.gamma, name="gamma"),
	path('delta/', views.delta, name="delta"),
	path('privacy/', views.privacy, name="privacy"),
	# API v1
	path('sync/', api.sync, name="sync"),
	path('delete/', api.delete, name="delete"),
	path('allusers/', api.all_users, name="allusers"),
	path('getdata/', api.get_data, name="get_data"),
	path('groups/', api.groups, name="groups"),
	path('create_group/', api.create_group, name="create_group"),
	path('league/', api.league_data, name="league_data"),
	path('season/', api.season, name="season"),
	path('setStatus/', api.setStatus, name="setStatus"),
	path('getStatus/', api.getStatus, name="getStatus"),
	path('getUserinfo/', api.getUserinfo, name="Userinfo"),
	path('joinGroup/', api.joinGroup, name="joinGroup"),
	path('manageGroup/', api.manageGroup, name="manageGroup"),
	path('banUser/', api.banUser, name="banUser"),
	path('leaveGroup/', api.leaveGroup, name="leaveGroup"),
	path('reportUser/', api.reportUser, name="reportUser"),
	path('signUp/', api.signUp, name="signUp"),
	path('logIn/', api.logIn, name="logIn"),
	path('deleteAccount/', api.deleteAccount, name="deleteAccount"),
	path('updateAccount/', api.updateAccount, name="updateAccount"),
	path('resetPassword/', api.resetPassword, name="resetPassword"),
	path('newPassword/<slug:token>', api.newPassword, name="newPassword"),
	path('changeUsername/', api.changeUsername, name="changeUsername"),
	# API v2
	path('api/v2/signUp/', api2.signUp, name="signUp"),
	path('api/v2/logIn/', api2.logIn, name="logIn"),
	path('api/v2/deleteAccount/', api2.deleteAccount, name="deleteAccount"),
	path('api/v2/changeUsername/', api2.changeUsername, name="changeUsername"),
	path('api/v2/resetPassword/', api2.resetPassword, name="resetPassword"),
	path('api/v2/newPassword/<slug:token>', api2.newPassword, name="newPassword"),
	path('api/v2/groups/', api2.groups, name="groups"),
	path('api/v2/joinGroup/', api2.joinGroup, name="joinGroup"),
	path('api/v2/createGroup/', api2.createGroup, name="createGroup"),
	path('api/v2/leaveGroup/', api2.leaveGroup, name="leaveGroup"),
	path('api/v2/manageGroup/', api2.manageGroup, name="manageGroup"),
	path('api/v2/banUser/', api2.banUser, name="banUser"),
	path('api/v2/reportUser/', api2.reportUser, name="reportUser"),
	path('api/v2/setBio/', api2.setBio, name="setBio"),
	path('api/v2/getBio/', api2.getBio, name="getBio"),
	path('api/v2/getUserinfo/', api2.getUserinfo, name="getUserinfo"),
	path('api/v2/users/', api2.users, name="users"),
	path('api/v2/season/', api2.season, name="season"),
	path('api/v2/sync/', api2.sync, name="sync"),
]
