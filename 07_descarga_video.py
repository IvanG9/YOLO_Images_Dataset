import os
import yt_dlp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip


def descargar_video_youtube(url, salida="video_descargado.mp4"):
    """
    Descarga un video de YouTube en formato MP4.
    """
    try:
        ydl_opts = {
            "format": "mp4",
            "outtmpl": salida,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Descargando video desde: {url}")
            ydl.download([url])
        print(f"Video descargado correctamente como: {salida}")
        return salida
    except Exception as e:
        print(f"Ocurrió un error al descargar el video: {e}")
        return None


def recortar_video(ruta_entrada, ruta_salida, inicio=0, duracion=10):
    """
    Recorta un segmento de un video usando FFmpeg a través de moviepy.
    """
    try:
        fin = inicio + duracion
        ffmpeg_extract_subclip(ruta_entrada, inicio, fin, ruta_salida)
        print(f"Video recortado y guardado como: {ruta_salida}")
    except Exception as e:
        print(f"Ocurrió un error al recortar el video: {e}")

# Pedir la URL del video al usuario
url = input("Introduce la URL del video de YouTube: ")
video_completo = "./videos/video_descargado.mp4"
video_recortado = "./videos/video_10_segundos.mp4"

# Descargar el video
ruta_descargada = descargar_video_youtube(url, video_completo)

# Recortar los primeros 10 segundos
if ruta_descargada:
    recortar_video(video_completo, video_recortado, duracion=10)

# Eliminar Video completo
os.remove(video_completo)