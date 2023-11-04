filename = input("File name: ").lower().strip()
ext = filename.split('.')[-1]
if ext in ['gif', 'png']:
    print(f"image/{ext}")
elif ext in ['jpg', 'jpeg']:
    print(f"image/jpeg")
elif ext == "bin" or not '.' in filename:
    print(f"application/octet-stream")
elif ext == "txt":
    print(f"text/plain")
else:
    print(f"application/{ext}")