from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news_of_day, name = 'newsToday'),
    path('archives/<str:past_date>', views.past_days_news, name = 'pastNews'),
    path('search/', views.search_results, name='search_results'),
    path('detail/<int:pkid>', views.detail, name = 'detail'),
    path('news/<int:pics_id>',views.news,name ='news'),
    path('help_centre',views.help_centre,name="helpCentre")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)