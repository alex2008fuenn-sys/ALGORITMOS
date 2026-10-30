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
# ==========================================================
#                   SELECCIÓN DE PERFIL / INICIO
# ==========================================================
def mostrar_inicio():
    limpiar_ventana()
    
    marco_padre = tk.Frame(canvas, bg="")
    canvas.create_window(525, 350, window=marco_padre, anchor="center")

    marco = ttk.Frame(marco_padre, padding=40)
    marco.pack()

    ttk.Label(marco, text="⚽ SPORTZONE 🏀", font=("Arial", 28, "bold")).pack(pady=10)
    ttk.Label(marco, text="¡Bienvenido a la Tienda Deportiva!", font=("Arial", 14)).pack(pady=5)
    ttk.Label(marco, text="Seleccione su modo de acceso:", font=("Arial", 11)).pack(pady=15)

    ttk.Button(marco, text="🛍️ INGRESAR COMO CLIENTE", command=mostrar_tienda_cliente, width=32).pack(pady=10)
    ttk.Button(marco, text="🔑 ACCESO ADMINISTRADOR", command=mostrar_login_admin, width=32).pack(pady=10)

# ==========================================================
#            MODO CLIENTE - CATÁLOGO TARJETAS E-COMMERCE
# ==========================================================
def mostrar_tienda_cliente():
    limpiar_ventana()

    top_frame = ttk.Frame(canvas, padding=10)
    canvas.create_window(0, 0, window=top_frame, anchor="nw", width=ventana.winfo_width())

    ttk.Label(top_frame, text="🛒 CATÁLOGO DE PRODUCTOS", font=("Arial", 18, "bold")).pack(side="left", padx=10)
    ttk.Button(top_frame, text="🚪 Cambiar Perfil", command=mostrar_inicio).pack(side="right", padx=5)
    
    cant_carrito = sum(item['cantidad'] for item in carrito_cliente)
    btn_carrito = ttk.Button(top_frame, text=f"🛍️ Ver Carrito ({cant_carrito})", command=vista_carrito)
    btn_carrito.pack(side="right", padx=5)

    global contenedor_dinamico
    contenedor_dinamico = ttk.Frame(canvas, padding=10)
    canvas.create_window(525, 370, window=contenedor_dinamico, anchor="center")

    vista_catalogo_tarjetas()

