import cv2
import numpy as np

def run_str():
    text = "123456789012345678901234567890"
    
    w, h = 100, 100
    fr = 24
    out = cv2.VideoWriter("runstr.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fr, (w, h))

    frame = np.zeros((h, w, 3), dtype = np.uint8)

    y = h // 2

    x = w // 2

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_thickness = 2
    font_color = (255, 255, 255)

    for t in range(fr*3):
        
        frame.fill(0)
        cv2.putText(frame, text, (x,y), font, font_scale, font_color, font_thickness)
        x -= len(text)*8 // fr
    

        out.write(frame)
    out.release()
run_str()
