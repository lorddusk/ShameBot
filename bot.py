import discord
from datetime import datetime, timezone

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_member_ban(self, guild, user):
        ch = client.get_channel(461812579589685250)
        time = datetime.now(timezone.utc).strftime("%A, %d %B %Y at %H:%M")
        await ch.send(f'On '+time+f' UTC {user.name} got banned for breaking the rules. We shall now collectively shame this person. :bell: :bell: :bell:')

client = MyClient()
client.run('TOKEN HERE')
