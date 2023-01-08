import discord
import asyncio


class MyClient(discord.Client):
	# ID of bot owner
    ownerID = <OWNER ID HERE>
	
	# ID of target user
    targetID = <TARGET ID HERE>

	# Checks if client is ready
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

	# Checks if a user's presence is updated
    async def on_presence_update(self, before: discord.Member, after: discord.Member):

		# Checks for target user
        if before.id != self.targetID:
            return

		# Checks if the presence change is due to a status change (online, offline, etc)
        if before.status != after.status:
            if before.activity is None or after.activity is None:
                return
            await asyncio.sleep(5)
            if before.activity is None or after.activity is None:
                return

		# Fetch the owner's user object
        owner = await self.fetch_user(self.ownerID)

		# If the activity changed, send a message to the owner
        if before.activity != after.activity:
			
			# Send the message as an embed object
            embed = discord.Embed(
                title=f'{after.name} updated their status', color=0xD8BFD8)
            embed.add_field(
                name='From:', value=f'{before.activity}', inline=False)
            embed.add_field(
                name='To:', value=f'{after.activity}', inline=False)
            await owner.send(embed=embed)


# Add the members and presences intents to the default intents
intents = discord.Intents.default()
intents.members = True
intents.presences = True

# Create a client with the custom intents
client = MyClient(intents=intents)

# Run the client with the bot token
client.run('MTA1ODE2NjU4MTk0MDcxNTYwMQ.GqYc4X.u9G4d2OcU7mLt44OjkdN1dBkLu1T654QUuBB10')
