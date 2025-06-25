# Editor-ISK → v0.1

Editor básico para Python con soporte de asistencia por IA via LM Studio

## 📌 Descripción

Esta herramienta está desarrollada en GNU/Linux para GNU/Linux, aunque adaptarla a otras plataformas no debería ser complejo.

Como alternativa a la integración de IA en editores como Geany (que me resultó complicada), creé este experimento con ayuda de DeepSeek.

## 🛠 Requisitos

1. **LM Studio** instalado:  
   [Descargar LM Studio](https://lmstudio.ai/download)

2. **Modelo de IA** competente en programación, por ejemplo:  
   [`deepseek-coder-6.7b-instruct.Q4_K_M`](https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF/tree/main)  
   (o modelos más avanzados según tu GPU)

## ⚡ Configuración

1. Activa el servidor API en LM Studio (puerto predeterminado: `1234`): http://localhost:1234/v1/chat/completions
*(Verifica el puerto - en mi caso uso `8080`)*

2. Inicia el editor (usa terminal XFCE por defecto, configurable)

3. ¡Listo! Recibirás recomendaciones del modelo basadas en prompts preconfigurados.

## ⚠️ Notas importantes

- Los modelos locales cuantizados tienen limitaciones - no esperes milagros
- La calidad de las respuestas depende del modelo/hardware usado
- Requiere mínimo 8GB RAM para modelos pequeños (16GB+ recomendado)

## 🖼️ Captura

![Captura del Editor](https://github.com/wsnlndrv/Editor-ISK/blob/main/Capturas/captura_20250625_050624.png?raw=true)
