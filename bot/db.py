from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import MONGODB_URI

client = None
db = None

async def init_db():
    global client, db
    client = AsyncIOMotorClient(MONGODB_URI)
    db = client.telegram_emoji_bot

async def increment_score(group_id, user_id, username):
    await db.scores.update_one(
        {'group_id': group_id, 'user_id': user_id},
        {'$inc': {'score': 1}, '$set': {'username': username}},
        upsert=True
    )

async def get_leaderboard(group_id, limit=10):
    cursor = db.scores.find({'group_id': group_id}).sort('score', -1).limit(limit)
    return await cursor.to_list(length=limit)

async def reset_round(group_id):
    await db.rounds.update_one({'group_id': group_id}, {'$set': {'active': False}}, upsert=True)

async def start_round(group_id, emoji):
    await db.rounds.update_one({'group_id': group_id}, {'$set': {'active': True, 'emoji': emoji, 'winner': None}}, upsert=True)

async def get_round(group_id):
    return await db.rounds.find_one({'group_id': group_id})

async def set_winner(group_id, user_id):
    await db.rounds.update_one({'group_id': group_id}, {'$set': {'winner': user_id}})
