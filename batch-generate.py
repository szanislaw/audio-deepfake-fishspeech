import subprocess

# Paths to reference audio and reference text
reference_audio = "voice-profiles/gracefu1.wav"
reference_text = "Miss Lim was suggesting that the government would have raised the GST immediately, if not for the adverse public reaction when it floated the suggestion late last year, and if, it had not been stuck with the previous statement that it had enough money"

# Read the corpus
with open("corpus.txt", "r", encoding="utf-8") as f:
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
