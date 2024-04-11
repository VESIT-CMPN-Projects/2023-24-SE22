import pretty_midi
import collections
import pandas as pd
import numpy as np

def midi_to_notes(midi_file: str) -> pd.DataFrame:
  pm = pretty_midi.PrettyMIDI(midi_file)  #the main this pretty midi is doing giving all the data
  instrument = pm.instruments[0]
  notes = collections.defaultdict(list)

  # Sort the notes by start time
  sorted_notes = sorted(instrument.notes, key=lambda note: note.start)
  prev_start = sorted_notes[0].start

  for note in sorted_notes:
    start = note.start
    end = note.end
    notes['pitch'].append(note.pitch)
    notes['start'].append(start)
    notes['end'].append(end)
    notes['step'].append(start - prev_start)
    notes['duration'].append(end - start)
    prev_start = start

  return pd.DataFrame({name: np.array(value) for name, value in notes.items()})
# p=midi_to_notes(r"C:\Users\mruna\Downloads\dataset\mididataset sad songs\mididataset sad songs\Oh Humsafar Song  Neha Kakkar Himansh Kohli  Tony Kakkar  Bhushan Kumar  Manoj Muntashir (1).mid")
# print(p)