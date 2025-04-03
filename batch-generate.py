import subprocess

# Paths to reference audio and reference text
reference_audio = "voices/voice-profiles/lwong1.wav"
reference_text = "Our aim is to provide support, to help Singaporeans through and help them tackle these cost pressures. We found CDC vouchers to be quite effective, we started this like I said a few years ago. It was well received by families. It helped families get through difficult times."

# Read the corpus
with open("corpus1.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip()]

# # Limit to 10 lines
# lines = lines[:10]

# Loop through each line and run the command
for i, text in enumerate(lines, 1):
    output_file = f"generated{i}"
    cmd = [
        "python", "-m", "tools.api_client",
        "--text", text,
        "--reference_audio", reference_audio,
        "--reference_text", reference_text,
        "--streaming", "False",
        "--output", output_file,
        "--format", "wav"
    ]
    print(cmd)
    print(f"Running command for line {i}: {text}")
    subprocess.run(cmd)
