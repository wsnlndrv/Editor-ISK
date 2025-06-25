# Editor-ISK → v0.1 🐍🔥

Editor Python "hecho en casa" con chispa de IA local (via LM Studio)  
*«Cuando Geany se me resistió, creé mi propia herramienta»*

---

## 🚀 **¡Hola, mundo!**
Este editor es mi experimento para tener un asistente de código **offline**, cocinado con:
- ✔️ 5% de frustración con editores existentes  
- ✔️ 95% de [DeepSeek](https://deepseek.com) (¡gracias por el copiloto!)  
- ✔️ 100% de amor al código abierto *(y un 200% de testeo insuficiente)*

---

## 🛠 **Configuración express** ⚡
1. **Instala [LM Studio](https://lmstudio.ai/download)** (Win/Linux/Mac)
2. **Descarga un modelo GGUF** como:  
   [`deepseek-coder-6.7b-instruct.Q4_K_M`](https://huggingface.co/TheBloke/deepseek-coder-6.7B-instruct-GGUF) (8GB VRAM mínimo)
3. **Prende el servidor API** (puerto `8080` por defecto)
4. **¡Arranca el editor!** (Terminal XFCE incluida de serie)

---

## 📸 **Vista previa**
<p align="center">
  <img src="https://raw.githubusercontent.com/wsnlndrv/Editor-ISK/main/Capturas/captura_20250625_050624.png" width="750" alt="Editor-ISK en acción">
  <br>
  <sup><em>ATENCIÓN: Imagen real no renderizada con Blender</em></sup>
</p>

---

## ⚠️ **Disclaimer honesto**
```diff
- Los modelos locales ≠ ChatGPT-4o (son como un tamagotchi: requieren cuidados)
- GPU vieja? Usa modelos pequeños (este va bien con GTX 1070/Tesla T4)
- ¿Bugs? ¡Feature no documentada! 🐞☕
- ¿Interfaz spartana? Así cargamos más rápido 🚀

def main():
    if not puede_instalar_IA_en_Geany():
        hacer_editor_propio(con="café", bugs="incluidos")
    else:
        print("Aburrido... ¡Hackeemos algo!")
        
    # P.D.: Cuidado con el 'GPTador de la pradera'
    # No sea que te cuelen un 'sudo rm -rf /* --no-preserve-root' 😱

📜 Licencia ⚖️

GPLv3 - Usa, modifica, comparte (pero nada de privatizar)
https://img.shields.io/badge/Licencia-GPLv3-blue?style=flat-square

«Hecho en Linux con amor, bugs incluidos sin cargo extra»
¿Preguntas? ¡Mejor abre un issue que leer la mente no es mi fuerte! 😅
