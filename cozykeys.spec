# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['cozykeys.py'],
    pathex=[],
    binaries=[],
    datas=[('mods_Cozy_sounds_keyboard1.wav', '.'), ('mods_Cozy_sounds_keyboard2.wav', '.'), ('mods_Cozy_sounds_keyboard3.wav', '.'), ('mods_Cozy_sounds_keyboard4.wav', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='cozykeys',
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
app = BUNDLE(
    exe,
    name='cozykeys.app',
    icon=None,
    bundle_identifier=None,
)
