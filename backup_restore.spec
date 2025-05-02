# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['backup_restore.py'],
    pathex=[],
    binaries=[],
    datas=[('/home/seed/Desktop/Text_file', '.'), ('/home/seed/Desktop/Tiger.jpeg', '.'), ('/home/seed/Documents/key.key', '.')],
    hiddenimports=['cryptography.hazmat.backends.openssl', 'ssl', '_ssl'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='backup_restore',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
