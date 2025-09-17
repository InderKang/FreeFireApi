import argparse
import uvicorn
from fastapi import FastAPI
from app.api import routes

app = FastAPI(title="Free Fire Unofficial API")
app.include_router(routes.router)


# CLI entry point (for GitHub Actions fetch.yml)
def cli_entry():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uid", type=str, help="Free Fire UID")
    args = parser.parse_args()

    if args.uid:
        import asyncio
        from app.api.routes import fetch_player_stats_from_source

        data = asyncio.run(fetch_player_stats_from_source(args.uid))
        print(data)


if __name__ == "__main__":
    cli_entry()
