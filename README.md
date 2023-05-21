Compile an executable of [Basic Pitch](https://github.com/spotify/basic-pitch), a lightweight yet powerful audio-to-MIDI converter with pitch bend detection.

The executable is compiled using pyinstaller.

### How to Build Executable
- Install a recent version of Python (3.10.11 or newer)
- Clone the repo and navigate to the project folder
- Create a virtual environment: `python -m venv env`
- Activate the virtual environment: `env\Scripts\Activate.ps1` (for Windows PowerShell)
- Install dependencies: `pip install -r requirements.txt`
- Optional: Run Python file to test your setup `basic_pitch_exe.py --input_file example_audio.ogg`
- Compile executable using pyinstaller `pyinstaller basic_pitch_exe.spec`
    - The resulting executable can be found in the `dist` folder
