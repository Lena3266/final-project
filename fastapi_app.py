from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import io
from PIL import Image
from backend.modules import backend_utils as bu
from backend.modules import db as dbmod

app = FastAPI(title='NAVI.AI backend', version='0.2')

@app.on_event('startup')
def startup():
    dbmod.init_db()

@app.get('/health')
def health():
    return {'status':'ok'}

@app.post('/detect')
async def detect(image: UploadFile = File(...)):
    contents = await image.read()
    img = Image.open(io.BytesIO(contents)).convert('RGB')
    labels = bu.run_yolo_detection(img)
    hazards = bu.heuristic_hazard_detection(labels)
    dbmod.log_event('detect', ','.join(labels))
    return JSONResponse({'labels': labels, 'hazards': hazards})

@app.post('/ocr')
async def ocr(image: UploadFile = File(...)):
    contents = await image.read()
    img = Image.open(io.BytesIO(contents)).convert('RGB')
    text, layout = bu.run_ocr(img)
    dbmod.log_event('ocr', text[:200])
    return JSONResponse({'text': text, 'layout': layout})

@app.post('/tts')
async def tts(body: dict):
    text = body.get('text','')
    ok = bu.text_to_speech(text)
    dbmod.log_event('tts', text[:200])
    return JSONResponse({'ok': ok})
