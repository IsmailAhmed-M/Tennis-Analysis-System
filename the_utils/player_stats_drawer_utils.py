
# import numpy as np
# import cv2

# def draw_player_stats(output_video_frames,player_stats):

#     for index, row in player_stats.iterrows():
#         player_1_shot_speed = row['player_1_last_shot_speed']
#         player_2_shot_speed = row['player_2_last_shot_speed']
#         player_1_speed = row['player_1_last_player_speed']
#         player_2_speed = row['player_2_last_player_speed']

#         avg_player_1_shot_speed = row['player_1_average_shot_speed']
#         avg_player_2_shot_speed = row['player_2_average_shot_speed']
#         avg_player_1_speed = row['player_1_average_player_speed']
#         avg_player_2_speed = row['player_2_average_player_speed']

#         frame = output_video_frames[index]
#         shapes = np.zeros_like(frame, np.uint8)

#         width=210
#         height=120

#         start_x = frame.shape[1]-220
#         start_y = frame.shape[0]-450
#         end_x = start_x+width
#         end_y = start_y+height

#         overlay = frame.copy()
#         cv2.rectangle(overlay, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
#         alpha = 0.5 
#         cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
#         output_video_frames[index] = frame

#         text = "    Player 1    Player 2"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+40, start_y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (255, 255, 255), 1)
        
#         text = "Shot Speed"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+5, start_y+40), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 255, 255), 1)
#         text = f"{player_1_shot_speed:.1f} km/h    {player_2_shot_speed:.1f} km/h"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+65, start_y+40), cv2.FONT_HERSHEY_SIMPLEX, 0.30, (255, 255, 255), 1)

#         text = "Player Speed"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+5, start_y+60), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 255, 255), 1)
#         text = f"{player_1_speed:.1f} km/h    {player_2_speed:.1f} km/h"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+65, start_y+60), cv2.FONT_HERSHEY_SIMPLEX, 0.30, (255, 255, 255), 1)
        
        
#         text = "avg. S. Speed"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+5, start_y+80), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 255, 255), 1)
#         text = f"{avg_player_1_shot_speed:.1f} km/h    {avg_player_2_shot_speed:.1f} km/h"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+65, start_y+80), cv2.FONT_HERSHEY_SIMPLEX, 0.30, (255, 255, 255), 1)
        
#         text = "avg. P. Speed"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+5, start_y+100), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (255, 255, 255), 1)
#         text = f"{avg_player_1_speed:.1f} km/h    {avg_player_2_speed:.1f} km/h"
#         output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+65, start_y+100), cv2.FONT_HERSHEY_SIMPLEX, 0.30, (255, 255, 255), 1)
    
#     return output_video_frames


import numpy as np
import cv2

def draw_player_stats(output_video_frames,player_stats):

    for index, row in player_stats.iterrows():
        player_1_shot_speed = row['player_1_last_shot_speed']
        player_2_shot_speed = row['player_2_last_shot_speed']
        player_1_speed = row['player_1_last_player_speed']
        player_2_speed = row['player_2_last_player_speed']

        avg_player_1_shot_speed = row['player_1_average_shot_speed']
        avg_player_2_shot_speed = row['player_2_average_shot_speed']
        avg_player_1_speed = row['player_1_average_player_speed']
        avg_player_2_speed = row['player_2_average_player_speed']

        frame = output_video_frames[index]
        shapes = np.zeros_like(frame, np.uint8)

        width = 320
        height = 180

        start_x = frame.shape[1]-350
        start_y = frame.shape[0]-700
        end_x = start_x+width
        end_y = start_y+height

        overlay = frame.copy()
        cv2.rectangle(overlay, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
        alpha = 0.5 
        cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)
        output_video_frames[index] = frame

        text = "   Player 1    Player 2"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+80, start_y+45), cv2.FONT_HERSHEY_SIMPLEX, 0.50, (255, 255, 255), 1)
        
        text = "Shot Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+75), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 1)
        text = f"{player_1_shot_speed:.1f} km/h    {player_2_shot_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+110, start_y+75), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)

        text = "Player Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+100), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 255, 255), 1)
        text = f"{player_1_speed:.1f} km/h    {player_2_speed:.1f}  km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+110, start_y+100), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        
        
        text = "avg. S. Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+125), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 255, 255), 1)
        text = f"{avg_player_1_shot_speed:.1f} km/h    {avg_player_2_shot_speed:.1f} km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+110, start_y+125), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
        
        text = "avg. P. Speed"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+10, start_y+150), cv2.FONT_HERSHEY_SIMPLEX, 0.40, (255, 255, 255), 1)
        text = f"{avg_player_1_speed:.1f} km/h    {avg_player_2_speed:.1f}  km/h"
        output_video_frames[index] = cv2.putText(output_video_frames[index], text, (start_x+110, start_y+150), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    
    return output_video_frames
