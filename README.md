# 🎥 AI Video Assistant using RAG

An AI-powered Video Assistant that allows users to analyze YouTube videos or local audio/video files using Retrieval-Augmented Generation (RAG). The application automatically extracts audio, transcribes speech, builds a searchable knowledge base, and enables natural language conversations with the video content.

---

## 🚀 Features

- 🎬 Process YouTube videos using URL input
- 📁 Support for local audio and video files
- 🎙️ Automatic audio extraction and preprocessing
- 📝 Speech-to-text transcription using Whisper
- 📚 Retrieval-Augmented Generation (RAG)
- 💬 Ask questions about the video
- 📄 AI-generated summaries
- ⚡ Interactive Streamlit interface
- 🔍 Semantic search over transcript chunks

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- OpenAI GPT
- OpenAI Whisper
- ChromaDB
- yt-dlp
- FFmpeg
- Pydub

---

## 📂 Project Workflow

```text
YouTube URL / Local Video
            │
            ▼
    Audio Extraction (yt-dlp / FFmpeg)
            │
            ▼
      Audio Preprocessing
            │
            ▼
 Whisper Speech-to-Text
            │
            ▼
 Transcript Chunking
            │
            ▼
 Generate Embeddings
            │
            ▼
      Store in ChromaDB
            │
            ▼
      User Question
            │
            ▼
     Retrieve Relevant Chunks
            │
            ▼
      GPT Response Generation
            │
            ▼
      Final Answer
```

---

## 📸 Screenshots

### Home Page

> Add screenshot here

### AI Response

> Add screenshot here

### Generated Summary

> Add screenshot here

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Dakshp17/AI-Video-Assistant-using-RAG.git
```

Move into the project

```bash
cd AI-Video-Assistant-using-RAG
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

```env
OPENAI_API_KEY=your_api_key
```

If downloading YouTube videos requires authentication, export your YouTube cookies using the **Get cookies.txt LOCALLY** browser extension and place the `cookies.txt` file in the project root.

> **Note:** Never upload `cookies.txt` or `.env` to GitHub.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
AI-Video-Assistant-using-RAG
│
├── app.py
├── audio_processing.py
├── transcriber.py
├── rag.py
├── llm.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
└── ...
```

---

## 📌 Future Improvements

- Speaker Diarization
- Timestamp-based Question Answering
- PDF Summary Export
- Multi-language Support
- Video Chapter Detection
- Deploy on Streamlit Cloud
- Multiple LLM Support

---

## 👨‍💻 Author

**Daksh Patel**

GitHub: https://github.com/Dakshp17

---

## ⭐ If you found this project useful

Please consider giving the repository a ⭐.
