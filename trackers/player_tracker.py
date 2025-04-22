from ultralytics import YOLO
import cv2
import pickle
import sys
sys.path.append('../')
from the_utils import measure_distance, get_center_of_bbox

class PlayerTracker:

    def __init__(self, model_path):
        self.model = YOLO(model_path)
        self.prev_p1, self.prev_p2 = None, None  # Store previous player positions

    def choose_and_filter_players(self, court_keypoints, player_detections):
        player_detections_first_frame = player_detections[0]
        chosen_player = self.choose_players(court_keypoints, player_detections_first_frame)
        filtered_player_detections = []
        for player_dict in player_detections:
            filtered_player_dict = {track_id: bbox for track_id, bbox in player_dict.items() if track_id in chosen_player}
            filtered_player_detections.append(filtered_player_dict)
        return filtered_player_detections

    def choose_players(self, court_keypoints, player_dict):
        distances = []
        for track_id, bbox in player_dict.items():
            player_center = get_center_of_bbox(bbox)

            min_distance = float('inf')
            for i in range(0, len(court_keypoints), 2):
                court_keypoint = (court_keypoints[i], court_keypoints[i + 1])
                distance = measure_distance(player_center, court_keypoint)
                if distance < min_distance:
                    min_distance = distance
            distances.append((track_id, min_distance))
        
        # Sort Distances in asc
        distances.sort(key=lambda x: x[1])
        # choose the first two tracks
        chosen_players = [distances[0][0], distances[1][0]]
        return chosen_players


    def detect_frames(self, frames, read_from_stub = False, stub_path = None):
        player_detections = []

        if read_from_stub and stub_path is not None:
            with open(stub_path, 'rb') as f:
                player_detections = pickle.load(f)
            return player_detections

        for frame in frames:
            player_dict = self.detect_frame(frame)
            player_detections.append(player_dict)

        if stub_path is not None:
            with open(stub_path, 'wb') as f:
                pickle.dump(player_detections, f)

        return player_detections

    def detect_frame(self, frame):
        results = self.model.track(frame, persist=True)[0]
        id_name_dict = results.names

        # Define court zones
        h, w, _ = frame.shape
        lower_court, upper_court = int(h * 0.60), int(h * 0.40)

        lower, upper = [], []  # Separate detections based on y-coordinates

        for box in results.boxes:
            if box.id is None:  
                continue  # Skip if no ID is assigned

            track_id = int(box.id.tolist()[0])
            result = box.xyxy.tolist()[0]
            object_cls_id = int(box.cls.tolist()[0])  # Ensure it's an integer
            object_cls_name = id_name_dict.get(object_cls_id, "Unknown")

            if object_cls_name == "person":
                x1, y1, x2, y2 = result
                bbox_center_y = (y1 + y2) / 2  # Get vertical center of bounding box

                if bbox_center_y > lower_court:
                    lower.append((track_id, result))  # Player 1 (near bottom)
                elif bbox_center_y < upper_court:
                    upper.append((track_id, result))  # Player 2 (near top)

        # Assign players based on closest match
        p1 = max(lower, key=lambda b: b[1][1], default=(None, None))[1] or self.prev_p1
        p2 = min(upper, key=lambda b: b[1][1], default=(None, None))[1] or self.prev_p2
        self.prev_p1, self.prev_p2 = p1, p2  # Update previous positions

        return {1: p1, 2: p2} if p1 and p2 else {}  # Assign fixed IDs to prevent audience tracking
    
    
    def draw_bboxes(self, video_frames, player_detections):
        output_video_frames = []
        for frame, player_dict in zip(video_frames, player_detections):
            for player_id, bbox in player_dict.items():
                if bbox is None:
                    continue
                x1, y1, x2, y2 = bbox
            
            # Set text color to red (BGR: (0, 0, 255))
                cv2.putText(frame, f"Player {player_id}", (int(x1), int(y1 - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            
            # Set bounding box color to red (BGR: (0, 0, 255))
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)

            output_video_frames.append(frame)
    
        return output_video_frames

