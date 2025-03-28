# Leaderboard for Anki 2.1
Forked from [ThoreBor/Anki_Leaderboard](https://github.com/ThoreBor/Anki_Leaderboard) and currently still under development.

This add-on ranks all of its users by the number of cards reviewed today, time spent studying today, current streak, reviews in the past 31 days and retention. You can also invite friends, join a group and/or country leaderboard and compete in leagues.

The online version of the add-on is available on [this website](https://leaderboard.tuesd4y.com/).

## Installing

This section is still under construction

[//]: # (You can download the newest stable release from [AnkiWeb]&#40;https://ankiweb.net/shared/info/41708974&#41;.)

[//]: # (The newest stable version can be downloaded from GitHub. Just download the .ankiaddon file from releases and open it.)

If you want to test the newest, potentially unstable version from GitHub, clone this repository into the addons21 folder and run /tools/build_ui.sh. If you already have an account, you might want to copy the meta.json file into the cloned folder.

## Setup for local development

### Setting up the server

- [Install uv](https://docs.astral.sh/uv/getting-started/installation/) if you haven't already
- Install dependencies (including dev dependencies) `uv sync`
- Activate the environment (`source .venv/bin/activate` on macOS)
- Migrate db if necessary `python manage.py migrate`
- Start the server `python manage.py runserver`

Before commiting, please install the git-hooks to auto-format files before they are commited using `pre-commit install`.

### Starting the client

- Build the UI `cd tools && ./build_ui.sh`
- Symlink (or copy) the folder into the anki addons folder (e.g. `ln -s /Users/dev/code/temp/Anki_Leaderboard/ anki/addons21`)
- Start Anki (and pass the server URL environment variable). The `-b temp_anki` flag starts from a temporary profile in the temp_anki folder.
  `export LEADERBOARD_API_BASE="http://localhost:8000"; /Applications/Anki.app/Contents/MacOS/anki -b temp_anki`

### Migrating the db

- Change models
- `python manage.py makemigrations`
- `python manage.py migrate`
- Commit the created migration files

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ThoreBor/Anki_Leaderboard/blob/master/LICENSE) file for details

© Chris and Eva 2025
See also the list of [contributors](https://github.com/ThoreBor/Anki_Leaderboard/contributors) who participated in this project.

<img src="screenshots/lb_light.png" align="left" width="40%" height="40%"></img>
<img src="screenshots/lb_dark.png" align="left" width="40%" height="40%"></img>
<img src="screenshots/homescreen_light.png" align="left" width="40%" height="40%"></img>
<img src="screenshots/homescreen_dark.png" align="left" width="40%" height="40%"></img>

