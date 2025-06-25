#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import json
import tempfile
import subprocess
import requests
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                               QTabWidget, QTextEdit, QPushButton, QLabel, QLineEdit,
                               QFileDialog, QMessageBox, QToolBar, QSplitter, QFontDialog,
                               QPlainTextEdit, QScrollArea, QGroupBox, QFormLayout, QComboBox)
from PySide6.QtCore import Qt, QFile, QSaveFile, QSettings, Signal, QRegularExpression, QThread, QSize
from PySide6.QtGui import (QFont, QTextCursor, QSyntaxHighlighter, QTextCharFormat, 
                          QColor, QTextDocument, QAction, QPainter, QTextFormat,
                          QPalette, QIcon)

class ConfigManager:
    """Gestor de configuración mejorado con soporte JSON"""
    def __init__(self):
        self.settings = QSettings("MiEditor", "PythonCodeEditorPro")
        self.default_config = {
            'lm_studio': {
                'endpoint': "http://localhost:8080/v1/chat/completions",
                'api_key': "",
                'selected_endpoint_type': 0
            },
            'editor': {
                'font': "",
                'default_directory': os.path.expanduser("~"),
                'theme': "dark"
            },
            'prompts': {
                'selected_prompt': 0,
                'custom_prompt': "Analiza este código Python y sugiere mejoras:"
            }
        }
        
    def get(self, key, default=None):
        """Obtiene un valor de configuración con estructura jerárquica"""
        keys = key.split('/')
        value = self.settings.value(key)
        return value if value is not None else default

    def set(self, key, value):
        """Establece un valor de configuración"""
        self.settings.setValue(key, value)

    def save(self):
        """Guarda la configuración"""
        self.settings.sync()
        
    def value(self, key, default=None):
        """Alias para compatibilidad"""
        return self.get(key, default)
        
    def save_to_json(self, file_path):
        """Guarda la configuración a un archivo JSON"""
        config = {
            'lm_studio': {
                'endpoint': self.get('lm_studio/endpoint', self.default_config['lm_studio']['endpoint']),
                'api_key': self.get('lm_studio/api_key', self.default_config['lm_studio']['api_key']),
                'selected_endpoint_type': self.get('lm_studio/selected_endpoint_type', 0)
            },
            'editor': {
                'font': self.get('editor/font', ""),
                'default_directory': self.get('editor/default_directory', self.default_config['editor']['default_directory']),
                'theme': self.get('editor/theme', "dark")
            },
            'prompts': {
                'selected_prompt': self.get('prompts/selected_prompt', 0),
                'custom_prompt': self.get('prompts/custom_prompt', self.default_config['prompts']['custom_prompt'])
            }
        }
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving config: {str(e)}")
            return False

    def load_from_json(self, file_path):
        """Carga la configuración desde un archivo JSON"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                
            # LM Studio config
            self.set('lm_studio/endpoint', config.get('lm_studio', {}).get('endpoint', self.default_config['lm_studio']['endpoint']))
            self.set('lm_studio/api_key', config.get('lm_studio', {}).get('api_key', ""))
            self.set('lm_studio/selected_endpoint_type', config.get('lm_studio', {}).get('selected_endpoint_type', 0))
            
            # Editor config
            self.set('editor/font', config.get('editor', {}).get('font', ""))
            self.set('editor/default_directory', config.get('editor', {}).get('default_directory', self.default_config['editor']['default_directory']))
            self.set('editor/theme', config.get('editor', {}).get('theme', "dark"))
            
            # Prompts config
            self.set('prompts/selected_prompt', config.get('prompts', {}).get('selected_prompt', 0))
            self.set('prompts/custom_prompt', config.get('prompts', {}).get('custom_prompt', self.default_config['prompts']['custom_prompt']))
            
            self.save()
            return True
        except Exception as e:
            print(f"Error loading config: {str(e)}")
            return False

class LineNumberArea(QWidget):
    """Área para mostrar números de línea"""
    def __init__(self, editor):
        super().__init__(editor)
        self.editor = editor

    def sizeHint(self):
        return QSize(self.editor.line_number_area_width(), 0)

    def paintEvent(self, event):
        self.editor.line_number_area_paint_event(event)

class CodeEditor(QPlainTextEdit):
    """Editor de código con números de línea y resaltado mejorado"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.line_number_area = LineNumberArea(self)
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.blockCountChanged.connect(self.update_line_number_area_width)
        self.updateRequest.connect(self.update_line_number_area)
        self.update_line_number_area_width(0)
        self.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #d4d4d4;
                selection-background-color: #264f78;
            }
        """)

    def line_number_area_width(self):
        """Calcula el ancho necesario para los números de línea"""
        digits = len(str(max(1, self.blockCount())))
        space = 10 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    def update_line_number_area_width(self, _):
        """Actualiza el margen para los números de línea"""
        self.setViewportMargins(self.line_number_area_width(), 0, 0, 0)

    def update_line_number_area(self, rect, dy):
        """Actualiza el área de números de línea al desplazarse"""
        if dy:
            self.line_number_area.scroll(0, dy)
        else:
            self.line_number_area.update(0, rect.y(), self.line_number_area.width(), rect.height())

    def resizeEvent(self, event):
        """Redimensiona el área de números de línea"""
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.line_number_area.setGeometry(cr.left(), cr.top(), self.line_number_area_width(), cr.height())

    def line_number_area_paint_event(self, event):
        """Pinta los números de línea"""
        painter = QPainter(self.line_number_area)
        painter.fillRect(event.rect(), QColor("#252526"))
        
        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.setPen(QColor("#858585"))
                painter.drawText(0, top, self.line_number_area.width() - 5, 
                                self.fontMetrics().height(),
                                Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            block_number += 1

class PythonSyntaxHighlighter(QSyntaxHighlighter):
    """Resaltador de sintaxis mejorado para Python"""
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Palabras clave
        self.keyword_format = QTextCharFormat()
        self.keyword_format.setForeground(QColor("#569cd6"))
        self.keyword_format.setFontWeight(QFont.Bold)
        
        # Auto completado de corchetes/llaves
        self.bracket_format = QTextCharFormat()
        self.bracket_format.setForeground(QColor("#ffd700"))
        
        # Strings
        self.string_format = QTextCharFormat()
        self.string_format.setForeground(QColor("#ce9178"))
        
        # Números
        self.number_format = QTextCharFormat()
        self.number_format.setForeground(QColor("#b5cea8"))
        
        # Comentarios
        self.comment_format = QTextCharFormat()
        self.comment_format.setForeground(QColor("#6a9955"))
        self.comment_format.setFontItalic(True)
        
        # Reglas
        self.rules = []
        
        # Palabras clave
        keywords = [
            'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
            'elif', 'else', 'except', 'False', 'finally', 'for', 'from', 'global',
            'if', 'import', 'in', 'is', 'lambda', 'None', 'nonlocal', 'not', 'or',
            'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield'
        ]
        self.rules.extend((QRegularExpression(rf'\b{kw}\b'), self.keyword_format) for kw in keywords)
        
        # Strings
        self.rules.append((QRegularExpression(r'"[^"\\]*(\\.[^"\\]*)*"'), self.string_format))
        self.rules.append((QRegularExpression(r"'[^'\\]*(\\.[^'\\]*)*'"), self.string_format))
        
        # Números
        self.rules.append((QRegularExpression(r'\b[0-9]+\b'), self.number_format))
        
        # Comentarios
        self.rules.append((QRegularExpression(r'#[^\n]*'), self.comment_format))
        
        # Corchetes/llaves
        self.rules.append((QRegularExpression(r'[{}()\[\]]'), self.bracket_format))

    def highlightBlock(self, text):
        """Aplica el resaltado de sintaxis"""
        for pattern, fmt in self.rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), fmt)

class AIWorker(QThread):
    """Hilo para procesamiento de IA sin bloquear la UI"""
    analysis_complete = Signal(dict)
    
    def __init__(self, endpoint, code, prompt, api_key=None, endpoint_type=0):
        super().__init__()
        self.endpoint = endpoint
        self.code = code
        self.prompt = prompt
        self.api_key = api_key
        self.endpoint_type = endpoint_type  # 0=chat, 1=completions, 2=models
    
    def run(self):
        """Envía la solicitud a la API de IA"""
        try:
            headers = {"Content-Type": "application/json"}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"
            
            if self.endpoint_type == 2:  # GET /models
                response = requests.get(self.endpoint, headers=headers, timeout=30)
                result = response.json()
                
                if response.status_code == 200:
                    models = "\n".join([m['id'] for m in result.get('data', [])])
                    self.analysis_complete.emit({
                        'status': 'success',
                        'analysis': f"Modelos disponibles:\n{models}",
                        'example': ""
                    })
                else:
                    self.analysis_complete.emit({
                        'status': 'error',
                        'message': f"Error {response.status_code}: {result.get('error', {}).get('message', 'Error desconocido')}"
                    })
                return
            
            # Preparar payload según tipo de endpoint
            if self.endpoint_type == 0:  # chat/completions
                payload = {
                    "messages": [
                        {"role": "system", "content": "Eres un asistente de programación Python."},
                        {"role": "user", "content": f"{self.prompt}\n\n{self.code}"}
                    ],
                    "temperature": 0.7,
                    "max_tokens": 3096
                }
            else:  # completions
                payload = {
                    "prompt": f"{self.prompt}\n\n{self.code}",
                    "temperature": 0.7,
                    "max_tokens": 3096
                }
            
            response = requests.post(self.endpoint, json=payload, headers=headers, timeout=30)
            result = response.json()
            
            if response.status_code == 200:
                if self.endpoint_type == 0:  # chat/completions
                    analysis = result.get("choices", [{}])[0].get("message", {}).get("content", "No se recibió respuesta válida")
                else:  # completions
                    analysis = result.get("choices", [{}])[0].get("text", "No se recibió respuesta válida")
                
                self.analysis_complete.emit({
                    'status': 'success',
                    'analysis': analysis,
                    'example': self.extract_code_example(analysis)
                })
            else:
                self.analysis_complete.emit({
                    'status': 'error',
                    'message': f"Error {response.status_code}: {result.get('error', {}).get('message', 'Error desconocido')}"
                })
        except Exception as e:
            self.analysis_complete.emit({
                'status': 'error',
                'message': f"Error de conexión: {str(e)}"
            })
    
    def extract_code_example(self, text):
        """Extrae bloques de código del texto de respuesta"""
        import re
        code_blocks = re.findall(r'```python\n(.*?)\n```', text, re.DOTALL)
        return "\n".join(code_blocks) if code_blocks else ""

class MainWindow(QMainWindow):
    """Ventana principal mejorada con todas las características"""
    def __init__(self):
        super().__init__()
        self.config = ConfigManager()
        self.current_file = None
        self.ai_worker = None
        self.default_dir = self.config.get('editor/default_directory', os.path.expanduser("~"))
        self.setup_ui()
        self.load_initial_config()
        self.setWindowTitle("Editor Iskander - 0.1")
        self.resize(1200, 800)

    def setup_ui(self):
        """Configura la interfaz de usuario mejorada"""
        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Splitter principal
        splitter = QSplitter(Qt.Horizontal)
        main_layout.addWidget(splitter)
        
        # Editor de código
        self.editor = CodeEditor()
        self.highlighter = PythonSyntaxHighlighter(self.editor.document())
        splitter.addWidget(self.editor)
        
        # Panel lateral
        side_panel = QTabWidget()
        side_panel.setMinimumWidth(250)
        splitter.addWidget(side_panel)
        # Configuración inicial de tamaños de los marcos
        splitter.setSizes([int(self.width() * 0.9), int(self.width() * 0.1)])
        
        # Pestaña de IA
        ai_tab = QWidget()
        ai_layout = QVBoxLayout(ai_tab)
        
        self.ai_response = QTextEdit()
        self.ai_response.setReadOnly(True)
        ai_layout.addWidget(QLabel("Análisis de IA:"))
        ai_layout.addWidget(self.ai_response)
        
        self.ai_example = QPlainTextEdit()
        self.ai_example.setReadOnly(False)
        ai_layout.addWidget(QLabel("Ejemplo mejorado:"))
        ai_layout.addWidget(self.ai_example)
        
        side_panel.addTab(ai_tab, "Asistente IA")
        
        # Pestaña de configuración mejorada
        side_panel.addTab(self.setup_config_tab(), "Configuración")
        
        # Barra de herramientas
        self.setup_toolbar()
        self.setup_menu()

    def setup_config_tab(self):
        """Configuración mejorada de la pestaña de configuración"""
        config_tab = QWidget()
        config_layout = QVBoxLayout(config_tab)
        
        # Grupo para configuración de LM Studio
        lm_group = QGroupBox("Configuración LM Studio")
        lm_layout = QFormLayout()
        
        self.endpoint_type_combo = QComboBox()
        self.endpoint_type_combo.addItems([
            "Chat Completions (POST /v1/chat/completions)",
            "Completions (POST /v1/completions)"
        ])
        lm_layout.addRow("Tipo de Endpoint:", self.endpoint_type_combo)
        
        self.ai_endpoint_input = QLineEdit()
        self.ai_endpoint_input.setPlaceholderText("http://localhost:8080/v1/...")
        lm_layout.addRow("Endpoint completo:", self.ai_endpoint_input)
        
        self.api_key_input = QLineEdit()
        self.api_key_input.setPlaceholderText("Opcional para LM Studio")
        self.api_key_input.setEchoMode(QLineEdit.Password)
        lm_layout.addRow("API Key:", self.api_key_input)
        
        self.test_connection_btn = QPushButton("Probar conexión")
        self.test_connection_btn.clicked.connect(self.test_ai_connection)
        lm_layout.addRow(self.test_connection_btn)
        
        lm_group.setLayout(lm_layout)
        config_layout.addWidget(lm_group)
        
        # Grupo para configuración del editor
        editor_group = QGroupBox("Configuración del Editor")
        editor_layout = QFormLayout()
        
        self.font_btn = QPushButton("Cambiar fuente")
        self.font_btn.clicked.connect(self.change_editor_font)
        editor_layout.addRow("Fuente:", self.font_btn)
        
        self.default_dir_btn = QPushButton("Seleccionar directorio")
        self.default_dir_btn.clicked.connect(self.set_default_directory)
        self.default_dir_label = QLabel(self.default_dir)
        editor_layout.addRow("Directorio predeterminado:", self.default_dir_btn)
        editor_layout.addRow("", self.default_dir_label)
        
        editor_group.setLayout(editor_layout)
        config_layout.addWidget(editor_group)
        
        # Grupo para configuración de prompts
        prompt_group = QGroupBox("Configuración de Prompts")
        prompt_layout = QVBoxLayout()
        
        self.prompt_selector = QComboBox()
        self.prompt_selector.addItems([
            "Análisis de código",
            "Refactorización",
            "Generar documentación",
            "Buscar errores",
            "Personalizado"
        ])
        prompt_layout.addWidget(self.prompt_selector)
        
        self.custom_prompt_edit = QPlainTextEdit()
        self.custom_prompt_edit.setPlaceholderText("Escribe tu prompt personalizado aquí...")
        prompt_layout.addWidget(self.custom_prompt_edit)
        
        prompt_group.setLayout(prompt_layout)
        config_layout.addWidget(prompt_group)
        
        # Botones de guardar/cargar configuración
        btn_layout = QHBoxLayout()
        self.save_config_btn = QPushButton("Guardar Configuración")
        self.save_config_btn.clicked.connect(self.save_configuration)
        btn_layout.addWidget(self.save_config_btn)
        
        self.save_json_btn = QPushButton("Guardar en JSON...")
        self.save_json_btn.clicked.connect(self.save_config_to_json)
        btn_layout.addWidget(self.save_json_btn)
        
        self.load_json_btn = QPushButton("Cargar desde JSON...")
        self.load_json_btn.clicked.connect(self.load_config_from_json)
        btn_layout.addWidget(self.load_json_btn)
        
        config_layout.addLayout(btn_layout)
        config_layout.addStretch()
        
        return config_tab

    def setup_menu(self):
        """Configura el menú principal"""
        menubar = self.menuBar()
        
        # Menú Archivo
        file_menu = menubar.addMenu("&Archivo")
        file_menu.addAction("Nuevo", self.new_file, "Ctrl+N")
        file_menu.addAction("Abrir...", self.open_file, "Ctrl+O")
        file_menu.addAction("Guardar", self.save_file, "Ctrl+S")
        file_menu.addAction("Guardar como...", self.save_file_as, "Ctrl+Shift+S")
        file_menu.addSeparator()
        file_menu.addAction("Salir", self.close, "Ctrl+Q")
        
        # Menú Herramientas
        tools_menu = menubar.addMenu("&Herramientas")
        tools_menu.addAction("Ejecutar", self.execute_code, "F5")
        tools_menu.addAction("Analizar", self.analyze_with_ai, "F6")
        tools_menu.addSeparator()
        tools_menu.addAction("Configuración", lambda: self.tab_widget.setCurrentIndex(1))

    def set_application_icon():
        """Configura el icono de la aplicación con manejo de errores"""
        try:
            # Rutas alternativas donde podría estar el icono
            possible_icon_paths = [
                "icono.png",
                "resources/icono.png",
                "images/icono.png",
                os.path.join(os.path.dirname(__file__), "icono.png"),
                "/usr/share/pixmaps/tu_app/icono.png"  # Para Linux
            ]
            
            for icon_path in possible_icon_paths:
                if os.path.exists(icon_path):
                    app_icon = QIcon(icon_path)
                    QApplication.setWindowIcon(app_icon)
                    return True
            
            # Si no se encontró el icono, usar uno por defecto del sistema
            print("Advertencia: No se encontró el archivo de icono, usando icono por defecto")
            QApplication.setWindowIcon(QApplication.style().standardIcon(QStyle.SP_ComputerIcon))
            return False
        except Exception as e:
            print(f"Error al cargar el icono: {str(e)}")
            return False

    def setup_toolbar(self):
        """Configura la barra de herramientas mejorada"""
        toolbar = self.addToolBar("Herramientas")
        
        actions = [
            ("Nuevo", "document-new", self.new_file),
            ("Abrir", "document-open", self.open_file),
            ("Guardar", "document-save", self.save_file),
            ("Guardar como", "document-save-as", self.save_file_as),
            ("Ejecutar", "system-run", self.execute_code),
            ("Analizar con IA", "tools-wizard", self.analyze_with_ai),
        ]
        
        for text, icon, callback in actions:
            action = QAction(text, self)
            action.triggered.connect(callback)
            toolbar.addAction(action)
        
        toolbar.setMovable(False)

    def load_initial_config(self):
        """Carga la configuración inicial"""
        # LM Studio config
        endpoint_type = int(self.config.get('lm_studio/selected_endpoint_type', 0))  # Convertir a int
        self.endpoint_type_combo.setCurrentIndex(endpoint_type)
        self.ai_endpoint_input.setText(self.config.get('lm_studio/endpoint', "http://localhost:8080/v1/chat/completions"))
        self.api_key_input.setText(self.config.get('lm_studio/api_key', ""))
        
        # Editor config
        # Configuración de fuente
        font_str = self.config.get('editor/font')
        if font_str:
            try:
                font = QFont()
                if font.fromString(font_str):
                    self.editor.setFont(font)
            except:
                # Si hay error al cargar la fuente, usar una predeterminada
                default_font = QFont("Monospace", 12)
                self.editor.setFont(default_font)
        else:
            # Fuente predeterminada si no hay configuración guardada
            default_font = QFont("Monospace", 12)
            self.editor.setFont(default_font)
            self.config.set('editor/font', default_font.toString())
        
        self.default_dir = self.config.get('editor/default_directory', os.path.expanduser("~"))
        self.default_dir_label.setText(self.default_dir)
        
        # Prompts config
        self.prompt_selector.setCurrentIndex(int(self.config.get('prompts/selected_prompt', 0)))  # Convertir a int
        self.custom_prompt_edit.setPlainText(self.config.get('prompts/custom_prompt', "Analiza este código Python y sugiere mejoras:"))

    def save_configuration(self):
        """Guarda la configuración actual"""
        # LM Studio config
        self.config.set('lm_studio/selected_endpoint_type', self.endpoint_type_combo.currentIndex())
        self.config.set('lm_studio/endpoint', self.ai_endpoint_input.text())
        self.config.set('lm_studio/api_key', self.api_key_input.text())
        
        # Editor config
        self.config.set('editor/default_directory', self.default_dir)
        
        # Prompts config
        self.config.set('prompts/selected_prompt', self.prompt_selector.currentIndex())
        self.config.set('prompts/custom_prompt', self.custom_prompt_edit.toPlainText())
        
        self.config.save()
        QMessageBox.information(self, "Configuración", "Configuración guardada exitosamente")

    def save_config_to_json(self):
        """Guarda la configuración a un archivo JSON"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Guardar configuración", self.default_dir, "JSON Files (*.json)"
        )
        
        if file_path:
            if self.config.save_to_json(file_path):
                QMessageBox.information(self, "Éxito", "Configuración guardada correctamente")
            else:
                QMessageBox.critical(self, "Error", "No se pudo guardar la configuración")

    def load_config_from_json(self):
        """Carga la configuración desde un archivo JSON"""
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Cargar configuración", self.default_dir, "JSON Files (*.json)"
        )
        
        if file_path:
            if self.config.load_from_json(file_path):
                self.load_initial_config()
                QMessageBox.information(self, "Éxito", "Configuración cargada correctamente")
            else:
                QMessageBox.critical(self, "Error", "No se pudo cargar la configuración")

    def change_editor_font(self):
        """Permite cambiar la fuente del editor correctamente"""
        try:
            # Obtener la fuente actual del editor
            current_font = self.editor.font()
            font_dialog = QFontDialog(current_font, self)
            # Mostrar el diálogo de selección de fuente
            font, ok = QFontDialog.getFont(current_font, self, "Seleccionar Fuente del Editor")
            if font_dialog.exec():
                selected_font = font_dialog.currentFont()
                self.editor.setFont(selected_font)
                self.config.set('editor/font', selected_font.toString())
                self.config.save()

                
                # Actualizar también el resaltador de sintaxis si es necesario
                self.highlighter.rehighlight()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo cambiar la fuente: {str(e)}")

    def set_default_directory(self):
        """Establece el directorio por defecto"""
        dir_path = QFileDialog.getExistingDirectory(self, "Seleccionar directorio predeterminado", self.default_dir)
        if dir_path:
            self.default_dir = dir_path
            self.default_dir_label.setText(dir_path)
            self.config.set('editor/default_directory', dir_path)
            self.config.save()

    def test_ai_connection(self):
        """Prueba la conexión con el endpoint de LM Studio"""
        endpoint = self.ai_endpoint_input.text().strip()
        if not endpoint:
            QMessageBox.warning(self, "Error", "Por favor ingrese un endpoint válido")
            return
        
        api_key = self.api_key_input.text().strip() or None
        endpoint_type = self.endpoint_type_combo.currentIndex()
        
        try:
            headers = {"Content-Type": "application/json"}
            if api_key:
                headers["Authorization"] = f"Bearer {api_key}"
            
            if endpoint_type == 2:  # GET /models
                response = requests.get(endpoint, headers=headers, timeout=10)
            else:  # POST /chat/completions or /completions
                payload = {"model": "default"}
                response = requests.post(endpoint, json=payload, headers=headers, timeout=10)
            
            if response.status_code == 200:
                QMessageBox.information(self, "Conexión exitosa", 
                                      f"LM Studio respondió correctamente:\n{response.json()}")
            else:
                QMessageBox.warning(self, "Error de conexión", 
                                  f"Error {response.status_code}: {response.text}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo conectar: {str(e)}")

    def get_current_prompt(self):
        """Obtiene el prompt actual según la selección"""
        prompts = [
            "Analiza este código Python y sugiere mejoras:",
            "Refactoriza este código Python para hacerlo más eficiente y legible:",
            "Genera documentación para este código Python:",
            "Busca errores potenciales en este código Python:",
            self.custom_prompt_edit.toPlainText()
        ]
        return prompts[self.prompt_selector.currentIndex()]

    def analyze_with_ai(self):
        """Envía el código a LM Studio para análisis"""
        code = self.editor.toPlainText()
        if not code.strip():
            QMessageBox.warning(self, "Error", "No hay código para analizar")
            return
        
        endpoint = self.ai_endpoint_input.text().strip()
        if not endpoint:
            QMessageBox.warning(self, "Error", "Por favor configure un endpoint válido")
            return
        
        api_key = self.api_key_input.text().strip() or None
        endpoint_type = self.endpoint_type_combo.currentIndex()
        prompt = self.get_current_prompt()
        
        self.ai_response.setPlainText("Conectando con LM Studio...")
        self.ai_worker = AIWorker(endpoint, code, prompt, api_key, endpoint_type)
        self.ai_worker.analysis_complete.connect(self.handle_ai_response)
        self.ai_worker.start()

    def handle_ai_response(self, result):
        """Procesa la respuesta de la IA"""
        if result['status'] == 'success':
            self.ai_response.setPlainText(result['analysis'])
            self.ai_example.setPlainText(result.get('example', ''))
        else:
            self.ai_response.setPlainText(f"Error: {result['message']}")

    def new_file(self):
        """Crea un nuevo archivo vacío"""
        if self.maybe_save():
            self.editor.clear()
            self.current_file = None
            self.setWindowTitle("Python Code Editor Pro - [Nuevo archivo]")

    def open_file(self):
        """Abre un archivo existente"""
        if not self.maybe_save():
            return
            
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Abrir archivo", self.default_dir, "Python Files (*.py);;All Files (*)"
        )
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    self.editor.setPlainText(f.read())
                self.current_file = file_path
                self.setWindowTitle(f"Python Code Editor Pro - {file_path}")
                self.default_dir = os.path.dirname(file_path)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo abrir el archivo:\n{str(e)}")

    def save_file(self):
        """Guarda el archivo actual"""
        if self.current_file:
            try:
                with open(self.current_file, 'w', encoding='utf-8') as f:
                    f.write(self.editor.toPlainText())
                return True
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo:\n{str(e)}")
                return False
        else:
            return self.save_file_as()

    def save_file_as(self):
        """Guarda el archivo con un nuevo nombre"""
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Guardar como", self.default_dir, "Python Files (*.py);;All Files (*)"
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.editor.toPlainText())
                self.current_file = file_path
                self.setWindowTitle(f"Python Code Editor Pro - {file_path}")
                self.default_dir = os.path.dirname(file_path)
                return True
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo guardar el archivo:\n{str(e)}")
                return False
        return False

    def maybe_save(self):
        """Pregunta si guardar cambios antes de continuar"""
        if not self.editor.document().isModified():
            return True
            
        ret = QMessageBox.question(
            self, "Documento modificado",
            "El documento ha sido modificado. ¿Desea guardar los cambios?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel
        )
        
        if ret == QMessageBox.Save:
            return self.save_file()
        elif ret == QMessageBox.Cancel:
            return False
        return True

    def execute_code(self):
        """Ejecuta el código directamente desde el archivo guardado o temporal"""
        code = self.editor.toPlainText()
        if not code.strip():
            QMessageBox.warning(self, "Error", "No hay código para ejecutar")
            return
        
        # Si el archivo está guardado, ejecutarlo directamente
        if self.current_file and os.path.exists(self.current_file):
            file_path = self.current_file
            is_temp = False
        else:
            # Si no está guardado, crear temporal
            try:
                with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as tmp:
                    tmp.write(code.encode('utf-8'))
                    file_path = tmp.name
                is_temp = True
            except Exception as e:
                QMessageBox.critical(self, "Error", f"No se pudo crear archivo temporal: {str(e)}")
                return
        
        try:
            # Construir comando para ejecutar
            cmd = f'python "{file_path}"'
            
            # Ejecutar en terminal
            if sys.platform == 'win32':
                subprocess.Popen(['start', 'cmd', '/k', cmd], shell=True)
            else:
                # En Linux, mantener el terminal abierto
                terminal_cmd = ['xfce4-terminal', '--hold', '--command', cmd]
                
                # Alternativa para otros entornos de escritorio
                try:
                    subprocess.Popen(terminal_cmd)
                except FileNotFoundError:
                    # Si xfce4-terminal no está disponible, probar con otros terminales
                    try:
                        subprocess.Popen(['gnome-terminal', '--', 'bash', '-c', f'{cmd}; exec bash'])
                    except FileNotFoundError:
                        subprocess.Popen(['xterm', '-hold', '-e', cmd])
            
            # Pequeña pausa para asegurar que el terminal abre el archivo
            QApplication.processEvents()
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo ejecutar: {str(e)}")
        finally:
            # Solo eliminar si es temporal y después de un retraso
            if is_temp:
                try:
                    # Esperar un poco antes de eliminar
                    QTimer.singleShot(5000, lambda: os.unlink(file_path) if os.path.exists(file_path) else None)
                except:
                    pass

    def closeEvent(self, event):
        """Maneja el cierre de la ventana"""
        if self.maybe_save():
            # Guardar configuración al cerrar
            self.save_configuration()
            event.accept()
        else:
            event.ignore()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.setWindowIcon(QIcon("icono.png"))
    window.show()
    sys.exit(app.exec())
