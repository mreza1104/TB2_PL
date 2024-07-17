class HTTPException(Exception):
    def __init__(self, status_code, detail):
        self.status_code = status_code
        self.detail = detail

    def __str__(self):
        return f"HTTP {self.status_code}: {self.detail}"
