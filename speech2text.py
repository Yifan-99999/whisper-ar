import whisper, torch, os

device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"当前设备: {device} ({torch.cuda.get_device_name(0) if device=='cuda' else 'CPU'})")

base_dir = os.path.dirname(os.path.abspath(__file__))

possible_exts = [".mp3", ".wav", ".m4a", ".flac", ".ogg"]
audio_path = None
for ext in possible_exts:
    path = os.path.join(base_dir, f"input{ext}")
    if os.path.exists(path):
        audio_path = path
        break

if not audio_path:
    print("未找到 input 音频文件，请确保与脚本在同一文件夹，例如 input.mp3。")
    exit()

print(f"找到音频文件：{audio_path}")
model = whisper.load_model("medium", device=device)
print("开始识别中...")
try:
    result = model.transcribe(audio_path, language="ar")
    with open(os.path.join(base_dir, "output.txt"), "w", encoding="utf-8") as f:
        f.write(result["text"])
    print("识别完成，结果已保存到 output.txt")
except Exception as e:
    print("识别出错：", e)
