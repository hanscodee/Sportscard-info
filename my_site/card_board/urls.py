from django.urls import URLPattern, path
from . import views

app_name = 'card_board'

urlpatterns = [
    path('',views.example_view,name='example'),
    path('card',views.card_view,name= 'card'),
    path('kobe',views.kobe_view,name= 'kobe'),
    path('james',views.james_view,name= 'james'),
    path('jordan',views.jordan_view,name= 'jordan'),
    path('player',views.player_view,name= 'player'),
    path('search',views.search_view, name='search'),
    path('detail',views.detail_view, name='detail')

]