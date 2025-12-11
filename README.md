# Whisper Arabic Speech Transcription Tool

A lightweight tool for automatically transcribing Arabic audio using OpenAI Whisper.

---

## Features

- Automatically detects audio formats: mp3 / wav / m4a / flac / ogg
- Automatically selects CPU or GPU
- Uses Whisper medium model for high-quality transcription
- Outputs transcription to `output.txt`
- Clean and simple code structure, easy to extend

---

## Directory Structure

```
whisper-ar/
│── speech2text.py
│── README.md
└── .gitignore
```

---

## Installation

### GPU version (recommended if using NVIDIA CUDA)

```
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install openai-whisper
```

### CPU version

```
pip install torch torchvision torchaudio
pip install openai-whisper
```

---

## Usage

### 1. Place your audio file in the same folder and name it as one of:

```
input.mp3
input.wav
input.m4a
input.flac
input.ogg
```

### 2. Run the program:

```
python speech2text.py
```

### 3. Output file:

```
output.txt
```

---

## Main Script (speech2text.py)

```python
import whisper, torch, os

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Current device: {device} ({torch.cuda.get_device_name(0) if device=='cuda' else 'CPU'})")

base_dir = os.path.dirname(os.path.abspath(__file__))

possible_exts = [".mp3", ".wav", ".m4a", ".flac", ".ogg"]
audio_path = None
for ext in possible_exts:
    path = os.path.join(base_dir, f"input{ext}")
    if os.path.exists(path):
        audio_path = path
        break

if not audio_path:
    print("Audio file not found. Please place an input audio file (e.g., input.mp3) in the same directory.")
    exit()

print(f"Audio file detected: {audio_path}")
model = whisper.load_model("medium", device=device)
print("Transcribing...")

try:
    result = model.transcribe(audio_path, language="ar")
    with open(os.path.join(base_dir, "output.txt"), "w", encoding="utf-8") as f:
        f.write(result["text"])
    print("Transcription completed. Result saved to output.txt")
except Exception as e:
    print("Transcription error:", e)
```

---

## .gitignore

```
*.mp3
*.wav
*.m4a
*.flac
*.ogg

output.txt

__pycache__/
*.pyc

*.pt
*.pth
```

---
