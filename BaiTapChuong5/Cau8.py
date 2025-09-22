import os

def get_filename(path: str) -> str:
    
    return os.path.basename(path)

def get_filename_without_ext(path: str) -> str:
    
    return os.path.splitext(os.path.basename(path))[0]

path = input(r"Nhập link file nhạc (VD:d:\music\muabui.mp3):")
print("Tên file:", get_filename(path))           
print("Tên file không đuôi:", get_filename_without_ext(path))