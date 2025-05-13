import time

def print_lyrics():
    lyrics = [
        ("I'll imagine we fell in love", 0.7, 0.07),
        ("I'll nap under moonlight skies with you", 0.7, 0.06),
        ("I think I'll picture us, you with the waves", 0.7, 0.09),
        ("The ocean's colors on your face", 0.7, 0.09),
        ("I'll leave my heart with your air", 0.7, 0.09),
        ("So let me fly with you", 0.7, 0.09),
        ("Will you be forever with me?", 0.7, 0.18),
        ("", 0.3, 0.0),
        ("", 0.5, 0.06)]
    for ting, delay_time, delay_hand in lyrics:
        for c in ting:
            print(c, end='', flush=True)
            time.sleep(delay_hand)
        print()
        time.sleep(delay_time)

if __name__ == "__main__":
    print_lyrics()