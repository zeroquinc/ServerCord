from aiohttp import web

from utils.custom_logger import logger

class HandleWebHook:
    # Initialize the webhook receiver
    def __init__(self, discord_bot, host="0.0.0.0", port=2024):
        self.discord_bot = discord_bot
        self.host = host
        self.port = port
        self.app = web.Application()
        #self.app.router.add_post('/sonarr_webhook', self.handle_sonarr)
        #self.app.router.add_post('/radarr_webhook', self.handle_radarr)
        #self.app.router.add_post('/plex_webhook', self.handle_plex)
        self.uvicorn_params = {
            "host": self.host,
            "port": self.port,
            "access_log": False,
        }

    # Start the webhook receiver
    async def start(self):
        try:
            runner = web.AppRunner(self.app)
            await runner.setup()
            site = web.TCPSite(runner, self.host, self.port)
            await site.start()
            logger.info(f"Server started at http://{self.host}:{self.port}")
        except Exception as e:
            logger.error(f"Error starting the server: {e}")


    # Cleanup the webhook receiver
    async def cleanup(self):
        await self.app.cleanup()