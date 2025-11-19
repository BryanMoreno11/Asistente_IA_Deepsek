# Banano Bot Tests

This project uses a DeepSeek model for answering questions. The API key is read from environment variables through `config.py`.

## Setup

1. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
   Whisper requires FFmpeg. On Debian/Ubuntu you can install it with:
   ```bash
   sudo apt-get install ffmpeg
   ```
2. Create a `.env` file or set environment variables in your shell. At minimum, define your DeepSeek API key:
   ```bash
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   ```

Start the backend with:
```bash
python backend_run.py
```

## Audio transcription example

A sample audio file `sample_question_es.mp3` is provided. You can transcribe it and query the RAG pipeline with:
```bash
python pruebas_local/test_whisper_to_llm.py
```
This will print the transcribed question and the model's answer.