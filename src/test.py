from pytubefix import YouTube

def Youtube_Video_Resolution(Link):
    try:
        yt = YouTube(Link)
        print(f"Video Title: {yt.title}")
        
        # Mostrar todas las resoluciones disponibles
        print("Resoluciones disponibles:")
        for stream in yt.streams.filter(progressive=True):  # `progressive=True` incluye video y audio juntos
            print(stream.resolution)

        # Aquí intentas obtener el stream con la resolución más baja y más alta
        highest_res = yt.streams.get_highest_resolution()
        lowest_res = yt.streams.get_lowest_resolution()

        print(f"Resolución más alta: {highest_res.resolution}")
        print(f"Resolución más baja: {lowest_res.resolution}")

        # Intentar la descarga con la más baja o alta
        lowest_res.download()
        print(f"Descarga completa: {yt.title}")

    except Exception as e:
        print(f"Error: {e}")

# Prueba con un enlace de video
Youtube_Video_Resolution("https://www.youtube.com/watch?v=w5JsyFN0qjU")
