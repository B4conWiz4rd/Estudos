import win32gui
def listar_janelas():
    def callback(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title and ("pokemon" in title.lower() or "mgba" in title.lower() or "vba" in title.lower()):
                print(f"[ATIVA] {title}")
    win32gui.EnumWindows(callback, None)

listar_janelas()