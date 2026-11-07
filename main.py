import asyncio
from adapter import get_suggestions

async def main():
    payload = await get_suggestions("rec-1", "Customer asked about a refund")
    print(payload.model_dump_json(indent=2))

if __name__ == "__main__":
    asyncio.run(main())
