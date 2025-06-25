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

<div style="background: #1e1e1e; color: #d4d4d4; font-family: 'Courier New', monospace; padding: 15px; border-radius: 8px; border: 1px solid #444; line-height: 1.5;">
<span style="color: #569cd6;">def</span> <span style="color: #dcdcaa;">main</span>():<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># Fase 1: Crisis existencial</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #569cd6;">if not</span> <span style="color: #dcdcaa;">puede_instalar_IA_en_Geany</span>():<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">proyecto</span> = <span style="color: #dcdcaa;">hacer_editor_propio</span>(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">cafeína</span>=<span style="color: #b5cea8;">0xCAFE</span>,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># Hexadecimal para parecer hacker</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">bugs</span>=<span style="color: #ce9178;">"features"</span>,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># Marketing 101</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">deuda_técnica</span>=<span style="color: #b5cea8;">9999</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># Future Me's problem</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #569cd6;">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #dcdcaa;">print</span>(<span style="color: #ce9178;">"Aburrido... ¡Hackeemos el kernel entonces!"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">proyecto</span> = <span style="color: #ce9178;">"linux-next"</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># Por si acaso</span><br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># Fase 2: Desarrollo real (aka. 'el infierno')</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #569cd6;">while not</span> <span style="color: #9cdcfe;">proyecto</span>.<span style="color: #9cdcfe;">estable</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">cafeína</span> *= <span style="color: #b5cea8;">1.61803398875</span>&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># Proporción áurea del café</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #569cd6;">if</span> <span style="color: #9cdcfe;">bug</span> := <span style="color: #dcdcaa;">next</span>((<span style="color: #9cdcfe;">b</span> <span style="color: #569cd6;">for</span> <span style="color: #9cdcfe;">b</span> <span style="color: #569cd6;">in</span> <span style="color: #9cdcfe;">proyecto</span>.<span style="color: #9cdcfe;">bugs</span> <span style="color: #569cd6;">if</span> <span style="color: #9cdcfe;">b</span>.<span style="color: #9cdcfe;">crítico</span>), <span style="color: #569cd6;">None</span>):<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #dcdcaa;">maldecir</span>(<span style="color: #9cdcfe;">bug</span>, <span style="color: #9cdcfe;">idioma</span>=<span style="color: #ce9178;">"español antiguo"</span>)&nbsp;&nbsp;<span style="color: #6a9955;"># Más efectivo</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">proyecto</span>.<span style="color: #9cdcfe;">parches</span>.<span style="color: #dcdcaa;">append</span>(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #dcdcaa;">Parche</span>(<span style="color: #9cdcfe;">título</span>=<span style="color: #ce9178;">"Fix mágico"</span>, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">descripción</span>=<span style="color: #ce9178;">"Ya no crashea... mucho"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #569cd6;">else</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #dcdcaa;">commit</span>(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">mensaje</span>=<span style="color: #ce9178;">"¡Funciona! (en mi máquina)"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">fuerza</span>=<span style="color: #569cd6;">True</span>,&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># --force es mi amor verdadero</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">hora</span>=<span style="color: #ce9178;">"03:42 AM"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">emoción</span>=<span style="color: #ce9178;">"euforia irracional"</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;)<br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># Post-mortem debugging</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #569cd6;">if</span> <span style="color: #ce9178;">"GPTeador de la pradera"</span> <span style="color: #569cd6;">in</span> <span style="color: #9cdcfe;">proyecto</span>.<span style="color: #9cdcfe;">colaboradores</span>:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #dcdcaa;">print</span>(<span style="color: #ce9178;">"¡ALERTA! Posible rm -rf /* camuflado"</span>)<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">proyecto</span>.<span style="color: #9cdcfe;">sandbox_mode</span> = <span style="color: #569cd6;">True</span>&nbsp;&nbsp;<span style="color: #6a9955;"># Por si las moscas</span><br>
<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #6a9955;"># Fase 3: Lanzamiento (aka. 'arrepentimiento público')</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #569cd6;">return</span> <span style="color: #dcdcaa;">Proyecto</span>(<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">nombre</span>=<span style="color: #ce9178;">"Editor-ISK"</span>, <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">versión</span>=<span style="color: #ce9178;">"0.1.1-alpha-preview-nightly"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span style="color: #9cdcfe;">soporte_vital</span>=<span style="color: #b5cea8;">42</span>&nbsp;&nbsp;<span style="color: #6a9955;"># Horas de sueño perdidas</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;)<br>
<br>
<span style="color: #6a9955;"># Corolario Zen:</span><br>
<span style="color: #6a9955;"># "El código perfecto no existe... pero el que compila sirve"</span>
</div>

# Corolario Zen:
# "El código perfecto no existe... pero el que compila sirve"
