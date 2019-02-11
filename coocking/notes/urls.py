from django.urls import path
from .views import AddNoteToDishView, AddNoteToOrderView

app_name = 'notes'

urlpatterns = [
    path('dish<int:dish_id>/add_note',AddNoteToDishView.as_view(), name='add_notes_to_dish'),
    path('order<int:order_id>/add_note',AddNoteToOrderView.as_view(), name='add_notes_to_order'),

]