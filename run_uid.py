#!/usr/bin/env python3
"""CLI runner to call the existing Flask route `get_player_info` and print result.
Usage: python run_uid.py --uid <player_uid>
This imports the Flask app and calls the route inside a test_request_context so all existing logic is reused.
"""
import argparse
import sys
from main import app
from app.api.routes import get_player_info
from flask import Response

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--uid', required=True, help='Player UID to fetch')
    args = parser.parse_args()

    url = f"/api/player-info?uid={args.uid}"
    with app.test_request_context(url):
        resp = get_player_info()
        # route functions may return (response, status) or a Response object
        if isinstance(resp, tuple):
            response_obj = resp[0]
        else:
            response_obj = resp
        try:
            if isinstance(response_obj, Response):
                data = response_obj.get_data(as_text=True)
                print(data)
            else:
                # fallback: print repr
                print(response_obj)
        except Exception as e:
            print('Failed to read response:', e, file=sys.stderr)
            print('Raw response object:', repr(response_obj))

if __name__ == '__main__':
    main()
