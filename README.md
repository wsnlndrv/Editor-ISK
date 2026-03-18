# Editor-ISK → v0.1 🐍🔥

Editor Python "hecho en casa" con chispa de IA 
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
   Con una RTX Bi-Turbo Intercoller 7090 del año 2029 Vas sobrado.
4. **Prende el servidor API** (puerto `8080` por defecto)
5. **¡Arranca el editor!** (Terminal XFCE incluida de serie... En el S.O.)

📜 Licencia ⚖️
[![Licencia GPLv3](https://img.shields.io/badge/⚖️_Licencia-GPLv3-important)](LICENSE)
[![Made with](https://img.shields.io/badge/Hecho_con-5%25_paciencia-ff69b4)](https://github.com/wsnlndrv)
[![GPU](https://img.shields.io/badge/GPU-8GB%2B-orange)](https://lmstudio.ai)
---

## 📸 **Vista previa**
<p align="center">
  <img src="https://raw.githubusercontent.com/wsnlndrv/Editor-ISK/main/Capturas/captura_20250625_050624.png" width="750" alt="Editor-ISK en acción">
  <br>
  <sup><em>ATENCIÓN: Imagen real no renderizada con Blender</em></sup>
</p>

---

## 🧪 **Especificaciones Técnicas (más o menos)**
```python
# Editor-ISK Core: ¡Código con personalidad!
def main():
    # ----------------------------------------
    # Fase 1: Crisis existencial del developer
    # ----------------------------------------
    if not puede_instalar_IA_en_Geany():
        proyecto = hacer_editor_propio(
            cafeína=0xCAFE,      # Hexadecimal para sentirnos hackers
            bugs="features",     # eufemismo profesional
            deuda_técnica=9999   # problema del "yo futuro"
        )
    else:
        print("Aburrido... ¡Hackeemos systemd entonces!")
        proyecto = "linux-6.10-rc3"  # por si las moscas

    # ----------------------------------------
    # Fase 2: Loop de desarrollo (aka. purgatorio)
    # ----------------------------------------
    while not proyecto.estable:
        cafeína *= 1.61803398875  # proporción áurea del café
        
        if bug := next((b for b in proyecto.bugs if b.crítico), None):
            maldecir(bug, volumen=11, idioma="español medieval")
            proyecto.parches.append(
                Parche(
                    título="Fix mágico", 
                    descripción="Ya no peta... mucho",
                    urgencia="WTF"
                )
            )
        else:
            commit(
                mensaje="¡Funciona! (en mi Docker)",
                fuerza=True,       # --force es como el ajo: cuanto más mejor
                hora="04:20 AM",
                emoción="éxtasis programático"
            )
        
        # ----------------------------------------
        # Chequeo de seguridad anti-GPTs salvajes
        # ----------------------------------------
        if "GPT4" in proyecto.colaboradores:
            print("¡ALERTA! Comando sospechoso detectado:")
            print("$ sudo rm -rf /* --no-preserve-root 2>/dev/null")
            proyecto.sandbox_mode = True  # por si acaso

    # ----------------------------------------
    # Fase 3: Lanzamiento (arrepentimiento público)
    # ----------------------------------------
    return Proyecto(
        nombre="Editor-ISK", 
        versión="v0.1.1-alpha-nightly-hotfix",
        horas_sueño=42,    # en hexadecimal sería 0x2A
        estado="¿Arranca? → Sí | ¿Funciona? → It's complicated"
    )

# Post-data filosófica:
# "El código perfecto no existe... pero el que pasa los tests sirve"
# (A veces ni eso)
```
