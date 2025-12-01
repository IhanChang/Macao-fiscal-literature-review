import importlib, pathlib
root = pathlib.Path('.').resolve()
out = root / 'tmp_pdf_imports.txt'
lines = []
for name in ['pypdf', 'PyPDF2']:
    try:
        m = importlib.import_module(name)
        lines.append(f'{name} OK {getattr(m, '__version__', '')}\n')
    except Exception as e:
        lines.append(f'{name} ERR {e}\n')
out.write_text(''.join(lines), encoding='utf-8')

