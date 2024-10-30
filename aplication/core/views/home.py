from django.views.generic import TemplateView

from aplication.core.models import Paciente

class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {"title1": "SaludSync", "title2": "Sistema Medico"}
        context["can_paci"] = Paciente.cantidad_pacientes()
        print(context["can_paci"])
        return context