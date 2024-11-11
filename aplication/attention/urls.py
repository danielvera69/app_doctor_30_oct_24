from django.urls import path
from aplication.attention.views.medical_attention import AttentionCreateView, AttentionDetailView, AttentionListView, AttentionUpdateView
from aplication.core.views.home import HomeTemplateView
from aplication.core.views.patient import PatientCreateView, PatientDeleteView, PatientDetailView, PatientListView, PatientUpdateView
 
app_name='attention' # define un espacio de nombre para la aplicacion
urlpatterns = [
  # rutas de atenciones
  path('attention_list/',AttentionListView.as_view() ,name="attention_list"),
  path('attention_create/', AttentionCreateView.as_view(),name="attention_create"),
  path('attention_update/<int:pk>/', AttentionUpdateView.as_view(),name='attention_update'),
  path('attention_detail/<int:pk>/', AttentionDetailView.as_view(),name='attention_detail'),
  # path('patient_delete/<int:pk>/', PatientDeleteView.as_view(),name='patient_delete'),
]