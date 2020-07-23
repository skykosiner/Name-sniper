import mojang_api
import asyncio

async def main():
    user = await Client.User.createUser('Minecraft playername')
    await user.authenticate('Mojang Email', 'Mojang password')
    await user.changeSkin('Skin url', slim_model = True)