from django.views.generic import ListView, TemplateView, CreateView, DeleteView, UpdateView
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
    success_url = reverse_lazy("patrimonio:listagem") # Apos cadastrado, vai para lista


class ApagaPatrimonio(DeleteView):
    template_name = "patrimonio/apaga.html"
    model = Patrimonio
    context_object_name = "apaga_patrimonio"
    success_url = reverse_lazy("patrimonio:listagem") # pós cadastrado vai para a lista


class AtualizaPatrimonio(UpdateView):
    template_name = "patrimonio/atualiza.html"
    model = Patrimonio
    fields = '__all__'  # substitui listar tosos os campos
    success_url = reverse_lazy("patrimonio:listagem") # pós cadastrado vai para a lista

