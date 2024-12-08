import subprocess
import threading


def execute_ffmpeg(command, output_file):
    subprocess.run(command, check=True)
    print(f"Saved GIF segment to {output_file}")


def extract_video_segments_as_gif(input_file, output_folder, segments):
    """
    Extracts specified parts of a video and saves them as GIFs using FFmpeg for speed.
    """

    threads = []

    try:
        for idx, (start, end, emote_name) in enumerate(segments):
            output_file = f"{output_folder}/{emote_name}.gif"
            print(f"Processing segment {idx + 1}: {start}s to {end}s")

            # Use FFmpeg to extract the segment and convert to GIF
            command = [
                "ffmpeg",
                "-ss", str(start),  # Start time
                "-to", str(end),    # End time
                "-i", input_file,   # Input file,
                "-lavfi", "minterpolate=fps=20,scale=600:-2:flags=lanczos,setpts=1.3*PTS",
                "-c:v", "gif",  # Use H.265 codec
                output_file,         # Output file
                "-y"
            ]

            thread = threading.Thread(
                target=execute_ffmpeg, kwargs={'command': command, 'output_file': output_file}
            )
            thread.start()
            threads.append(thread)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

    for thread in threads:
        thread.join()


gifs = [
    (1, 3, "Ridicle"),
    (4, 6, "Threaten"),
    (8, 9, "Applause")
]


def main():
    input_video = "video.webm"
    output_folder = "images/gifs"
    time_ranges = gifs  # Specify time ranges
    extract_video_segments_as_gif(input_video, output_folder, time_ranges)


if __name__ == "__main__":
    main()
