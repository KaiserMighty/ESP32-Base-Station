import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-modify-playback-state user-read-playback-state",
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    open_browser=True,
    cache_path=".spotifycache"
))

def controller_main(arg):
    match arg:
        case "ROTARY":
            loop_track()
        case "SKIP":
            next_track()
        case "PLAY":
            play_pause()
        case "BACK":
            previous_track()
        case "VOLDOWN":
            volume_down()
        case "VOLUP":
            volume_up()

def play_pause():
    playback = sp.current_playback()
    if playback and playback['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()

def next_track():
    sp.next_track()

def previous_track():
    sp.previous_track()

def loop_track():
    sp.repeat('track')

def volume_up(step=5):
    volume = _get_current_volume()
    if volume is not None:
        new_volume = min(100, volume + step)
        sp.volume(new_volume)

def volume_down(step=5):
    volume = _get_current_volume()
    if volume is not None:
        new_volume = max(0, volume - step)
        sp.volume(new_volume)

def _get_current_volume():
    playback = sp.current_playback()
    if playback and 'device' in playback:
        return playback['device']['volume_percent']
    return None
