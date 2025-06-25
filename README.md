# Editor-ISK → v0.1 🐍🔥

Editor Python "hecho en casa" con chispa de IA local (via LM Studio)  
*«Cuando Geany se me resistió, creé mi propia herramienta»*

---

## 🚀 **¡Hola, mundo!**
Este editor es mi experimento para tener un asistente de código **sin depender de la nube**, hecho con:
- ✔️ 10% de frustración con editores existentes  
- ✔️ 90% de ayuda de [DeepSeek](https://deepseek.com)  
- ✔️ 100% de amor al código abierto

---

## 🛠 **Configuración express**
1. **Descarga [LM Studio](https://lmstudio.ai/download)** (¡Soporta Windows/Linux/Mac!)
2. **Consigue un modelo de programación** como:  
   [`deepseek-coder-6.7b-instruct.Q4_K_M`](https://huggingface.co/TheBloke) (ideal para GPUs modestas)
3. **Activa el servidor API** en LM Studio (puerto `8080` o el que prefieras)
4. **¡Ejecuta el editor!** (Usa terminal XFCE por defecto)

---

## 📸 **Vista previa**
<p align="center">
  <img src="https://raw.githubusercontent.com/wsnlndrv/Editor-ISK/main/Capturas/captura_20250625_050624.png" width="700" alt="Captura del Editor-ISK">
</p>

---

## ⚠️ **Advertencias realistas**
- Los modelos locales **no son ChatGPT** (requieren paciencia)
- Si tu GPU es vieja como mi primer PC, usa modelos pequeños
- ¿Bug? ¡Seguro! Pero se arregla con café y tiempo 🐛☕

---

## 💡 **¿Por qué esto?**
```python
if not puedo_instalar_IA_en_Geany():
    print("¡Haz tu propio editor!")
else:
    print("...¿en serio necesitas esto?")

