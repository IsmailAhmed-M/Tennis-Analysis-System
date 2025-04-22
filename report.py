from fpdf import FPDF
from plots import generate_ball_heatmap
from plots import generate_player_heatmaps
import datetime
import pandas as pd
import os

df_ball_positions = pd.read_pickle("analysis/dataframe/df_ball_positions.pkl")
df_player_positions = pd.read_pickle("analysis/dataframe/df_players_positions.pkl")

def generate_pdf_report(username, output_path="report.pdf"):

    generate_ball_heatmap(df_ball_positions, save_path="outputs/ball_heatmap.png")
    generate_player_heatmaps(df_player_positions, save_path="outputs/player_heatmaps.png")

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt=" Your Tennis Match Analysis Report", ln=True, align='C')

    pdf.set_font("Arial", size=11)
    pdf.cell(200, 10, txt=f"Generated for: {username}", ln=True)
    pdf.cell(200, 10, txt=f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, txt= "Ball Heatmap:", ln=True)

    # Heatmap Image
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Ball Movement Heatmap", ln=True, align="L")
    pdf.image("outputs/ball_heatmap.png", x=10, y=60, w=180)  # adjust position/size as needed

    pdf.add_page()

    # Add title
    pdf.ln(5)
    pdf.set_font("Arial", size=13)
    pdf.cell(200, 10, txt="Players Movement Heatmap:", ln=True, align="L")

    # Add the heatmap image
    pdf.image("outputs/player_heatmaps.png", x=10, y=40, w=180)  # Adjust x, y, w for positioning

    pdf.output(output_path)
    return output_path
