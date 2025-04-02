import subprocess

# Step 1: Generate semantic codes from a wav file
subprocess.run([
    "python", "fish_speech/models/vqgan/inference.py",
    "-i", "voice-profiles/lwong1.wav",
    "--checkpoint-path", "checkpoints/fish-speech-1.5/firefly-gan-vq-fsq-8x1024-21hz-generator.pth"
])

# Step 2: Convert text to semantic tokens
subprocess.run([
    "python", "fish_speech/models/text2semantic/inference.py",
    "--text", "The text you want to convert",
    "--prompt-text", "Our aim is to provide support, to help Singaporeans through and help them tackle these cost pressures. We found CDC vouchers to be quite effective.",
    "--prompt-tokens", "fake.npy",
    "--checkpoint-path", "checkpoints/fish-speech-1.5",
    "--num-samples", "2",
    "--compile"
])

# Step 3: Decode semantic tokens back into audio
subprocess.run([
    "python", "fish_speech/models/vqgan/inference.py",
    "-i", "codes_1.npy",
    "--checkpoint-path", "checkpoints/fish-speech-1.5/firefly-gan-vq-fsq-8x1024-21hz-generator.pth"
])
