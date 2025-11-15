from PIL import Image
import numpy as np, os
try:
    from ultralytics import YOLO
    YOLO_AVAILABLE = True
    model = YOLO(os.environ.get('YOLO_MODEL','yolov8n.pt'))
except Exception:
    YOLO_AVAILABLE = False
    model = None
try:
    import pytesseract
    OCR_AVAILABLE = True
except Exception:
    OCR_AVAILABLE = False
try:
    import pyttsx3
    TTS_AVAILABLE = True
    engine = pyttsx3.init()
except Exception:
    TTS_AVAILABLE = False
    engine = None

def run_yolo_detection(pil_img):
    if YOLO_AVAILABLE and model is not None:
        results = model(pil_img)
        labels = []
        for r in results:
            names = getattr(r, 'names', None) or {}
            boxes = getattr(r, 'boxes', None)
            if boxes is not None and hasattr(boxes, 'data'):
                for box in boxes.data.tolist():
                    try:
                        cls = int(box[5])
                        labels.append(names.get(cls, str(cls)))
                    except Exception:
                        pass
        return list(set(labels))
    else:
        # fallback heuristic
        arr = np.array(pil_img.convert('L').resize((320,240)))
        avg = arr.mean()
        labels = []
        if avg < 60:
            labels.append('person?')
        if avg > 200:
            labels.append('table?')
        return labels

def run_ocr(pil_img):
    if OCR_AVAILABLE:
        text = pytesseract.image_to_string(pil_img)
    else:
        text = '[OCR not available on server]'
    layout = []
    lower = text.lower()
    if 'insert card' in lower:
        layout.append('ATM-like interface detected.')
    if 'start' in lower:
        layout.append('Start button detected.')
    if not layout:
        layout.append('No structured interface detected.')
    return text, layout

def heuristic_hazard_detection(labels):
    hazards = []
    for l in labels:
        ll = l.lower()
        if 'stair' in ll:
            hazards.append('stairs')
        if 'person' in ll:
            hazards.append('moving person')
        if 'bag' in ll or 'box' in ll:
            hazards.append('obstacle')
    return list(set(hazards))

def text_to_speech(text):
    if TTS_AVAILABLE and engine is not None:
        engine.say(text); engine.runAndWait(); return True
    return False
