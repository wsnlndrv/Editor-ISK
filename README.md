# Editor-ISK

## Editor básico para Python con soporte para la asistencia de IA via LM Studio

Esta herramienta básica esta hecha en GNU/Linux, para GNU/Linux.  

Adaptarla para otras plataformas no debería ser complejo.

Como soy torpe aprendiendo a usar las herramientas de otros y no he podido añadirle un asistente IA a Geany, hice este esperimento con la ayuda de DeepSeek.

Para que funcione como debe, tendras que tener instalado LM Studio -> https://lmstudio.ai/download  

Luego tendras que descargar un modelo que tenga alguna competencia en programación, por ejemplo ->  
deepseek-coder-6.7b-instruct.Q4_K_M o alguno mejor si tu GPU lo soporta. ->> https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF/tree/main  

Hay que activar el servidor API de LM Studio que por defecto trabaja en (http://localhost:1234/v1/chat/completions) -> Comprueba el puerto, en mi caso 8080.

Luego ya podras iniciar el editor (usa la terminal de XFCE por defecto, cambiala por otra si es el caso) 
y ya podrías recibir recomendaciones del modelo a partir de un Prompt preconfigurado.  

No esperes grandes hazañas de un modelo local cuantizado.  

![Captura del Editor](https://github.com/wsnlndrv/Editor-ISK/blob/main/Capturas/captura_20250625_044446.png?raw=true)
