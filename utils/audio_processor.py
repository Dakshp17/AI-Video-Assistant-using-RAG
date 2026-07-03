import yt_dlp
import os
import subprocess

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def download_youtube_audio(url: str) -> str:
    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best/best",
        "outtmpl": output_path,
        "noplaylist": True,
        "quiet": False,

        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ]
    }

    if os.path.exists("cookies.txt"):
        ydl_opts["cookiefile"] = "cookies.txt"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

        filename = ydl.prepare_filename(info)

        filename = (
            filename.replace(".webm", ".wav")
                    .replace(".m4a", ".wav")
                    .replace(".mp4", ".wav")
        )

    return filename


def convert_to_wav(input_path: str) -> str:
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"

    command = [
        "ffmpeg",
        "-y",
        "-i",
        input_path,
        "-ac",
        "1",
        "-ar",
        "16000",
        output_path,
    ]

    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    return output_path


def chunk_audio(wav_path: str, chunk_minutes: int = 10) -> list:

    chunk_seconds = chunk_minutes * 60

    output_pattern = os.path.splitext(wav_path)[0] + "_chunk_%03d.wav"

    command = [
        "ffmpeg",
        "-y",
        "-i",
        wav_path,
        "-f",
        "segment",
        "-segment_time",
        str(chunk_seconds),
        "-c",
        "copy",
        output_pattern,
    ]

    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True,
    )

    folder = os.path.dirname(wav_path)

    base = os.path.splitext(os.path.basename(wav_path))[0]

    chunks = sorted([
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.startswith(base + "_chunk_") and f.endswith(".wav")
    ])

    return chunks


def process_input(source: str):

    if source.startswith("http://") or source.startswith("https://"):
        print("Downloading YouTube Audio...")
        wav_path = download_youtube_audio(source)
    else:
        print("Converting Local File...")
        wav_path = convert_to_wav(source)

    print("Chunking Audio...")
    chunks = chunk_audio(wav_path)

    print(f"{len(chunks)} chunks created.")

    return chunks