# -*- mode: python ; coding: utf-8 -*-

a = Analysis(
    ['run_main.py'],
    pathex=[],
    binaries=[],
    datas=[
            (
                ".venv/Lib/site-packages/streamlit/static",
                "./streamlit/static"
            ),
            (
                ".venv/Lib/site-packages/streamlit/runtime",
                "./streamlit/runtime"
            ),
            (
                "./src",
                "./src"
            )
    ],
    hiddenimports=['streamlit'],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='run_main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='run_main',
)
