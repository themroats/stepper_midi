
from music21 import converter


# f = "arduino/goldsaucer_single_notes.mid" # works!! 40
# f = "arduino/Fireflies.mid" # works!! 90


# f = "arduino/set4/data/Zelda_Overworld.mid" #eh kinda sounds bad
# f = "arduino/set4/data/Still_Alive-1.mid" #amazing 60
# f = "arduino/Hans_Zimmer_-_Pirates_Of_The_Caribbean_-_He's_A_Pirate.mid"
# f = "arduino/pirates.mid" # 
# f = "arduino/MIDIlovania.mid" # hype 70
# f = "arduino/Spiderman_2_Pizza.mid" # sick 40 *12

# f = "arduino/mario1.mid" # 80
# f = "arduino/marble.mid"
f = "arduino/mii.mid"


score = converter.parse(f)




from music21 import *

stepper_count = 3
piece = converter.parse(f)
chords = list((piece.chordify()))
all_parts = [[] for _ in range(stepper_count)]
for event in chords:
  part_tuples = []

  
  offset = event.offset
  if getattr(event, 'isNote', None) and event.isNote:
    part_tuples.append((event.nameWithOctave, event.quarterLength, offset))
  if getattr(event, 'isChord', None) and event.isChord:
    notes = event.notes

  
    for n_idx in range(stepper_count):
      if n_idx >= len(list(event.notes)):
        all_parts[n_idx].append(('Rest', note.quarterLength, offset))
      
      else:
        note = notes[n_idx]
        all_parts[n_idx].append((note.nameWithOctave, note.quarterLength, offset))

  if getattr(event, 'isRest', None) and event.isRest:


    for n_idx in range(stepper_count):

      all_parts[n_idx].append(('Rest', event.quarterLength, offset))
      print(event.quarterLength, offset)


print(all_parts)


lookup = {
    "Rest": 0,
    "G3": 1,
    "G#3": 2,
    "A-3": 2,
    "A3": 3,
    "A#3": 4,
    "B-3": 4,
    "B3": 5,
    "C4": 6,
    "C#4": 7,
    "D-4": 7,
    "D4": 8,
    "D#4": 9,
    "E-4": 9,
    "E4": 10,
    "F4": 11,
    "F#4": 12,
    "G-4": 12,
    "G4": 13,
    "G#4": 14,
    "A-4": 14,
    "A4": 15,
    "A#4": 16,
    "B-4": 16,
    "B4": 17,
    "C5": 18,
    "C#5": 19,
    "D-5": 19,
    "D5": 20,
    "D#5": 21,
    "E-5": 21,
    "E5": 22,
    "F5": 23,
    "F#5": 24,
    "G-5": 24,
    "G5": 25,

    "G2": 26,
    "G#2": 27,
    "A-2": 27,
    "A2": 28,
    "A#2": 29,
    "B-2": 29,
    "B2": 30,
    "C3": 31,
    "C#3": 32,
    "D-3": 32,
    "D3": 33,
    "D#3": 34,
    "E-3": 34,
    "E3": 35,
    "F3": 36,
    "F#3": 37,
    "G-3": 37,


    "G1": 38,
    "G#1": 39,
    "A-1": 39,
    "A1": 40,
    "A#1": 41,
    "B-1": 41,
    "B1": 42,
    "C2": 43,
    "C#2": 44,
    "D-2": 44,
    "D2": 45,
    "D#2": 46,
    "E-2": 46,
    "E2": 47,
    "F2": 48,
    "F#2": 49,
    "G-2": 49,

    "G#5": 50,
    "A-5": 50,
    "A5": 51,
    "A#5": 52,
    "B-5": 52,
    "B5": 53,
    "C6": 54,
    "C#6": 55,
    "D-6": 55,
    "D6": 56,
    "D#6": 57,
    "E-6": 57,
    "E6": 58,
    "F6": 59,
    "F#6": 60,
    "G-6": 60,
    "G6": 61,


}


song_str = ["uint8_t song1[] = {", "uint8_t song2[] = {", "uint8_t song3[] = {"]
stop_str = ["bool stops1[] = {  ", "bool stops2[] = {  ", "bool stops3[] = {  "]

thresh = 2000
for p in range(3):
    j= 0

    for e in list(all_parts)[p]:

        note_name, duration, offset = e
        if note_name in lookup.keys():
            note_num = lookup[note_name]
        else:

            note_num = 0

        for i in range(int(duration * 8)):
            song_str[p] += str(note_num) + ","
            stop_str[p] += "0,"
            j+=1
            if j>thresh:
                break
        if j>thresh:
            break
        stop_str[p] = stop_str[p][:-2]
        stop_str[p] += "1,"
    song_str[p] += "};"
    stop_str[p] += "};"
print(song_str[0])
print(song_str[1])
print(song_str[2])


print("int songLen = ", j, ";")



