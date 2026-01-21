# Gemini API Setup Guide

This guide will help you get your Gemini API key for the YouTube Viral Clipper.

## What is the Gemini API used for?

The Gemini API is used to analyze video transcripts and intelligently select the most viral-worthy clips. It:

- Analyzes the content for engaging moments
- Identifies hooks, revelations, and quotable moments
- Scores each potential clip for virality (0-100)
- Selects complete thoughts (no mid-sentence cuts)

## Getting Your API Key

### Step 1: Visit Google AI Studio

Go to [Google AI Studio](https://aistudio.google.com/app/apikey)

### Step 2: Sign in with your Google Account

Use any Google account (Gmail, Workspace, etc.)

### Step 3: Create an API Key

1. Click on **"Get API key"** or **"Create API key"**
2. Choose **"Create API key in new project"** (recommended for first-time users)
3. Copy the generated API key

### Step 4: Add to Your Project

1. Open the `.env` file in your project directory
2. Replace `YOUR_GEMINI_API_KEY` with your actual API key:

```bash
GEMINI_API_KEY="AIzaSy..."  # Your actual key here
```

## API Permissions & Requirements

### ✅ What's Included (No Extra Setup Needed)

- **Model Access**: The project uses `gemini-1.5-flash` which is available by default
- **Text Generation**: Automatically enabled for all API keys
- **JSON Output**: Supported out of the box
- **No OAuth Required**: Simple API key authentication

### 📊 Usage Limits (Free Tier)

As of 2024, the free tier includes:

- **15 requests per minute (RPM)**
- **1 million tokens per minute (TPM)**
- **1,500 requests per day (RPD)**

For this project:

- Each video analysis uses **1 API call**
- Typical token usage: **500-2000 tokens per video** (depending on transcript length)
- You can process **hundreds of videos per day** within free limits

### 🔒 Security Best Practices

1. **Never commit your API key to Git**
   - The `.env` file is already in `.gitignore`
   - Never share your `.env` file publicly

2. **Restrict your API key** (Optional but recommended):
   - Go to [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
   - Find your API key
   - Click "Edit API key"
   - Under "API restrictions", select "Restrict key"
   - Choose "Generative Language API"
   - Save

3. **Monitor usage**:
   - Check your usage at [Google AI Studio](https://aistudio.google.com/app/apikey)
   - Set up billing alerts if needed (for paid usage)

## Troubleshooting

### Error: "API key not valid"

- Make sure you copied the entire key (starts with `AIza...`)
- Check for extra spaces or quotes in your `.env` file
- Verify the key is active in Google AI Studio

### Error: "Quota exceeded"

- You've hit the free tier limit
- Wait for the quota to reset (usually 1 minute for RPM, 1 day for RPD)
- Consider upgrading to a paid plan if needed

### Error: "Model not found"

- The project uses `gemini-1.5-flash` which should be available by default
- If you see this error, try updating the `google-generativeai` package:

  ```bash
  source venv/bin/activate
  pip install -U google-generativeai
  ```

## Cost Information

### Free Tier (Recommended for Most Users)

- **Cost**: $0
- **Sufficient for**: Processing dozens of videos per day
- **No credit card required**

### Paid Tier (If You Need More)

- **Gemini 1.5 Flash**: $0.075 per 1M input tokens, $0.30 per 1M output tokens
- **Example**: Processing 100 videos (~150K tokens) = ~$0.01-0.05
- Very affordable for high-volume usage

## Additional Resources

- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [Pricing Information](https://ai.google.dev/pricing)
- [API Quotas & Limits](https://ai.google.dev/gemini-api/docs/quota)

## Need Help?

If you encounter any issues:

1. Check the error message in the terminal
2. Verify your API key is correctly set in `.env`
3. Ensure you're within the free tier limits
4. Check the [official documentation](https://ai.google.dev/docs)
