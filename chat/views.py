from django.shortcuts import get_list_or_404, get_object_or_404, render, reverse
from django.views.generic import CreateView, DetailView, ListView

from chat.models import Message, Room


class RoomList(ListView):
    model = Room
    template_name = "room_list.html"
    context_object_name = "rooms"


class RoomDetail(DetailView):
    model = Room
    template_name = "room_detail.html"
    context_object_name = "room"


class MessageView(CreateView):
    model = Message
    fields = ["text"]
    template_name = "create_message.html"

    def get_success_url(self):
        return reverse("send", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        room = get_object_or_404(Room, pk=self.kwargs["pk"])
        form.instance.room = room
        return super().form_valid(form)
