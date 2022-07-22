#from . import views
from django.urls import path
from patrimonio.views import IndexPatrimonio, ListaPatrimonio, CadastraPatrimonio, ApagaPatrimonio, AtualizaPatrimonio


app_name = 'patrimonio'
# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    path('', IndexPatrimonio.as_view(), name='index'),
    path('lista', ListaPatrimonio.as_view(), name='listagem'),
    path('cadastra',CadastraPatrimonio.as_view(), name='cadastra_patrimonio'),
    path('apaga/<pk>', ApagaPatrimonio.as_view(), name='apaga_patrimonio'),
    path('atualiza/<pk>', AtualizaPatrimonio.as_view(), name='atualiza_patrimonio'),

]

