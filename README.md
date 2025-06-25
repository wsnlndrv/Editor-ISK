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
4. **¡Arranca el editor!** (Terminal XFCE incluida de serie... En el S.O.)

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
```diff
! ADVERTENCIA EPIC:
! Los modelos locales ≠ DeepSeek V3 (son como tamagotchis: si no los cuidas, se mueren)
! GPU antigua? Modelos pequeños (8GB VRAM mínimo)
! ¿Interfaz espartana? ¡Feature de optimización! 🚀


def main():
    # Fase 1: Crisis existencial
    if not puede_instalar_IA_en_Geany():
        proyecto = hacer_editor_propio(
            cafeína=0xCAFE,          # Hexadecimal para parecer hacker
            bugs="features",         # Marketing 101
            deuda_técnica=9999       # Future Me's problem
        )
    else:
        print("Aburrido... ¡Hackeemos el kernel entonces!")
        proyecto = "linux-next"      # Por si acaso

    # Fase 2: Desarrollo real (aka. "el infierno")
    while not proyecto.estable:
        cafeína *= 1.61803398875     # Proporción áurea del café
        
        if bug := next((b for b in proyecto.bugs if b.crítico), None):
            maldecir(bug, idioma="español antiguo")  # Más efectivo
            proyecto.parches.append(
                Parche(título="Fix mágico", 
                       descripción="Ya no crashea... mucho")
            )
        else:
            commit(
                mensaje="¡Funciona! (en mi máquina)",
                fuerza=True,          # --force es mi amor verdadero
                hora="03:42 AM",
                emoción="euforia irracional"
            )
        
        # Post-mortem debugging
        if "GPT de la pradera" in proyecto.colaboradores:
            print("¡ALERTA! Posible rm -rf /* camuflado")
            proyecto.sandbox_mode = True  # Por si las moscas

    # Fase 3: Lanzamiento (aka. "arrepentimiento público")    
    return Proyecto(
        nombre="Editor-ISK", 
        versión="0.1.1-alpha-preview-nightly",
        soporte_vital=42  # Horas de sueño perdidas
    )


# Corolario Zen:
# "El código perfecto no existe... pero el que compila sirve"
