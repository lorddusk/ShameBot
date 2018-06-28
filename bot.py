import discord
from datetime import datetime, timezone


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content == "!backlog" and (
                message.author.id == 95486109852631040 or message.author.id == 281076500017446914) and message.guild.id == 285108337693949972:
            guild = client.get_guild(445867743477104641)
            async for entry in guild.audit_logs(reverse=True, action=discord.AuditLogAction.ban):
                day = datetime.date(entry.created_at).strftime("%A, %d %B %Y")
                time = datetime.time(entry.created_at).strftime("%H:%M")
                ch = client.get_channel(461812579589685250)
                await ch.send(
                    f'On ' + day + ' at ' + time + f' UTC {entry.target.name} got banned for breaking the rules. We shall now collectively shame this person. :bell: :bell: :bell:')

    async def on_member_ban(self, guild, user):
        ch = client.get_channel(461812579589685250)
        time = datetime.now(timezone.utc).strftime("%A, %d %B %Y at %H:%M")
        await ch.send(
            f'On ' + time + f' UTC {user.name} got banned for breaking the rules. We shall now collectively shame this person. :bell: :bell: :bell:')


client = MyClient()
client.run('TOKEN')
