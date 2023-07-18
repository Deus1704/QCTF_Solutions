from pydub import AudioSegment
# Replace 'file_path' with the actual path to your file
file_path = 'binval.bin'

# Read the file as binary data
with open(file_path, 'rb') as file:
    binary_data = file.read()

# Continue with the code to process the binary_data
# using the provided code snippets in previous responses

# Replace 'binary_audio_data' with your actual binary audio data
# 'sample_rate' and 'bit_depth' with the values you identified or know
sample_rate= 44100
sample_wd=2
chann=1
extra_bytes = len(binary_data) % (sample_wd * chann)
print(extra_bytes)
if extra_bytes > 0:
    # Add zero padding at the end to align the data correctly
    binary_data += b'\x00' * (sample_wd * chann - extra_bytes)
audio_segment = AudioSegment(
    data= binary_data,
    sample_width=sample_wd,  # 2 bytes (16 bits) for 16-bit audio (adjust if different)
    frame_rate=sample_rate,
    channels=chann  # Mono channel
)

audio_segment.export("outputfinaltry.wav", format="wav")
