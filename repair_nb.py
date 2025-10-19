import json, pathlib

p = pathlib.Path("FINAL_Demo.ipynb")
raw = p.read_text(encoding="utf-8")
nb = json.loads(raw)

nb.setdefault("nbformat", 4)
nb.setdefault("nbformat_minor", 5)
nb.setdefault("metadata", {})
nb.setdefault("cells", [])

for c in nb["cells"]:
    c.setdefault("metadata", {})
    if c.get("cell_type") == "code":
        c.setdefault("outputs", [])
        c.setdefault("execution_count", None)
    src = c.get("source", [])
    if isinstance(src, str):
        c["source"] = src.splitlines(keepends=True)

out = p.with_name(p.stem + "_fixed" + p.suffix)
out.write_text(json.dumps(nb, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"Wrote: {out}")
