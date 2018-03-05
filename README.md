# FRONTEND_WPA_SUPPLICANT
# /etc/wpa_supplicant

FRONTEND que genera un fichero WPA_SUPPLICANT .conf necesario para conectar por WIFI.
Dados los datos: SSID, ENCRIPTADO, CLAVE y ADAPTADOR DE RED, genera un fichero .conf WPA_SUPPLICANT y conecta con la red

# EJEMPLO GENERADO CON EL FRONTEND
/etc/wpa_supplicant/archivoWIFI.conf
________________________________________
ctrl_interface=/var/run/wpa_supplicant
network={
   ssid="REDWIFI"
   key_mgmt=WPA-PSK
   psk="CONTRASEÑAWIFI"
}
_________________________________________

En la versión alfa 1.0 Genera el fichero necesario y conecta lanzando comando externo.
wpa_supplicant -c/etc/wpa_supplicant/1_RED_WIFI.conf -iwlan1


# Esta pendientes para versines posteriores:
1 - gestion de perfiles WIFI.
2- WIFI RADAR el cual lista wifis cercanas y se conecta.



