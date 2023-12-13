import bcrypt

# Contraseña almacenada en la base de datos (generalmente se obtiene de la base de datos)
password_hash_from_database = b'$2b$12$SxHwHzoG.ygUC7DZ4kYd7eMzUt8NwgtHNdN9V1sJD1yN78LdozC.q'

# Contraseña proporcionada por el usuario para verificar
user_input_password = "contrasena123".encode('utf-8')  # Asegúrate de codificar la contraseña en bytes

# Verificar si la contraseña proporcionada por el usuario coincide con la contraseña almacenada
if bcrypt.checkpw(user_input_password, password_hash_from_database):
    print("La contraseña es válida.")
else:
    print("La contraseña es incorrecta.")