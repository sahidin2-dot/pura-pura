from motor.motor_asyncio import AsyncIOMotorClient

class MongoStorage:
    def __init__(self, uri: str, database: str, collection: str = "sessions"):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[database]
        self.collection = self.db[collection]

    async def open(self):
        pass  # Bisa dipakai untuk inisialisasi, jika perlu

    async def save(self, key: str, data: bytes):
        await self.collection.update_one(
            {"_id": key},
            {"$set": {"data": data}},
            upsert=True
        )

    async def load(self, key: str):
        doc = await self.collection.find_one({"_id": key})
        return doc["data"] if doc else None

    async def close(self):
        self.client.close()
