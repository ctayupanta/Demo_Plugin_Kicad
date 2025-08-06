import wx
import pcbnew
import os

class PluginDemo(pcbnew.ActionPlugin):
    def __init__(self):
        super().__init__()
        # Configuración básica del plugin
        self.name = "Plugin Kicad Demo"
        self.category = "Fabricación"
        self.description = "Envía tu PCB a fabricación con un clic"
        
        # Icono para el administrador de plugins (24x24)
        self.icon_file_name = os.path.join(
            os.path.dirname(__file__), 
            "..", 
            "resources", 
            "icon.png"
        )
        
        # Icono para la barra de herramientas (16x16) - ¡CRÍTICO!
        self.toolbar_icon = os.path.join(
            os.path.dirname(__file__), 
            "icon.png"  # Archivo en la carpeta plugins/
        )
        
        # Habilita el botón en la barra de herramientas
        self.show_toolbar_button = True
        
        # Verificación de iconos (opcional, para debug)
        self._check_icons()

    def _check_icons(self):
        """Verifica que los iconos existan (solo para desarrollo)"""
        if not os.path.exists(self.icon_file_name):
            print(f"⚠️ Icono admin no encontrado: {self.icon_file_name}")
        if not os.path.exists(self.toolbar_icon):
            print(f"⚠️ Icono barra no encontrado: {self.toolbar_icon}")

    def Run(self):
        """Función que se ejecuta al hacer clic"""
        wx.MessageBox(
            "¡Archivos listos para fabricación!",
            "Plugin Kicad Demo",
            wx.OK | wx.ICON_INFORMATION
        )

# Registro automático al cargar el plugin
PluginDemo().register()