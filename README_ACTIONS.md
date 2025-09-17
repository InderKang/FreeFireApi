# free-fire-infoapi (GitHub Actions ready)

This fork adds a simple CLI runner (`run_uid.py`) and a GitHub Actions workflow
(`.github/workflows/freefire.yml`) so you can input a player UID via the workflow
dispatcher and see the output printed in the Actions log.

How it works
- The `run_uid.py` imports the Flask app and calls the existing `get_player_info` route
  inside a Flask `test_request_context`, reusing the repo's logic unchanged.
- The workflow installs requirements and runs `python run_uid.py --uid <your_uid>`.
- Keep your existing credentials in `app/config/settings.py` (they are used to request the JWT).

Usage
1. Push this repository to GitHub.
2. On GitHub, go to Actions → FreeFire UID Runner → Run workflow and enter the `uid` input.
3. View the job logs to see the printed JSON output.
