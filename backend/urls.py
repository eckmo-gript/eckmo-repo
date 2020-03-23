from django.urls import path
from backend.views import Chat
app_name = 'Eckmo-backend'

urlpatterns = [
    path('api/chatbot', Chat.as_view())

]
