from django.urls import path
from api.views import CompanyList,CompanyDetails,VacancyList,VacancyDetails,VacanciesByCompanies,VacanciesTopTen
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('login/',TokenObtainPairView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('companies/',CompanyList.as_view()),
    path('vacancies/',VacancyList.as_view()),
    path('companies/<int:pk>/',CompanyDetails.as_view()),
    path('vacancies/<int:pk>/',VacancyDetails.as_view()),
    path('companies/<int:pk>/vacancies/',VacanciesByCompanies.as_view()),
    path('vacancies/top_ten/',VacanciesTopTen.as_view()),

]