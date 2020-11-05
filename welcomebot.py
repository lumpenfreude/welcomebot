from mautrix.types import RoomID, EventType, MessageType
from maubot import Plugin, MessageEvent
from maubot.handlers import event

class WelcomeBot(Plugin):
    @event.on(EventType.ROOM_MEMBER)
    async def send_welcome(self, evt: StateEvent) -> None:
        if (evt.content.membership == Membership.JOIN):
            self.client.send_message(evt.room_id, "FUCK")
