import turbo

from .models import Message, Room


@turbo.register(Message)
class MessageBroadcast(turbo.ModelBroadcast):
    def on_save(self, message, created, *args, **kwargs):
        if created:
            message.room.turbo.render(
                "components/message.html", {"message": message}
            ).append(id="messages")
