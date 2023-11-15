# Speech Pronunciation and Filler Word Detection

This project is designed to detect pronunciation errors and filler words in spoken language. It utilizes advanced speech processing models to convert speech into text and phonemes, and then analyses these outputs to identify any discrepancies or issues.

## Features
Speech to Text Conversion: Leverages the power of the Whisper model to accurately transcribe spoken language into text.
Speech to Phoneme Transcription: Uses Wav2Vec2Phoneme for precise conversion of speech into phonetic representations.
Pronunciation Error Detection: Employs a phoneme dictionary to identify pronunciation errors in the decoded phonemes.
Filler Word Identification: Utilizes a blacklist of filler words to spot unnecessary fillers in the transcribed text.

## How It Works
Speech to Text: The audio input is first processed by the Whisper model, which transcribes the speech into text. This text is then analyzed to detect filler words based on a predefined blacklist.

Speech to Phoneme: Simultaneously, the Wav2Vec2Phoneme model converts the speech into its phonemic form. This phonetic transcription is compared against a standard phoneme dictionary to identify any pronunciation errors.

Error and Filler Word Reporting: The system outputs a report highlighting any detected pronunciation errors and filler words, providing valuable feedback for speech improvement.

## Dependencies
pip install transformers datasets evaluate jiwer accelerate librosa soundfile

