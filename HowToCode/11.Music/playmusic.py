import music

tune = ["C4:4", "D4:4", "E4:4", "C4:4", "C4:4", "D4:4", "E4:4", "C4:4",
        "E4:4", "F4:4", "G4:8", "E4:4", "F4:4", "G4:8"]
music.play(tune)

for freq in range(880, 1760, 16):
    music.pitch(freq, 30)
for freq in range(1760, 880, -16):
    music.pitch(freq, 30)