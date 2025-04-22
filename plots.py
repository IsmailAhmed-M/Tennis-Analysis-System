from trackers import BallTracker
import matplotlib.pyplot as plt
import pickle
import pandas as pd
import seaborn as sns

ball_tracker = BallTracker(model_path='models/yolo5_last.pt')

# Load ball_detections from the pickle file
# with open('outputs/ball_detections.pkl', 'rb') as f:
#     ball_detections = pickle.load(f)

df_ball_positions = pd.read_pickle("analysis/dataframe/df_ball_positions.pkl")

# Load player_detections from the pickle file

df_player_positions = pd.read_pickle("analysis/dataframe/df_players_positions.pkl")

def generate_ball_heatmap(df_ball_positions, save_path="outputs/heatmap.png"):
    # Make sure center_x and center_y exist
    if 'center_x' not in df_ball_positions or 'center_y' not in df_ball_positions:
        df_ball_positions['center_x'] = (df_ball_positions['x1'] + df_ball_positions['x2']) / 2
        df_ball_positions['center_y'] = (df_ball_positions['y1'] + df_ball_positions['y2']) / 2

    plt.figure(figsize=(10, 6))
    sns.kdeplot(
        x=df_ball_positions['center_x'],
        y=df_ball_positions['center_y'],
        cmap='Reds',
        fill=True,
        thresh=0.05,
        bw_adjust=1.2,
        shade=True
    )
    plt.title("Ball Movement Heatmap")
    plt.xlabel("X Position (pixels)")
    plt.ylabel("Y Position (pixels)")
    plt.gca().invert_yaxis()  # Flip vertically if video origin is top-left
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()

# ball_shot_frames = ball_tracker.get_ball_shot_frames(ball_detections)
# print(ball_shot_frames)

def generate_player_heatmaps(df_player_positions, save_path="outputs/player_heatmaps.png"):
    
    #Generate heatmaps for two players and save the image to `save_path`.
    
    # Set plot style
    # Set plot style
    sns.set(style="white")

    plt.figure(figsize=(8,8))
    
    # Player 1 Heatmap (bottom court)
    sns.kdeplot(
        data = df_player_positions[df_player_positions['player_id'] == 1],
        x="center_x", y="center_y",
        fill=True, cmap="Reds", alpha=0.7, bw_adjust=0.5,
        label="Player 1"
    )

    # Player 2 Heatmap (top court)
    sns.kdeplot(
        data=df_player_positions[df_player_positions['player_id'] == 2],
        x="center_x", y="center_y",
        fill=True, cmap="Blues", alpha=0.7, bw_adjust=0.5,
        label="Player 2"
    )

    # Invert y-axis so that top of plot is top of court
    plt.gca().invert_yaxis()

    # Optional: Set court dimensions (adjust based on your data range)
    plt.xlim(0, 1280)
    plt.ylim(720, 0)  # Top to bottom

    plt.title("Player Movement Heatmap on Tennis Court")
    plt.xlabel("Court Width (pixels)")
    plt.ylabel("Court Height (pixels)")
    plt.legend()

    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    plt.close()