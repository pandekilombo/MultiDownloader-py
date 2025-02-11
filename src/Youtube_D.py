from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
import subprocess

# Descargar el video con la resolución más alta y combinarlo con el audio
def Youtube_Video_Highest(Link):
    try:
        yt = YouTube(Link, on_progress_callback=on_progress)
        print(f"Video Title: {yt.title}")

        # Obtener el stream de video con la resolución más alta disponible
        video_stream = yt.streams.filter(progressive=False, file_extension='mp4').get_highest_resolution()
        
        # Obtener el stream de solo audio
        audio_stream = yt.streams.filter(only_audio=True).first()

        if video_stream is None or audio_stream is None:
            print("No se encontró un stream adecuado para video y/o audio.")
            return None

        print(f"Descargando video y audio...")
        
        # Descargar el video y el audio
        video_path = video_stream.download(output_path="descargas", filename="video.mp4")
        audio_path = audio_stream.download(output_path="descargas", filename="audio.mp4")

        # Combinar el video y el audio usando ffmpeg
        output_file = f"descargas/{yt.title}_1080p.mp4"
        
        # Comando para combinar video y audio
        subprocess.run(['ffmpeg', '-i', video_path, '-i', audio_path, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', output_file])

        # Eliminar los archivos temporales (video y audio por separado)
        os.remove(video_path)
        os.remove(audio_path)

        print(f"Descarga y combinación completadas: {output_file}")
        return output_file

    except Exception as e:
        print(f"Error: {e}")
        return None

# Descargar el video con la resolución más baja (240p) y combinarlo con el audio
def Youtube_Video_Lowest(Link):
    try:
        yt = YouTube(Link, on_progress_callback=on_progress)
        print(f"Video Title: {yt.title}")

        # Obtener el stream con la resolución más baja (240p)
        video_stream = yt.streams.filter(resolution="240p", progressive=False).first()
        
        # Obtener el stream de solo audio
        audio_stream = yt.streams.filter(only_audio=True).first()

        if video_stream is None or audio_stream is None:
            print("No se encontró un stream adecuado para video y/o audio.")
            return None

        print(f"Descargando video y audio...")
        
        # Descargar el video y el audio
        video_path = video_stream.download(output_path="descargas", filename="video_240p.mp4")
        audio_path = audio_stream.download(output_path="descargas", filename="audio.mp4")

        # Combinar el video y el audio usando ffmpeg
        output_file = f"descargas/{yt.title}_240p.mp4"
        
        # Comando para combinar video y audio
        subprocess.run(['ffmpeg', '-i', video_path, '-i', audio_path, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', output_file])

        # Eliminar los archivos temporales (video y audio por separado)
        os.remove(video_path)
        os.remove(audio_path)

        print(f"Descarga y combinación completadas: {output_file}")
        return output_file

    except Exception as e:
        print(f"Error: {e}")
        return None
# Descargar solo el audio del video
def Youtube_Audio(Link):
    try:
        yt = YouTube(Link, on_progress_callback=on_progress)
        print(f"Video Title: {yt.title}")

        # Obtener el stream de solo audio
        ys = yt.streams.get_audio_only()
        
        # Descargar el audio
        ys.download()
        print(f"Descarga completa: {yt.title}")
        return yt.title
    except Exception as e:
        print(f"Error: {e}")
        return None

# Descargar el video en una resolución específica y combinarlo con el audio
def Youtube_Video_Resolution(Link, Res):
    try:
        yt = YouTube(Link, on_progress_callback=on_progress)
        print(f"Video Title: {yt.title}")

        # Filtrar los streams por resolución específica
        video_stream = yt.streams.filter(resolution=Res, progressive=False).first()

        # Obtener el stream de solo audio
        audio_stream = yt.streams.filter(only_audio=True).first()

        if video_stream is None or audio_stream is None:
            print(f"No se encontró un stream adecuado para la resolución {Res} y/o audio.")
            return None

        print(f"Descargando video en {Res} y audio...")
        
        # Descargar el video y el audio
        video_path = video_stream.download(output_path="descargas", filename=f"video_{Res}.mp4")
        audio_path = audio_stream.download(output_path="descargas", filename="audio.mp4")

        # Combinar el video y el audio usando ffmpeg
        output_file = f"descargas/{yt.title}_{Res}.mp4"
        
        # Comando para combinar video y audio
        subprocess.run(['ffmpeg', '-i', video_path, '-i', audio_path, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', output_file])

        # Eliminar los archivos temporales (video y audio por separado)
        os.remove(video_path)
        os.remove(audio_path)

        print(f"Descarga y combinación completadas: {output_file}")
        return output_file

    except Exception as e:
        print(f"Error: {e}")
        return None

# Prueba de las funciones
# Cambia estos enlaces de ejemplo por los tuyos
#Youtube_Video_Highest("https://youtu.be/oQU27tfUl4o?si=64i3EobehUfHGVYJ")
#Youtube_Video_Lowest("https://youtu.be/oQU27tfUl4o?si=64i3EobehUfHGVYJ")
#Youtube_Video_Resolution("https://youtu.be/oQU27tfUl4o?si=64i3EobehUfHGVYJ", "720p")
