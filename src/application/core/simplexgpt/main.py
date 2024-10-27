from __future__ import annotations
import asyncio
from app.application import SimpleXGPT

async def main():
    app: SimpleXGPT = SimpleXGPT()
    await app.run()

if __name__ == "__main__":
    asyncio.run(main())
