from symbol import return_stmt

import cv2
import sys

def overlay (path_to_video):
    cap = cv2.VideoCapture(path_to_video)

    if not cap.isOpened():
        print(f"Wrong path to video file: {path_to_video}")
        return

    fps = cap.get(cv2.CAP_PROP_FPS)
    font = cv2.FONT_HERSHEY_DUPLEX
    text = (f"File: {path_to_video.split('/')[-1]} FPS: {fps}")
    position = (10, 30)
    font_scale = 1
    font_color = (0, 0, 255)
    font_thickness = 1

    while True:
        ret, frame = cap.read()

        if not ret:
            print("end of file")
            break

        cv2.putText(frame, text, position, font, font_scale, font_color, font_thickness)

        cv2.imshow('Video', frame)

        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('e'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Wrong number of arguments")
        exit()
    path_to_video = sys.argv[1]
    overlay(path_to_video)