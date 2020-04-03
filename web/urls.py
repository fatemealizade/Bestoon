from django.conf.urls import url
from . import views

urlpatterns = [
    url('submit/expense/$', views.submit_expense, name='submit-expense'),
    url('submit/income/$',views.submit_income,name='submit-income')
]
