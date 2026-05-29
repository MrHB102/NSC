# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['meta_context_framework.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['yaml'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='MetaContextOS',
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='MetaContextOS',
)
