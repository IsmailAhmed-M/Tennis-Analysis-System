import cv2

# Function to read video frames from a given video path
def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    original_fps = cap.get(cv2.CAP_PROP_FPS)  
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames, original_fps

# Function to save processed video frames to a new video file
def save_video(output_video_frames, output_video_path, fps):
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))

    # Write each frame to the output video file
    for frame in output_video_frames:
        out.write(frame)
    out.release() # Release the VideoWriter object after writing is done