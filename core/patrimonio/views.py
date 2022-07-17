from django.views.generic import ListView, TemplateView, CreateView
from django.urls import reverse_lazy
from core.models import Patrimonio
from patrimonio.forms import InserePatrimonioForm


class IndexPatrimonio(TemplateView):
    template_name = "patrimonio/index.html"
    

class ListaPatrimonio(ListView):
    template_name = "patrimonio/lista.html"
    model = Patrimonio
    context_object_name = "listagem"


class CadastraPatrimonio(CreateView):
    template_name = "patrimonio/cadastra.html"
    model = Patrimonio
    form_class = InserePatrimonioForm
    success_url = reverse_lazy(  # apos cadastrado, vai para a lista!
    "patrimonio:listagem"
)

