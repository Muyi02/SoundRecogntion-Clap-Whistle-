import pyaudio
import numpy as np
import time

# Audio configuration
CHUNK = 1024             # Size of data frames
FORMAT = pyaudio.paInt16  # 16-bit format
CHANNELS = 1              # Mono audio
RATE = 44100              # Sampling rate
CLAP_THRESHOLD = 17000    # Adjusted threshold for detecting claps
WHISTLE_MIN_FREQ = 1000   # Minimum frequency for whistle detection
WHISTLE_MAX_FREQ = 3000   # Maximum frequency for whistle detection
WHISTLE_THRESHOLD = 5000  # Increased magnitude threshold for whistles
NOISE_GATE_THRESHOLD = 1000  # Minimum sound level to consider for detection
DETECTION_DELAY = 1       # Delay between detections to avoid repeats

def detect_clap(audio_data):
    """Detect claps based on peak signal amplitude."""
    peak_amplitude = np.abs(audio_data).max()  # Peak amplitude of the signal
    return peak_amplitude > CLAP_THRESHOLD

def detect_whistle(audio_data, rate):
    """Detect whistles based on frequency."""
    # Apply FFT (Fast Fourier Transform) to get frequency content
    fft_data = np.fft.fft(audio_data)
    fft_freqs = np.fft.fftfreq(len(fft_data), 1.0 / rate)

    # Focus on positive frequencies
    fft_data = np.abs(fft_data[:len(fft_data)//2])
    fft_freqs = fft_freqs[:len(fft_freqs)//2]

    # Check for ambient noise (low-level signals)
    if np.mean(np.abs(audio_data)) < NOISE_GATE_THRESHOLD:
        return False  # Skip processing if the sound is too quiet

    # Find frequencies within the whistle range
    whistle_freqs = np.where((fft_freqs > WHISTLE_MIN_FREQ) & (fft_freqs < WHISTLE_MAX_FREQ))

    # If the magnitude of the frequencies in the whistle range exceeds a threshold, a whistle is detected
    if np.max(fft_data[whistle_freqs]) > WHISTLE_THRESHOLD:
        return True
    return False

def main():
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open the microphone stream
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    print("Listening for claps and whistles...")
    try:
        while True:
            # Read audio data from the stream
            data = stream.read(CHUNK, exception_on_overflow=False)
            audio_data = np.frombuffer(data, dtype=np.int16)

            # Detect claps
            if detect_clap(audio_data):
                print("Clap detected!")
                time.sleep(DETECTION_DELAY)  # Avoid detecting the same clap multiple times

            # Detect whistles
            if detect_whistle(audio_data, RATE):
                print("Whistle detected!")
                time.sleep(DETECTION_DELAY)  # Avoid detecting the same whistle multiple times

    except KeyboardInterrupt:
        print("Stopping detection...")

    # Close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == "__main__":
    main()
