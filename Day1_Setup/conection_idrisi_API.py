# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 20:10:46 2025

@author: Admin
"""

import win32com.client


try:
    # Intentar crear la instancia del servidor COM
    IDRISI32 = win32com.client.Dispatch('IDRISI32.IdrisiAPIServer')
    print("✅ Conexión exitosa con IDRISI API.")
    
    # Comprobar si el objeto tiene algún método o propiedad
    #print("🔍 Métodos disponibles:", dir(IDRISI32))

except Exception as e:
    print(f"❌ Error al conectar con IDRISI: {e}")



# Set IDRISI working directory path the data folder. If you are using this code, you must update the file path here. 
IDRISI32.SetWorkingDir("C:/Users/Admin/Desktop/Terrset")

# Display a .rst file this optional and if yu want to try it change, you must update the file path on the command.
IDRISI32.DisplayFile('Abril-2019/Indices/lswi_abril_2019_pol.rst', 'greyscale')
