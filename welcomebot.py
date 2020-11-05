from mautrix.types import RoomID, UserID, AccountDataEventContent, EventType, Membership
from maubot import Plugin, MessageEvent
from maubot.handlers import event, command

class WelcomeBot(Plugin):
    @event.on(EventType.ROOM_MEMBER)
    async def send_welcome(self, evt: MessageEvent) -> AccountDataEventContent:
        if (evt.content.membership == Membership.JOIN):
            await self.respond(evt.room_id, "FUCK")
