import winsound
import time

# Define the frequencies for the notes (in Hz) and their corresponding duration (in milliseconds)
# These frequencies are approximations of the "Among Us" theme song melody
notes = {
    'C4': 261, 'D4': 294, 'E4': 329, 'F4': 349, 'G4': 392, 'A4': 440, 'B4': 493,
    'C5': 523, 'D5': 587, 'E5': 659, 'F5': 698, 'G5': 784, 'A5': 880, 'B5': 987
}

# Define the melody in terms of notes and durations
melody = [
    ('E4', 400), ('E4', 400), ('F4', 400), ('G4', 400), ('G4', 400), ('F4', 400),
    ('E4', 400), ('D4', 400), ('C4', 800), 
    ('C4', 400), ('D4', 400), ('E4', 400), ('E4', 400), ('F4', 400), ('G4', 400),
    ('G4', 400), ('F4', 400), ('E4', 400), ('D4', 400), ('C4', 800),
    
    ('E4', 400), ('E4', 400), ('F4', 400), ('G4', 400), ('G4', 400), ('F4', 400),
    ('E4', 400), ('D4', 400), ('C4', 800),
    
    # Repeat part of the melody (for simplicity, can be looped if desired)
    ('C4', 400), ('D4', 400), ('E4', 400), ('E4', 400), ('F4', 400), ('G4', 400),
    ('G4', 400), ('F4', 400), ('E4', 400), ('D4', 400), ('C4', 800)
]

# Function to play the melody
def play_melody():
    for note, duration in melody:
        winsound.Beep(notes[note], duration)
        time.sleep(0.05)  # Small delay between notes

# Play the Among Us theme song
play_melody()