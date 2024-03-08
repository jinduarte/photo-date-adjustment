import os
import ctypes
import datetime

def change_file_creation_time(file_path, new_creation_time):
    # Convert new_creation_time para um objeto FILETIME do Windows
    file_time = datetime.datetime.utcfromtimestamp(new_creation_time)
    file_time = file_time - datetime.timedelta(microseconds=file_time.microsecond)
    file_time = file_time.strftime("%Y%m%d%H%M%S")
    file_time = int(file_time)

    # Abrir o arquivo para obter o handle
    handle = ctypes.windll.kernel32.CreateFileW(file_path, ctypes.c_uint32(0x80000000), 0, None, ctypes.c_uint32(3), 0, None)

    # Definir a nova data de criação do arquivo
    ctypes.windll.kernel32.SetFileTime(handle, None, None, ctypes.byref(ctypes.c_ulonglong(file_time)))

    # Fechar o handle do arquivo
    ctypes.windll.kernel32.CloseHandle(handle)

if __name__ == "__main__":
    file_path = "Caminho_do_arquivo"
    new_creation_time = 1619539200  # Exemplo: timestamp da nova data de criação (1º de maio de 2021)

    change_file_creation_time(file_path, new_creation_time)
