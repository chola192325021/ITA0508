import cv2

def process_and_save_video(video_path, output_path, speed=1.0):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Cannot open video file.")
        return

    # Get original video properties
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Adjust fps based on speed for saving
    new_fps = max(1, fps * speed)  # Avoid fps = 0

    out = cv2.VideoWriter(output_path, fourcc, new_fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Show video
        cv2.imshow(f"Playing at {speed}x speed", frame)

        # Write frame
        out.write(frame)

        # Wait key adjusted to playback speed
        delay = int(1000 / (fps * speed))  # in ms
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Saved video as '{output_path}' at {speed}x speed.")

# === USAGE ===
input_video = "your_video.mp4"  # Replace with your file

# Normal speed
process_and_save_video(input_video, "output_normal.mp4", speed=1.0)

# Slow motion (0.5x)
process_and_save_video(input_video, "output_slow.mp4", speed=0.5)

# Fast motion (2x)
process_and_save_video(input_video, "output_fast.mp4", speed=2.0)