def vista_catalogo_tarjetas(filtro_deporte=None):
    for widget in contenedor_dinamico.winfo_children():
        widget.destroy()

    # Filtros
    frame_filtros = ttk.Frame(contenedor_dinamico)
    frame_filtros.pack(fill="x", pady=5)

    ttk.Button(frame_filtros, text="Todos", command=lambda: vista_catalogo_tarjetas(None)).pack(side="left", padx=5)
    ttk.Button(frame_filtros, text="⚽ Fútbol", command=lambda: vista_catalogo_tarjetas("Fútbol")).pack(side="left", padx=5)
    ttk.Button(frame_filtros, text="🏀 Básquetbol", command=lambda: vista_catalogo_tarjetas("Básquetbol")).pack(side="left", padx=5)

    lista_mostrar = productos if not filtro_deporte else [p for p in productos if p["deporte"] == filtro_deporte]

    # Canvas interno con Scrollbar
    canvas_scroll = tk.Canvas(contenedor_dinamico, width=820, height=460, bg="#f5f5f5", highlightthickness=0)
    scrollbar = ttk.Scrollbar(contenedor_dinamico, orient="vertical", command=canvas_scroll.yview)
    grid_frame = tk.Frame(canvas_scroll, bg="#f5f5f5")

    grid_frame.bind("<Configure>", lambda e: canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all")))
    canvas_scroll.create_window((0, 0), window=grid_frame, anchor="nw")
    canvas_scroll.configure(yscrollcommand=scrollbar.set)

    canvas_scroll.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Renderizar Tarjetas
    columnas_max = 3
    for index, prod in enumerate(lista_mostrar):
        row = index // columnas_max
        col = index % columnas_max

        card = tk.Frame(grid_frame, bg="#ffffff", bd=1, relief="solid", padx=10, pady=8)
        card.grid(row=row, column=col, padx=10, pady=10)

        # Tag Oferta
        lbl_tag = tk.Label(card, text="OFERTA", bg="#e63946", fg="white", font=("Arial", 8, "bold"))
        lbl_tag.pack(anchor="ne")

        # Contenedor de imagen con tamaño fijo para evitar que se aplaste
        frame_img = tk.Frame(card, width=170, height=110, bg="#eeeeee")
        frame_img.pack_propagate(False)
        frame_img.pack(pady=4)

        lbl_img = tk.Label(frame_img, text="Cargando...", font=("Arial", 9), bg="#eeeeee", fg="#555555")
        lbl_img.pack(fill="both", expand=True)
        
        cargar_imagen_async(prod.get("imagen_url", ""), lbl_img)

        # Nombre
        lbl_nom = tk.Label(card, text=prod["nombre"], font=("Arial", 10, "bold"), bg="#ffffff", wraplength=170)
        lbl_nom.pack()

        # Categoría
        lbl_cat = tk.Label(card, text=f"{prod['deporte']} • {prod['categoria']}", font=("Arial", 8), fg="#666666", bg="#ffffff")
        lbl_cat.pack()

        # Precio
        lbl_precio = tk.Label(card, text=f"Q{prod['precio']:.2f}", font=("Arial", 11, "bold"), fg="#1d3557", bg="#ffffff")
        lbl_precio.pack(pady=2)

        # Stock
        lbl_stock = tk.Label(card, text=f"Stock: {prod['stock']} un.", font=("Arial", 8), fg="#2a9d8f", bg="#ffffff")
        lbl_stock.pack()

        # Botón
        def crear_cmd(p=prod):
            return lambda: agregar_carrito_directo(p)

        btn_add = tk.Button(card, text="🛒 Añadir al carrito", bg="#2a9d8f", fg="white", font=("Arial", 9, "bold"), relief="flat", command=crear_cmd())
        btn_add.pack(pady=6, fill="x")

def agregar_carrito_directo(prod):
    cant_en_carrito = sum(c["cantidad"] for c in carrito_cliente if c["producto"]["codigo"] == prod["codigo"])
    if cant_en_carrito + 1 > prod["stock"]:
        messagebox.showerror("Sin Stock", f"No hay más unidades disponibles de {prod['nombre']}.")
        return

    for c in carrito_cliente:
        if c["producto"]["codigo"] == prod["codigo"]:
            c["cantidad"] += 1
            c["subtotal"] = c["cantidad"] * prod["precio"]
            break
    else:
        carrito_cliente.append({"producto": prod, "cantidad": 1, "subtotal": prod["precio"]})

    messagebox.showinfo("Carrito Actualizado", f"¡{prod['nombre']} añadido al carrito!")
    mostrar_tienda_cliente()

def vista_carrito():
    for widget in contenedor_dinamico.winfo_children():
        widget.destroy()

    ttk.Label(contenedor_dinamico, text="🛍️ TU CARRITO DE COMPRAS", font=("Arial", 16, "bold")).pack(pady=10)

    if not carrito_cliente:
        ttk.Label(contenedor_dinamico, text="El carrito está vacío.").pack(pady=30)
        ttk.Button(contenedor_dinamico, text="⬅️ Volver al Catálogo", command=mostrar_tienda_cliente).pack()
        return

    columnas = ("codigo", "nombre", "precio", "cantidad", "subtotal")
    tabla = ttk.Treeview(contenedor_dinamico, columns=columnas, show="headings", height=6)

    headers = {"codigo": "Código", "nombre": "Producto", "precio": "Precio Unit.", "cantidad": "Cantidad", "subtotal": "Subtotal"}
    for col in columnas:
        tabla.heading(col, text=headers[col])

    for item in carrito_cliente:
        p = item["producto"]
        tabla.insert("", "end", values=(p["codigo"], p["nombre"], f"Q{p['precio']:.2f}", item["cantidad"], f"Q{item['subtotal']:.2f}"))

    tabla.pack(fill="both", expand=True, pady=10)

    total_compra = sum(item["subtotal"] for item in carrito_cliente)
    ttk.Label(contenedor_dinamico, text=f"TOTAL A PAGAR: Q{total_compra:.2f}", font=("Arial", 14, "bold")).pack(pady=5)

    frame_acciones = ttk.Frame(contenedor_dinamico)
    frame_acciones.pack(pady=10)

    def quitar_item():
        selected = tabla.selection()
        if not selected:
            messagebox.showwarning("Atención", "Seleccione un ítem del carrito para quitar.")
            return
        cod = tabla.item(selected[0])["values"][0]
        global carrito_cliente
        carrito_cliente = [item for item in carrito_cliente if item["producto"]["codigo"] != cod]
        mostrar_tienda_cliente()
        vista_carrito()

    def finalizar_compra():
        if messagebox.askyesno("Confirmar Compra", f"¿Desea confirmar su compra por un total de Q{total_compra:.2f}?"):
            for item in carrito_cliente:
                prod = item["producto"]
                cant = item["cantidad"]
                prod["stock"] -= cant
                ventas.append({"codigo": prod["codigo"], "nombre": prod["nombre"], "cantidad": cant, "total": item["subtotal"]})

            carrito_cliente.clear()
            messagebox.showinfo("¡Gracias por su compra!", "Su pedido se ha procesado exitosamente y se ha registrado en el historial de ventas.")
            mostrar_tienda_cliente()

    ttk.Button(frame_acciones, text="❌ Quitar Ítem", command=quitar_item).pack(side="left", padx=5)
    ttk.Button(frame_acciones, text="⬅️ Seguir Comprando", command=mostrar_tienda_cliente).pack(side="left", padx=5)
    ttk.Button(frame_acciones, text="✅ FINALIZAR COMPRA", command=finalizar_compra).pack(side="left", padx=5)
