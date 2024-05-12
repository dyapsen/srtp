# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py',
    'D:\\code\\4C\\editor\\algorithms.py',
    'D:\\code\\4C\\editor\\edit_kind.py',
    'D:\\code\\4C\\editor\\edit_mode.py',
    'D:\\code\\4C\\editor\\oprecord.py',
    'D:\\code\\4C\\editor\\point.py',
    'D:\\code\\4C\\models\\model.py',
    'D:\\code\\4C\\models\\part.py',
    'D:\\code\\4C\\models\\unet.py',
    'D:\\code\\4C\\ui\\file_ui.py',
    'D:\\code\\4C\\ui\\main_win_ui.py',
    'D:\\code\\4C\\utils\\DataFlow.py',
    'D:\\code\\4C\\utils\\Track.py',],
    pathex=['D:\\code\\4C'],
    binaries=[],
    datas=[('D:\\code\\4C\\icon', '.\\icon'),
            ('D:\\code\\4C\\settings', '.\\settings'),
            ('D:\\code\\4C\\models\\202403.pth', '.\\models'),],
    hiddenimports=[],
    hookspath=[],
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
    name='纳米材料力学分析',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='D:\\code\\4C\\icon\\namicailiao.ico'
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='coll',
)
