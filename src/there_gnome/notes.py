

# List of notes in one octave
notes = ["C", "C#","D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def get_note(pitch):
    octave = (pitch // 12)  # Determine the octave by dividing the index by 12
    note = notes[pitch % 12]  # Get the note for the current index within the octave
    return f"{note}{octave + 4}"