import sys
with open(r'C:\Users\devzu\Documents\research.csv', encoding='utf-8') as f:
    lines = f.readlines()
sys.stdout.write(str(len(lines)) + "\n")
with open(r'C:\Users\devzu\AppData\Local\Temp\claude\C--Users-devzu-Documents\d3092015-96e6-4b53-9b60-a0775041dae0\scratchpad\inspect_out.txt', 'w', encoding='utf-8') as out:
    out.write(lines[9])
    out.write(lines[10])
    out.write(lines[-1])
