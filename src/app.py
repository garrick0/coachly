from flask import Flask, jsonify, request
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
import torch
from datasets import load_dataset


device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

model_id = "openai/whisper-large-v3"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    chunk_length_s=30,
    batch_size=16,
    return_timestamps=True,
    torch_dtype=torch_dtype,
    device=device,
)



app = Flask(__name__)


#transcribe
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():

    # Check if a file is part of the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']

    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Read the file (assuming it's an audio file)
        audio_input = file.read()

        # Process the audio file with Whisper
        transcription_result = pipe(audio_input)

        # Return the transcription result as JSON
        return jsonify(transcription_result)
        


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
