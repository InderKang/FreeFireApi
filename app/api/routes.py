from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio

router = APIRouter()

class PlayerStats(BaseModel):
    uid: str
    nickname: str | None = None
    level: int | None = None
    total_kills: int | None = None
    total_matches: int | None = None
    win_rate: float | None = None
    raw: dict | None = None


async def fetch_player_stats_from_source(uid: str) -> dict:
    """
    TODO: Replace with real Free Fire scraping/endpoint logic.
    Currently returns mock data so API is runnable.
    """
    await asyncio.sleep(0.2)  # simulate network delay
    return {
        "uid": uid,
        "nickname": f"player_{uid}",
        "level": 50,
        "total_kills": 1234,
        "total_matches": 456,
        "win_rate": round(1234 / max(1, 456) * 100, 2),
        "raw": {"note": "This is mock data. Replace with real implementation."},
    }


@router.get("/player/{uid}", response_model=PlayerStats)
async def get_player(uid: str):
    try:
        data = await fetch_player_stats_from_source(uid)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
