import base64, os
d = r'C:\Users\devzu\AppData\Local\Temp\claude\C--Users-devzu-Documents\d3092015-96e6-4b53-9b60-a0775041dae0\scratchpad'
files = {
    'regular': 'pt-regular.woff2',
    'semibold': 'pt-semibold.woff2',
    'bold': 'pt-bold.woff2',
    'extrabold': 'pt-extrabold.woff2',
}
out = {}
for k, fn in files.items():
    with open(os.path.join(d, fn), 'rb') as f:
        b = f.read()
    out[k] = base64.b64encode(b).decode('ascii')
    print(k, len(b), len(out[k]))

with open(os.path.join(d, 'font_b64.py'), 'w', encoding='utf-8') as f:
    for k, v in out.items():
        f.write(f'{k} = "{v}"\n')
print("done")
