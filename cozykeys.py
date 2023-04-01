import sys
import pygame
from pygame.locals import *
from pynput import keyboard
import os
import pkg_resources  # Added: Import pkg_resources

# Set the working directory to the script's path
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Pre-initialize the mixer with a smaller buffer size to reduce latency
pygame.mixer.pre_init(44100, -16, 2, 512)

# Initialize Pygame
pygame.init()

# Get the base directory (location of the script or temporary folder when bundled)
base_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

# Load sound effects
sound_effects = {
    'enter': pygame.mixer.Sound(os.path.join(base_dir, 'mods_Cozy_sounds_keyboard1.wav')),
    'backspace': pygame.mixer.Sound(os.path.join(base_dir, 'mods_Cozy_sounds_keyboard4.wav')),
    'space': pygame.mixer.Sound(os.path.join(base_dir, 'mods_Cozy_sounds_keyboard2.wav')),
    'tab': pygame.mixer.Sound(os.path.join(base_dir, 'mods_Cozy_sounds_keyboard3.wav')),
    'general': pygame.mixer.Sound(os.path.join(base_dir, 'mods_Cozy_sounds_keyboard3.wav')),
}
# Set the volume of the sound effects to 80%
for key in sound_effects:
    sound_effects[key].set_volume(1)

# Set the music volume to 2.0 (double the default)
pygame.mixer.music.set_volume(50.0)

key_mapping = {
    keyboard.Key.enter: 'enter',
    keyboard.Key.backspace: 'backspace',
    keyboard.Key.space: 'space',
    keyboard.Key.tab: 'tab',
}

pressed_keys = set()  # Added: Maintain a set of pressed keys


def play_sound(key_name):
    if key_name in sound_effects:
        sound_effects[key_name].play()


def on_press(key):
    if key not in pressed_keys:  # Added: Check if the key is already pressed
        try:
            key_name = key_mapping.get(key, 'general')
            play_sound(key_name)
            # Added: Add the key to the set of pressed keys
            pressed_keys.add(key)
        except AttributeError:
            pass


def on_release(key):
    # Added: Remove the key from the set of pressed keys
    pressed_keys.discard(key)
    if key == keyboard.Key.esc:
        sys.exit()

# Main loop


def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
