import cv2
import os

def create_output_folder(output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def get_video_properties(video_capture):
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))
    return total_frames, fps

def save_frame(frame, output_folder, frame_index):
    frame_filename = f"frame_{frame_index:04d}.jpg"
    frame_path = os.path.join(output_folder, frame_filename)
    cv2.imwrite(frame_path, frame)

def extract_frames(video_path, output_folder, frame_interval=1):
    create_output_folder(output_folder)

    video_capture = cv2.VideoCapture(video_path)
    total_frames, fps = get_video_properties(video_capture)
    interval_in_frames = int(fps * frame_interval)

    frame_index = 0
    extracted_frames = 0

    while frame_index < total_frames:
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        success, frame = video_capture.read()

        if not success:
            break

        save_frame(frame, output_folder, extracted_frames)
        frame_index += interval_in_frames
        extracted_frames += 1

    video_capture.release()
    print(f"Extracted {extracted_frames} frames to {output_folder}")

if __name__ == "__main__":
    video_path = 'video.mp4'
    output_folder = 'extracted_frames'
    frame_interval = 1  # Extract one frame per second
    extract_frames(video_path, output_folder, frame_interval)
