from django.urls import path
from .views import page_register, page_login, home_page, create_publication, like_publication, out, create_comments

urlpatterns = [
    path("register/", page_register, name = "register"),
    path("login/", page_login, name = "login"),
    path("test/", create_publication, name = "create_publication"),
    path("", home_page, name = "home_page"),
    path("like/<slug:slug>/", like_publication, name="like_publication"),
    path("logout/", out),
    path("create_c/<slug:slug>/", create_comments, name="create_comments"),

]
