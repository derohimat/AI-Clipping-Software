import whisper
import torch
import os
from config import WHISPER_MODEL

class WhisperSingleton:
    """
    A singleton class for transcribing audio using the openai-whisper library.

    This class ensures that the Whisper model is loaded only once and provides
    a method to transcribe audio from a video file.
    """
    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_model()
        return cls._instance

    def _load_model(self):
        """Loads the openai-whisper model with optimized settings."""
        if self._model is None:
            print(f"Loading openai-whisper model ({WHISPER_MODEL})... (one time only)")
            try:
                # Check if CUDA is available
                device = "cuda" if torch.cuda.is_available() else "cpu"
                
                # Load the model
                self._model = whisper.load_model(WHISPER_MODEL, device=device)
                print(f"✅ openai-whisper model loaded and cached on: {device}")
            except Exception as e:
                print(f"Error loading model: {e}")
                # Fallback to base model
                self._model = whisper.load_model("base", device="cpu")
                print(f"✅ Loaded fallback base model on CPU")


    def transcribe(self, video_path):
        """
        Transcribes the audio from a video file.

        Args:
            video_path (str): The path to the video file.

        Returns:
            tuple: A tuple containing a list of words with timestamps, the full
                   transcript, and a list of segments.
        """
        print("🎵 Transcribing video...")
        try:
            print("⏳ Initializing transcription with openai-whisper...")
            print("⏳ Starting audio processing (this may take a while)...")
            
            # Transcribe with word timestamps
            result = self._model.transcribe(
                str(video_path),
                word_timestamps=True,
                language="en",
                verbose=False
            )
            print("✅ Audio processing complete, now extracting words and segments...")
            
            # Process segments and words
            words = []
            segments_list = []
            full_text = result.get("text", "")
            
            segment_count = 0
            
            print("⏳ Processing transcription segments...")
            for segment in result.get("segments", []):
                segment_count += 1
                if segment_count % 10 == 0:
                    print(f"⏳ Processed {segment_count} segments so far...")
                    
                segments_list.append({
                    'id': segment.get('id', segment_count - 1),
                    'start': segment.get('start', 0),
                    'end': segment.get('end', 0),
                    'text': segment.get('text', '')
                })
                
                # Extract word timestamps
                for word_info in segment.get('words', []):
                    word = word_info.get('word', '').strip().upper()
                    if word:
                        words.append({
                            'word': word,
                            'start': word_info.get('start', 0),
                            'end': word_info.get('end', 0)
                        })
            
            print(f"✅ Transcription complete! Found {len(words)} words in {len(segments_list)} segments")
            print(f"📝 Transcript length: {len(full_text)} characters")
            return words, full_text, segments_list

        except Exception as e:
            print(f"❌ Transcription failed: {e}")
            return [], "", []
