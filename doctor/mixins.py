from django.db.models import Q

class ListViewMixin(object):
    query = None
    paginate_by = 2
    
    def dispatch(self, request, *args, **kwargs):
        self.query = Q()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title1'] = f'{self.model._meta.verbose_name_plural}'
        context['title2'] = f'Consulta de {self.model._meta.verbose_name_plural}'
        # añade los permisos del grupo activo(add_pais, view_ciudad)
        # print("estoy en el mixing..")
        # print(self.request.session.get('group_id'))
        ### context['permissions'] = self._get_permission_dict_of_group() 
        # crear la data y la session con los menus y modulos del usuario 
        ### MenuModule(self.request).fill(context)
        return context