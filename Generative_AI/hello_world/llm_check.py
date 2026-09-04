from huggingface_hub import model_info
import psutil

def check_before_download(model_name):
    info = model_info(model_name)
    size_gb = sum(f.size for f in info.siblings if f.size) / 1e9
    available_gb = psutil.virtual_memory().available / 1e9
    
    print(f"Model: {model_name}")
    print(f"Download size: {size_gb:.2f} GB")
    print(f"Available RAM: {available_gb:.2f} GB")
    
    if size_gb > available_gb * 0.7:  # leave headroom for OS + other apps
        print("⚠️  Risky — might run out of RAM or slow your system heavily")
    else:
        print("✅ Should run fine")

check_before_download("google/gemma-4-31B-it")