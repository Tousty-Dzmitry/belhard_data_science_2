# import os
# from app.models.yolo_wrapper import (
#     load_model,
#     detect_on_video,
#     generate_voice_alert,
#     add_alerts_to_video
# )

# model = load_model()

# def process_video(input_path, output_path):
#     alert_audio = "drone_alert.wav"
#     temp_output = output_path.replace(".mp4", "_no_audio.mp4")
#     final_output = output_path

#     generate_voice_alert(alert_audio)
#     alert_times = detect_on_video(model, input_path, temp_output)  # убрал лишний аргумент
#     add_alerts_to_video(temp_output, alert_times, final_output, alert_audio)  # порядок аргументов правильный

#     return final_output

import os
from app.models.yolo_wrapper import load_model, detect_on_video

model = load_model()

def process_video(input_path, output_path):
    # просто вызываем детектор, без озвучки и аудио
    detect_on_video(model, input_path, output_path)
    return output_path
