from __future__ import annotations
import argparse
import glob
import os
import basic_pitch.inference

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
args = parser.parse_args()

input_audio_path = args.input_file
input_audio_path_list = [ input_audio_path ]
output_folder = args.output_folder
save_midi = args.save_midi
sonify_midi = args.sonify_midi
save_model_outputs = args.save_model_outputs
save_notes = args.save_notes

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
)
