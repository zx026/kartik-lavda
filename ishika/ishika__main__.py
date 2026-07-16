import asyncio
import os

from aiohttp import web

from ishika import app, LOGGER
from ishika.modules.helpers.mongo import mongoping


async def health(_request):
    return web.Response(text="Ishika is alive ✅")


async def run_web_server():
    """Binds a tiny HTTP server so Render's Web Service sees an open port.
    Also gives you a URL to ping (e.g. with UptimeRobot) to stop the free
    instance from spinning down after 15 minutes of inactivity."""
    port = int(os.environ.get("PORT", 8080))
    web_app = web.Application()
    web_app.router.add_get("/", health)

    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    LOGGER.info(f"Health-check server listening on port {port}")


async def main():
    await mongoping()
    await run_web_server()
    await app.start()
    LOGGER.info("IshikaChatBot Started Successfully ✅")
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())
