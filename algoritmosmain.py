import os
import io
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk

# ==========================================================
#                   DATOS DEL SISTEMA
# ==========================================================
USUARIO_ADMIN = "admin"
PASS_ADMIN = "1234"
URL_IMAGEN_FONDO = "https://www.shutterstock.com/image-illustration/soccer-ball-basket-3d-illustration-260nw-1898407648.jpg"

productos = [
    {
        "codigo": "F001",
        "nombre": "Balón Adidas Pro",
        "deporte": "Fútbol",
        "categoria": "Balones",
        "precio": 350.00,
        "stock": 10,
        "imagen_url": "https://images.unsplash.com/photo-1614632537190-23e4146777db?w=300"
    },
    {
        "codigo": "F002",
        "nombre": "Guantes de Portero",
        "deporte": "Fútbol",
        "categoria": "Porteros",
        "precio": 275.00,
        "stock": 6,
        "imagen_url": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=300"
    },
    {
        "codigo": "F003",
        "nombre": "Tacos Nike Phantom",
        "deporte": "Fútbol",
        "categoria": "Calzado",
        "precio": 850.00,
        "stock": 5,
        "imagen_url": "https://images.unsplash.com/photo-1511886929837-354d827aae26?w=300"
    },
    {
        "codigo": "B001",
        "nombre": "Balón Spalding NBA",
        "deporte": "Básquetbol",
        "categoria": "Balones",
        "precio": 400.00,
        "stock": 8,
        "imagen_url": "https://images.unsplash.com/photo-1519861531473-9200262188bf?w=300"
    },
    {
        "codigo": "B002",
        "nombre": "Camiseta Deportiva",
        "deporte": "Básquetbol",
        "categoria": "Ropa",
        "precio": 300.00,
        "stock": 12,
        "imagen_url": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=300"
    },
    {
        "codigo": "B003",
        "nombre": "Tenis Básquetbol Nike",
        "deporte": "Básquetbol",
        "categoria": "Calzado",
        "precio": 750.00,
        "stock": 7,
        "imagen_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=300"
    }
]

ventas = []
carrito_cliente = []
cache_imagenes = {}

# ==========================================================
#                   CONFIGURACIÓN VENTANA
# ==========================================================
ventana = tk.Tk()
ventana.title("SPORTZONE - Tienda Deportiva")
ventana.geometry("1050x700")
ventana.minsize(950, 650)

img_original = None
imagen_tk = None

def cargar_imagen_fondo():
    global img_original
    try:
        if not os.path.exists("fondo.jpg"):
            headers = {'User-Agent': 'Mozilla/5.0'}
            respuesta = requests.get(URL_IMAGEN_FONDO, headers=headers, timeout=5)
            if respuesta.status_code == 200:
                with open("fondo.jpg", "wb") as f:
                    f.write(respuesta.content)
        img_original = Image.open("fondo.jpg")
    except Exception as e:
        print(f"No se pudo cargar la imagen de fondo: {e}")

cargar_imagen_fondo()

canvas = tk.Canvas(ventana, highlightthickness=0)
canvas.pack(fill="both", expand=True)

