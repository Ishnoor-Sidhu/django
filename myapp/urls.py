
from django.urls import path
from myapp import views


urlpatterns = [
    path("",views.homepage, name="home" ),
    path("about/",views.aboutpage, name="about"),
    path("services/",views.servicespage, name="services" ),
    path("contactus/",views.contactuspage, name="contactus" ),
    path("contactdetail/",views.contactdetailpage, name="contact_detail" ),
    path("login/",views.loginpage, name="login" ),
    path("registration/",views.registrationpage, name="registration" ),
    path("logout/",views.logoutpage, name="logout"),


]


