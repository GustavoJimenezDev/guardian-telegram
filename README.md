# 🛡️ Folder Guardian & Telegram Bot

A Python-based file system monitoring tool built with `watchdog` and Telegram Bot API. It watches a target directory in real-time for any file or folder events (creation, modification, deletion) and sends instant alerts straight to your Telegram account.

---

## 🇬🇧 ENGLISH

### 🎯 Project Purpose
The goal of this project is to provide a lightweight security and activity monitor for specific directories. It tracks changes in the file system and immediately notifies the user via Telegram, keeping a detailed local history log of all activity.

### 🚀 Features
- **Real-time Monitoring:** Detects creation, modification, and deletion of files and folders.
- **Recursive Tracking:** Monitors subdirectories and nested files automatically.
- **Telegram Integration:** Instant alerts sent to your phone.
- **Local Logging:** Saves timestamped events in a `registro_actividad.log` file.

### 🛠️ Step-by-Step Instructions

#### Step 1: Requirements & Installation
Make sure you have Python 3 installed. Install the necessary packages:
```bash
pip install watchdog requests
Step 2: Set Environment Variables
Set your Telegram Bot Token (from @BotFather) and Chat ID (from @userinfobot) in your system environment:

Bash
export TELEGRAM_TOKEN="your_bot_token_here"
export TELEGRAM_CHAT_ID="your_chat_id_here"
Step 3: Run the Script
Execute the main script from your terminal:

Bash
python3 carpeta.py
🇲🇽 ESPAÑOL
🎯 Propósito del Proyecto
El objetivo de este proyecto es proporcionar un monitor de seguridad y actividad ligero para carpetas específicas. Rastrea cambios en el sistema de archivos y notifica inmediatamente al usuario a través de Telegram, manteniendo un historial local detallado de toda la actividad.

🚀 Características
Monitoreo en Tiempo Real: Detecta creación, modificación y eliminación de archivos y carpetas.

Rastreo Recursivo: Vigila subcarpetas y archivos internos automáticamente.

Integración con Telegram: Alertas instantáneas enviadas a tu teléfono.

Registro Local: Guarda los eventos con fecha y hora en un archivo registro_actividad.log.

🛠️ Instrucciones Paso a Paso
Paso 1: Requisitos e Instalación
Asegúrate de tener Python 3 instalado. Instala las librerías necesarias:

Bash
---------------------------------------------------------------------------
pip install watchdog requests
----------------------------------------------------------------------------
Paso 2: Configurar Variables de Entorno
Configura el Token de tu Bot (obtenido con @BotFather) y tu Chat ID (obtenido con @userinfobot) en tu sistema:

Bash
export TELEGRAM_TOKEN="tu_token_aqui"
export TELEGRAM_CHAT_ID="tu_chat_id_aqui"
Paso 3: Ejecutar el Script
Ejecuta el programa principal desde tu terminal:

Bash
python3 carpeta.py

---

¡Así queda súper ordenado y completo para tu repositorio!