def actualizar_fondo(event=None):
    global imagen_tk
    if img_original:
        w, h = ventana.winfo_width(), ventana.winfo_height()
        if w > 10 and h > 10:
            img_res = img_original.resize((w, h), Image.Resampling.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(img_res)
            canvas.delete("fondo")
            canvas.create_image(0, 0, image=imagen_tk, anchor="nw", tags="fondo")
            canvas.tag_lower("fondo")

ventana.bind("<Configure>", actualizar_fondo)

def cargar_imagen_async(url, label_destino):
    if not url:
        return
    if url in cache_imagenes:
        label_destino.config(image=cache_imagenes[url], text="")
        label_destino.image = cache_imagenes[url]
        return

    def tarea_descarga():
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            resp = requests.get(url, headers=headers, timeout=3)
            if resp.status_code == 200:
                img_data = Image.open(io.BytesIO(resp.content))
                img_data = img_data.resize((170, 110), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img_data)
                cache_imagenes[url] = img_tk
                
                ventana.after(0, lambda: label_destino.config(image=img_tk, text="") if label_destino.winfo_exists() else None)
                if hasattr(label_destino, "image"):
                    label_destino.image = img_tk
        except Exception:
            ventana.after(0, lambda: label_destino.config(text="📦 Imagen no disponible") if label_destino.winfo_exists() else None)

    threading.Thread(target=tarea_descarga, daemon=True).start()

def limpiar_ventana():
    for widget in canvas.winfo_children():
        widget.destroy()

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#ffffff")
style.configure("TLabel", background="#ffffff", foreground="#000000")import os
import io
import threading
import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk

# ==========================================================
#                   DATOS DEL SISTEMA
# ==========================================================
USUARIO_ADMIN = "admin"
PASS_ADMIN = "1234"
URL_IMAGEN_FONDO = "https://www.shutterstock.com/image-illustration/soccer-ball-basket-3d-illustration-260nw-1898407648.jpg"

productos = [
    {
        "codigo": "F001",
        "nombre": "Balón Adidas Pro",
        "deporte": "Fútbol",
        "categoria": "Balones",
        "precio": 350.00,
        "stock": 10,
        "imagen_url": "https://images.unsplash.com/photo-1614632537190-23e4146777db?w=300"
    },
    {
        "codigo": "F002",
        "nombre": "Guantes de Portero",
        "deporte": "Fútbol",
        "categoria": "Porteros",
        "precio": 275.00,
        "stock": 6,
        "imagen_url": "https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=300"
    },
    {
        "codigo": "F003",
        "nombre": "Tacos Nike Phantom",
        "deporte": "Fútbol",
        "categoria": "Calzado",
        "precio": 850.00,
        "stock": 5,
        "imagen_url": "https://images.unsplash.com/photo-1511886929837-354d827aae26?w=300"
    },
    {
        "codigo": "B001",
        "nombre": "Balón Spalding NBA",
        "deporte": "Básquetbol",
        "categoria": "Balones",
        "precio": 400.00,
        "stock": 8,
        "imagen_url": "https://images.unsplash.com/photo-1519861531473-9200262188bf?w=300"
    },
    {
        "codigo": "B002",
        "nombre": "Camiseta Deportiva",
        "deporte": "Básquetbol",
        "categoria": "Ropa",
        "precio": 300.00,
        "stock": 12,
        "imagen_url": "https://images.unsplash.com/photo-1577219491135-ce391730fb2c?w=300"
    },
    {
        "codigo": "B003",
        "nombre": "Tenis Básquetbol Nike",
        "deporte": "Básquetbol",
        "categoria": "Calzado",
        "precio": 750.00,
        "stock": 7,
        "imagen_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=300"
    }
]

ventas = []
carrito_cliente = []
cache_imagenes = {}

# ==========================================================
#                   CONFIGURACIÓN VENTANA
# ==========================================================
ventana = tk.Tk()
ventana.title("SPORTZONE - Tienda Deportiva")
ventana.geometry("1050x700")
ventana.minsize(950, 650)

img_original = None
imagen_tk = None

def cargar_imagen_fondo():
    global img_original
    try:
        if not os.path.exists("fondo.jpg"):
            headers = {'User-Agent': 'Mozilla/5.0'}
            respuesta = requests.get(URL_IMAGEN_FONDO, headers=headers, timeout=5)
            if respuesta.status_code == 200:
                with open("fondo.jpg", "wb") as f:
                    f.write(respuesta.content)
        img_original = Image.open("fondo.jpg")
    except Exception as e:
        print(f"No se pudo cargar la imagen de fondo: {e}")

cargar_imagen_fondo()

canvas = tk.Canvas(ventana, highlightthickness=0)
canvas.pack(fill="both", expand=True)

def actualizar_fondo(event=None):
    global imagen_tk
    if img_original:
        w, h = ventana.winfo_width(), ventana.winfo_height()
        if w > 10 and h > 10:
            img_res = img_original.resize((w, h), Image.Resampling.LANCZOS)
            imagen_tk = ImageTk.PhotoImage(img_res)
            canvas.delete("fondo")
            canvas.create_image(0, 0, image=imagen_tk, anchor="nw", tags="fondo")
            canvas.tag_lower("fondo")

ventana.bind("<Configure>", actualizar_fondo)

def cargar_imagen_async(url, label_destino):
    if not url:
        return
    if url in cache_imagenes:
        label_destino.config(image=cache_imagenes[url], text="")
        label_destino.image = cache_imagenes[url]
        return

    def tarea_descarga():
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            resp = requests.get(url, headers=headers, timeout=3)
            if resp.status_code == 200:
                img_data = Image.open(io.BytesIO(resp.content))
                img_data = img_data.resize((170, 110), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img_data)
                cache_imagenes[url] = img_tk
                
                ventana.after(0, lambda: label_destino.config(image=img_tk, text="") if label_destino.winfo_exists() else None)
                if hasattr(label_destino, "image"):
                    label_destino.image = img_tk
        except Exception:
            ventana.after(0, lambda: label_destino.config(text="📦 Imagen no disponible") if label_destino.winfo_exists() else None)

    threading.Thread(target=tarea_descarga, daemon=True).start()

def limpiar_ventana():
    for widget in canvas.winfo_children():
        widget.destroy()

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#ffffff")
style.configure("TLabel", background="#ffffff", foreground="#000000")
