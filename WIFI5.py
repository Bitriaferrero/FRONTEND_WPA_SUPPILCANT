import os, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5 import uic
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import ctypes #GetSystemMetrics
import subprocess
try:
    import netifaces
except:
    sys.exit("[!] Install the netifaces library: pip install netifaces")

interfaces = netifaces.interfaces()


#Clase heredada de QMainWindow (Constructor de ventanas)
class Ventana(QMainWindow):
 #Metodo constructor de la clase
      def __init__(self):
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("WIFI.ui", self)
        self.setWindowTitle("W-HYDRA")
        #Mostrar la ventana maximizada
        self.showMaximized()
        #Fijar el tamao de la ventana
        #Fijar el tamao minimo
        self.setMinimumSize(350, 100)
        #Fijar el tamano maximo
        self.setMaximumSize(350, 270)
        qfont = QFont("Arial", 12, QFont.Bold)
        self.setFont(qfont)
        #self.btn_acceder.clicked.connect(self.form_acceder)
        #boton.clicked.connect(self.on_click)
        #Asignar un tipo de cursor
        self.setCursor(Qt.SizeAllCursor)
        self.pushButton_3.setEnabled(False)

        self.boton.clicked.connect(self.acceder)
        #Asignar estilos CSS
        #self.setStyleSheet("background-color: #000; color: #fff;")
        #Modificar estilos de uno de los elementos de la ventana
        #self.boton.setStyleSheet("background-color: #000; color: #fff; font-size: 14px;")
        #ESSID = self.lineEdit.text()
        #CLAVE = self.lineEdit_2.text()self.lenguajes.addItem("C++")
        #ENCRIPTACION = self.seguridad.text()
        # CARGO INTERFACES DE RED EN COMBOBOX
        for elemento in range(1, len(interfaces), 1):
            #print(interfaces[elemento])
            self.comboBox.addItem(interfaces[elemento])

      def acceder(self):
        #self.pushButton_3.setEnabled(True)
        ESSID = self.lineEdit.text()
        CLAVE = self.lineEdit_2.text()
        ENCRI = self.seguridad.currentText()
        INTERFACE = self.comboBox.currentText()
        #ENCRI = self.seguridad.text()
        print (ESSID , CLAVE, ENCRI, INTERFACE)
        #CREACION DE ARCHIVO WPASPLICANT
        cadena1 = 'ctrl_interface=/var/run/wpa_supplicant'  # declara cadena1
        cadena2 = 'network={'  # declara cadena2
        cadena3 = '   ssid="' + ESSID + '"'
        cadena4 = '   key_mgmt=' + ENCRI
        cadena5 = '   psk="' + CLAVE + '"'
        cadena6 = '}'
        # Abre archivo para escribir WPASUPLICANT.conf
        archivo = open( ESSID +'.conf','w')
        # GUARDA PPERFILES DE RED EXISTENTES
        archivo2 = open(ESSID + '.save', 'w')

        # Escribe cadena1 añadiendo salto de línea
        archivo.write(cadena1 + '\n' + cadena2 + '\n' + cadena3 + '\n' + cadena4 + '\n' + cadena5 + '\n' + cadena6 + '\n')
        archivo2.write(ESSID + '\n' + CLAVE + '\n' + ENCRI + '\n' + INTERFACE)
        # cierra archivo
        archivo.close
        archivo2.close

        # DONDE GUARDARLO /directorioactual/wpa_supplicant
        comando3 = "wpa_supplicant -c " + ESSID + ".conf -i" + INTERFACE
        valor3 = os.system(comando3)
        print("Resultado:", valor3)


app = QApplication(sys.argv)
#Crear un objeto de la claseself.btn_acceder.clicked.connect(self.acceder)
ventana = Ventana()
#Mostra la ventana
ventana.show()

#Ejecutar la aplicacion
app.exec_()





