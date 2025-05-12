import numpy as np
import cv2

# Function to overlay player statistics on video frames
def draw_player_stats(output_video_frames,player_stats):

    for index, row in player_stats.iterrows():
        # Extract the latest shot speed and player speed for each player
        player_1_shot_speed = row['player_1_last_shot_speed']
        player_2_shot_speed = row['player_2_last_shot_speed']
        player_1_speed = row['player_1_last_player_speed']
        player_2_speed = row['player_2_last_player_speed']

        # Extract average shot and player speeds for each player
        avg_player_1_shot_speed = row['player_1_average_shot_speed']
        avg_player_2_shot_speed = row['player_2_average_shot_speed']
        avg_player_1_speed = row['player_1_average_player_speed']
        avg_player_2_speed = row['player_2_average_player_speed']

        frame = output_video_frames[index]
        shapes = np.zeros_like(frame, np.uint8)

        # Set dimensions and position of the overlay box
        width = 320
        height = 180

        start_x = frame.shape[1]-350
        start_y = frame.shape[0]-700
        end_x = start_x+width
        end_y = start_y+height

        # Create a semi-transparent black rectangle as background for text
        overlay = frame.copy()
        cv2.rectangle(overlay, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
        alpha = 0.5 # Transparency factor
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
        output_video_frames[index] = frame

        text = "   Player 1    Player 2"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+80, start_y+45), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (255, 255, 255), 1)
        
        # Last shot speed       
        text = "Shot Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+75), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        text = f"{player_1_shot_speed:.1f} km/h    {player_2_shot_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+110, start_y+75), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        
        # Last player speed
        text = "Player Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+100), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 255, 255), 1)
        text = f"{player_1_speed:.1f} km/h    {player_2_speed:.1f}  km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+110, start_y+100), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        
        
        # Average shot speed        
        text = "avg. S. Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+125), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 255, 255), 1)
        text = f"{avg_player_1_shot_speed:.1f} km/h    {avg_player_2_shot_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+110, start_y+125), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        
        # Average player speed        
        text = "avg. P. Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+150), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 255, 255), 1)
        text = f"{avg_player_1_speed:.1f} km/h    {avg_player_2_speed:.1f}  km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+110, start_y+150), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    
    return output_video_frames
