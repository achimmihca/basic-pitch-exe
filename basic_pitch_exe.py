from __future__ import annotations
import argparse
import glob
import os
import pathlib
import basic_pitch.inference

ICASSP_2022_MODEL_PATH = pathlib.Path(__file__).parent / "saved_models/icassp_2022/nmp"

# Parse command line arguments
parser = argparse.ArgumentParser(
                    prog='Basic Pitch executable',
                    description='Executable version of Basic Pitch https://github.com/spotify/basic-pitch')
parser.add_argument('--input_file', required=True)
parser.add_argument('--output_folder', default=".")
parser.add_argument('--save_midi', default=True, action='store_true')
parser.add_argument('--sonify_midi', default=False, action='store_true')
parser.add_argument('--save_model_outputs', default=False, action='store_true')
parser.add_argument('--save_notes', default=False, action='store_true')
parser.add_argument('--onset_threshold', default=0.5, type=float)
parser.add_argument('--frame_threshold', default=0.3, type=float)
parser.add_argument('--minimum_note_length', default=58, type=int)
parser.add_argument('--minimum_frequency', default=None)
parser.add_argument('--maximum_frequency', default=None)
parser.add_argument('--multiple_pitch_bends', default=False, action='store_true')
parser.add_argument('--melodia_trick', default=True, action='store_true')
parser.add_argument('--debug_file', default=None)
parser.add_argument('--sonification_samplerate', default=44100, type=int)
parser.add_argument('--midi_tempo', default=120, type=int)
args = parser.parse_args()

input_audio_path = args.input_file
input_audio_path_list = [ input_audio_path ]
output_folder = args.output_folder
save_midi = args.save_midi
sonify_midi = args.sonify_midi
save_model_outputs = args.save_model_outputs
save_notes = args.save_notes
model_path = ICASSP_2022_MODEL_PATH
onset_threshold = args.onset_threshold
frame_threshold = args.frame_threshold
minimum_note_length = args.minimum_note_length
minimum_frequency = args.minimum_frequency
maximum_frequency = args.maximum_frequency
multiple_pitch_bends = args.multiple_pitch_bends
melodia_trick = args.melodia_trick
debug_file = args.debug_file
sonification_samplerate = args.sonification_samplerate
midi_tempo = args.midi_tempo

# Remove old output files
old_files_pattern = f"{output_folder}/*_basic_pitch.*"
for file in glob.glob(old_files_pattern):
    os.remove(file)

# Run Basic Pitch model
basic_pitch.inference.predict_and_save (
    input_audio_path_list,
    output_folder,
    save_midi,
    sonify_midi,
    save_model_outputs,
    save_notes,
    model_path,
    onset_threshold,
    frame_threshold,
    minimum_note_length,
    minimum_frequency,
    maximum_frequency,
    multiple_pitch_bends,
    melodia_trick,
    debug_file,
    sonification_samplerate,
    midi_tempo,
)
