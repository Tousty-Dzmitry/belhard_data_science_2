# # import cv2
# # import os
# # import pyttsx3
# # import subprocess

# # def load_model():
# #     from ultralytics import YOLO
# #     model = YOLO("app/models/best.pt")
# #     model.fuse()
# #     return model

# # def generate_voice_alert(audio_path="drone_alert.wav"):
# #     if not os.path.exists(audio_path):
# #         engine = pyttsx3.init()
# #         engine.save_to_file("Обнаружен дрон", audio_path)
# #         engine.runAndWait()

# # def detect_on_video(model, input_path, output_path):
# #     cap = cv2.VideoCapture(input_path)
# #     out = None
# #     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# #     fps = cap.get(cv2.CAP_PROP_FPS)
# #     alert_times = set()
# #     frame_idx = 0

# #     while cap.isOpened():
# #         ret, frame = cap.read()
# #         if not ret:
# #             break

# #         results = model(frame)[0]

# #         for box in results.boxes:
# #             cls_id = int(box.cls[0])
# #             conf = float(box.conf[0])
# #             if cls_id == 0 and conf >= 0.83:
# #                 x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
# #                 cv2.rectangle(frame, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
# #                 cv2.putText(frame, "DRONE", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
# #                             fontScale=0.8, color=(0, 0, 255), thickness=2)
# #                 timestamp_ms = int((frame_idx / fps) * 1000)
# #                 alert_times.add(timestamp_ms)

# #         if out is None:
# #             h, w, _ = frame.shape
# #             out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

# #         out.write(frame)
# #         frame_idx += 1

# #     cap.release()
# #     if out:
# #         out.release()

# #     return sorted(alert_times)

# # def add_alerts_to_video(video_path: str, alert_times_ms: list[int], output_path: str, audio_path="drone_alert.wav"):
# #     if not alert_times_ms:
# #         os.rename(video_path, output_path)
# #         return

# #     alert_times_ms = sorted(set(alert_times_ms))
# #     grouped_alerts = [alert_times_ms[0]]
# #     for t in alert_times_ms[1:]:
# #         if t - grouped_alerts[-1] >= 500:
# #             grouped_alerts.append(t)

# #     alert_times_ms = grouped_alerts

# #     filter_parts = []
# #     for i, t in enumerate(alert_times_ms):
# #         filter_parts.append(f"[1]adelay={t}|{t},volume=1[a{i}];")

# #     mix_inputs = ''.join(f"[a{i}]" for i in range(len(alert_times_ms)))
# #     filter_complex = ''.join(filter_parts) + f"{mix_inputs}amix=inputs={len(alert_times_ms)}[mix];[0:a][mix]amix=inputs=2"

# #     command = [
# #         "ffmpeg", "-y",
# #         "-i", video_path,
# #         "-i", audio_path,
# #         "-filter_complex", filter_complex,
# #         "-map", "0:v", "-map", "[mix]",
# #         "-c:v", "copy",
# #         "-shortest",
# #         output_path
# #     ]

# #     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #     if result.returncode != 0:
# #         print("❌ FFmpeg error:\n", result.stderr.decode())
# #         os.rename(video_path, output_path)

# # def main():
# #     model = load_model()
# #     input_video = "input_video.mp4"
# #     temp_video = "temp_annotated.mp4"
# #     output_video = "output_with_alerts.mp4"
# #     alert_audio = "drone_alert.wav"

# #     generate_voice_alert(alert_audio)
# #     alert_times = detect_on_video(model, input_video, temp_video)
# #     add_alerts_to_video(temp_video, alert_times, output_video, alert_audio)
# #     print(f"Готово! Видео с оповещениями сохранено в {output_video}")

# # if __name__ == "__main__":
# #     main()


# import cv2
# import os
# import pyttsx3
# import subprocess

# def load_model():
#     from ultralytics import YOLO
#     model = YOLO("app/models/best.pt")
#     model.fuse()
#     return model

# # def generate_voice_alert(audio_path="drone_alert.wav"):
# #     if not os.path.exists(audio_path):
# #         engine = pyttsx3.init()
# #         engine.save_to_file("Обнаружен дрон", audio_path)
# #         engine.runAndWait()
# def generate_voice_alert(audio_path="drone_alert.wav"):
#     if not os.path.exists(audio_path):
#         engine = pyttsx3.init()
#         # Увеличиваем скорость речи (по умолчанию ~200 слов/мин, можно поднять до 250–300)
#         engine.setProperty('rate', 250)
#         # Максимальная громкость
#         engine.setProperty('volume', 1.0)
#         engine.save_to_file("Обнаружен дрон", audio_path)
#         engine.runAndWait()


