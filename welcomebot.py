from mautrix.types import EventType
from maubot import Plugin MessageEvent
from maubot.handlers import event

class WelcomeBot(Plugin):
    @event.on(EventType.ROOM_MEMBER)
    async def handler(self, event: MessageEvent) -> None:
        event.send_message_event("testing")
