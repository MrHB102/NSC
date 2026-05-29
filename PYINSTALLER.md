# Build com PyInstaller

No Windows:

```powershell
python -m pip install pyinstaller
pyinstaller --onefile --name MetaContextOS meta_context_framework.py
```

No Linux/macOS:

```bash
python -m pip install pyinstaller
pyinstaller --onefile --name MetaContextOS meta_context_framework.py
```

O arquivo `meta_context_framework.spec` já está incluído para ajustes.
