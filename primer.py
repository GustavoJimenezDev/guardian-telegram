import time
import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ==========================================
# CONFIGURACIÓN (Usa variables de entorno o edita localmente)
# ==========================================
CARPETA_A_VIGILAR = os.path.expanduser("~/carpeta protegida")

# ⚠️ NUNCA PUBLICAR EL TOKEN
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "COLOCA TU TOKEN PRIVADO AQUI")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "COLOCA TU ID PERSONAL")

ARCHIVO_LOG = "registro_actividad.log"

# ==========================================
# FUNCIONES AUXILIARES
# ==========================================
def enviar_alerta_telegram(mensaje):
    """Envía alertas a Telegram en formato HTML."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
        "parse_mode": "HTML"
    }
    try:
        respuesta = requests.post(url, data=payload, timeout=5)
        if respuesta.status_code != 200:
            print(f"[-] Error Telegram ({respuesta.status_code}): {respuesta.text}")
    except Exception as e:
        print(f"[-] Error de conexión: {e}")

def registrar_evento(descripcion):
    """Guarda los logs locales."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    linea = f"[{timestamp}] {descripcion}\n"
    print(linea.strip())
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as f:
        f.write(linea)

# ==========================================
# MANEJADOR DE EVENTOS (Archivos Y Carpetas)
# ==========================================
class GuardiánCarpeta(FileSystemEventHandler):

    def on_created(self, event):
        tipo = "📁 Carpeta" if event.is_directory else "📄 Archivo"
        msg = f"✨ <b>{tipo} creado:</b>\n<code>{event.src_path}</code>"
        registrar_evento(f"CREADO ({tipo}): {event.src_path}")
        enviar_alerta_telegram(msg)

    def on_modified(self, event):
        tipo = "📁 Carpeta" if event.is_directory else "📄 Archivo"
        msg = f"✏️ <b>{tipo} modificado:</b>\n<code>{event.src_path}</code>"
        registrar_evento(f"MODIFICADO ({tipo}): {event.src_path}")
        enviar_alerta_telegram(msg)

    def on_deleted(self, event):
        tipo = "📁 Carpeta" if event.is_directory else "📄 Archivo"
        msg = f"🗑️ <b>{tipo} eliminado:</b>\n<code>{event.src_path}</code>"
        registrar_evento(f"ELIMINADO ({tipo}): {event.src_path}")
        enviar_alerta_telegram(msg)

# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================
if __name__ == "__main__":
    if not os.path.exists(CARPETA_A_VIGILAR):
        os.makedirs(CARPETA_A_VIGILAR)
        print(f"[+] Se creó la carpeta: {CARPETA_A_VIGILAR}")

    event_handler = GuardiánCarpeta()
    observer = Observer()
    
    # recursive=True permite vigilar carpetas internas y subdirectorios
    observer.schedule(event_handler, path=CARPETA_A_VIGILAR, recursive=True)
    
    observer.start()
    print("=" * 50)
    print(f"🛡️ Guardián activo vigilando: {CARPETA_A_VIGILAR}")
    print("=" * 50)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\n[!] Guardián detenido.")
    
    observer.join()
