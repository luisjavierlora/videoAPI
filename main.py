"""API FOR UPLOAD VIDEO"""
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile, HTTPException

app = FastAPI(docs_url='/')

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Manejador de errores personalizado para manejar excepciones HTTP"""
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": True,"message": exc.detail }
    )

@app.post("/upload_video/")
async def create_upload_file(video: UploadFile = File(...)):
    """Crear video"""

    try:
        # Asegúrate de que el directorio "videos" exista en tu proyecto
        with open(f"db/videos/{video.filename}", "wb") as video_file:
            video_file.write(video.file.read())
        return JSONResponse( status_code=200,content={"error":False,"message":{"filename": video.filename}})
    except Exception as e:
        # Captura cualquier otro error y lanza una excepción HTTP
        raise HTTPException(status_code=500, detail=str(e)) from e