# def detect_on_video(model, input_path, output_path):
#     cap = cv2.VideoCapture(input_path)
#     out = None
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     fps = cap.get(cv2.CAP_PROP_FPS)
#     alert_times = set()
#     frame_idx = 0

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         results = model(frame)[0]

#         for box in results.boxes:
#             cls_id = int(box.cls[0])
#             conf = float(box.conf[0])
#             if cls_id == 0 and conf >= 0.83:
#                 x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
#                 cv2.rectangle(frame, (x1, y1), (x2, y2), color=(0, 0, 255), thickness=2)
#                 cv2.putText(frame, "Drone!", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
#                             fontScale=0.8, color=(0, 0, 255), thickness=2)
#                 timestamp_ms = int((frame_idx / fps) * 1000)
#                 alert_times.add(timestamp_ms)

#         if out is None:
#             h, w, _ = frame.shape
#             out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

#         out.write(frame)
#         frame_idx += 1

#     cap.release()
#     if out:
#         out.release()

#     return sorted(alert_times)

# # def add_alerts_to_video(video_path: str, alert_times_ms: list[int], output_path: str, audio_path="drone_alert.wav"):
# #     if not alert_times_ms:
# #         os.rename(video_path, output_path)
# #         return

# #     alert_times_ms = sorted(set(alert_times_ms))
# #     grouped_alerts = [alert_times_ms[0]]
# #     for t in alert_times_ms[1:]:
# #         if t - grouped_alerts[-1] >= 500:
# #             grouped_alerts.append(t)

# #     alert_times_ms = grouped_alerts

# #     filter_parts = []
# #     for i, t in enumerate(alert_times_ms):
# #         filter_parts.append(f"[1]adelay={t}|{t},volume=1[a{i}];")

# #     mix_inputs = ''.join(f"[a{i}]" for i in range(len(alert_times_ms)))
# #     filter_complex = ''.join(filter_parts) + f"{mix_inputs}amix=inputs={len(alert_times_ms)}[mix];[0:a][mix]amix=inputs=2"

# #     command = [
# #         "ffmpeg", "-y",
# #         "-i", video_path,
# #         "-i", audio_path,
# #         "-filter_complex", filter_complex,
# #         "-map", "0:v", "-map", "[mix]",
# #         "-c:v", "copy",
# #         "-shortest",
# #         output_path
# #     ]

# #     result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# #     if result.returncode != 0:
# #         print("❌ FFmpeg error:\n", result.stderr.decode())
# #         os.rename(video_path, output_path)

# # <<<<<<<<<<<<
# def add_alerts_to_video(video_path, alert_times_ms, output_path, audio_path="drone_alert.wav"):
#     # просто подмешаем весь звук разом
#     cmd = [
#         "ffmpeg", "-y",
#         "-i", video_path,
#         "-i", audio_path,
#         "-c:v", "copy", "-c:a", "aac",
#         "-map", "0:v", "-map", "1:a",
#         "-shortest", output_path
#     ]
#     print("Тестовый FFmpeg:", ' '.join(cmd))
#     res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     if res.returncode != 0:
#         print("❌ FFmpeg error:\n", res.stderr.decode())
#         os.rename(video_path, output_path)

# # <<<<<<<<<<<<
# def main():
#     model = load_model()
#     input_video = "input_video.mp4"
#     temp_video = "temp_annotated.mp4"
#     output_video = "output_with_alerts.mp4"
#     alert_audio = "drone_alert.wav"

#     generate_voice_alert(alert_audio)
#     alert_times = detect_on_video(model, input_video, temp_video)
#     add_alerts_to_video(temp_video, alert_times, output_video, alert_audio)
#     print(f"✅ Готово! Видео с оповещениями сохранено в {output_video}")

# if __name__ == "__main__":
#     main()

import cv2
import os
from ultralytics import YOLO

def load_model():
    model = YOLO("app/models/best.pt")
    model.fuse()
    return model

def detect_on_video(model, input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)[0]
        for box in results.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            # если класс 0 (дрон) и уверенность ≥ 0.83
            if cls_id == 0 and conf >= 0.82:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                # рисуем красную рамку
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                # подпись "Drone!" (латиницей)
                cv2.putText(frame, "Drone!", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

        if out is None:
            h, w, _ = frame.shape
            out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

        out.write(frame)

    cap.release()
    if out:
        out.release()
