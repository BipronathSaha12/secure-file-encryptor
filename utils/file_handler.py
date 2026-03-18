def read_file(path):
    try:
        with open(path, "rb") as f:
            return f.read()
    except:
        return None

def write_file(path, data):
    with open(path, "wb") as f:
        f.write(data)