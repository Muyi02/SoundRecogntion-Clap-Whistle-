

This Python project detects claps and whistles in real-time using a microphone connected to a Raspberry Pi 4B or any other compatible system. The script analyzes the audio input and identifies claps based on loudness and whistles based on their frequency content.

## Features

- Real-time detection of claps and whistles.

https://github.com/user-attachments/assets/984b3a1d-6f05-4f19-9795-76a3eb29975f


- Simple setup with adjustable thresholds for detecting sounds.
- Avoids repeated detection of the same sound through delays.
- Designed to run on Raspberry Pi 4B but can work on any system that supports the required libraries.

## Requirements

- Python 3.x
- PyAudio
- NumPy

## Setup Instructions

### 1. Clone the Repository

bash
git clone https://github.com/yourusername/clap-whistle-detection.git
cd clap-whistle-detection
2. Install Dependencies
First, make sure you have Python 3 installed. Then, install the required libraries using pip:

bash
pip3 install pyaudio numpy
Note: On some systems, you may need additional libraries for PyAudio. If you're on a Raspberry Pi, you can install them with:

bash
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
3. Running the Script
Once dependencies are installed, run the script:

bash
python3 sd.py
4. Adjusting Thresholds
You can adjust the detection thresholds in the sd.py file to fine-tune the sensitivity for claps and whistles.

CLAP_THRESHOLD: Controls how loud a sound needs to be to be considered a clap.
WHISTLE_MIN_FREQ and WHISTLE_MAX_FREQ: Define the frequency range for whistles.
WHISTLE_THRESHOLD: Adjusts the sensitivity of whistle detection.
NOISE_GATE_THRESHOLD: Ignores sounds that are too quiet.
5. Usage
The script listens for claps and whistles, printing a message to the console whenever it detects either sound.

Troubleshooting
If PyAudio fails to install, make sure you have the necessary system dependencies installed as listed above.
Adjust the thresholds if it detects sounds too frequently or misses claps/whistles.
