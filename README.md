# YouTube Viral Clipper

**Transform any YouTube video into captivating, shareable short-form clips with the YouTube Viral Clipper.** This free and open-source software leverages AI to automate the entire video clipping process, making viral content creation accessible to everyone.

## Features

- **AI-Powered Clip Selection**: Automatically identifies the most engaging and viral-worthy moments in a video.
- **Smart Face Tracking**: Keeps the speaker perfectly framed, even in dynamic scenes.
- **Engaging Captions**: Adds word-by-word captions in various styles to boost viewer retention.
- **Easy Configuration**: Simple setup with a `.env` file for your API keys and preferences.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/youtube-viral-clipper.git
   cd youtube-viral-clipper
   ```

2. **Create a virtual environment (recommended):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or on Windows: venv\Scripts\activate
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   **Note for macOS users:** If you encounter issues, make sure you have `pkg-config` and `ffmpeg` installed:

   ```bash
   brew install pkg-config ffmpeg
   ```

4. **Configure your environment:**
   Copy the `.env.example` file to `.env` and add your Gemini API key.

   ```bash
   cp .env.example .env
   ```

   Open the `.env` file and add your API key:

   ```
   GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
   ```

   **Need help getting an API key?** See the [Gemini API Setup Guide](GEMINI_API_SETUP.md) for detailed instructions.

## Usage

**Option 1: Using the convenience script (recommended):**

```bash
./run.sh
```

**Option 2: Manual activation:**

```bash
source venv/bin/activate  # Activate virtual environment first
python main.py
```

The script will prompt you for the YouTube URL and other options. The generated clips will be saved in the `clips` directory.

## Troubleshooting

If you encounter issues downloading YouTube videos, try the following:

- **Use a custom user agent**: Set a custom user agent in your `.env` file to improve download reliability.
- **Update pytubefix**: YouTube frequently changes its platform, so keeping `pytubefix` updated can help:

  ```bash
  source venv/bin/activate
  pip install -U pytubefix
  ```

- **Check video availability**: Ensure the video is publicly available and not age-restricted or private.
