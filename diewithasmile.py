import time
import sys

def type_text(lines, delays):
    for line, delay in zip(lines, delays):
        time.sleep(delay)  # Wait before starting the line
        for char in line:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()

lyrics = [
    "So I'ma love you every night like it's the last night",
    "Like it's the last night",
    "If the world was ending",
    "I'd wanna be next to youuuuuuu!",
    "If the party was over",
    "And our time on Earth was throughhh!",
    "I'd wanna hold you just for a while",
    "And dieee with a smile",
]   

delays = [0.6, 0.7, 1.0, 1.6, 4.0, 3.1, 4.1, 3.3]
type_text(lyrics, delays)