# Validation Reference

## Factory-Level Validation

Run from `E:/aipro/internet-product-factory`:

```powershell
python -m py_compile scripts/workflow_schema.py scripts/create_product_folder.py scripts/validate_stage_files.py scripts/validate_meaningful_substage.py scripts/audit_workflow_substance.py
python scripts/validate_stage_files.py
python scripts/validate_meaningful_substage.py
```

For completed products:

```powershell
python scripts/audit_workflow_substance.py --strict product-XXX
```

If the factory root is not a git repo, report that and do not initialize it unless explicitly asked.

## Product-Level Validation

From `products/product-XXX/repo`, run available checks:

```powershell
python -m unittest discover -s tests
python scripts/smoke_test.py
python -m py_compile <modified python files>
```

Use product-specific npm, Python, or build commands when present.

## Secret Scan

Before public launch:

```powershell
Get-ChildItem -Recurse -File | Select-String -Pattern 'nvapi--' -List | ForEach-Object { $_.Path }
```

Also check for `.env` and other real secrets. Never commit real NIM keys.

## Validation Meaning

Passing validators is not enough. Validators check structure and common failure modes. The agent still must enforce:

- evidence quality
- source diversity
- method fit
- implementation depth
- real-world depth
- business workflow depth
- README claim honesty
- user-ready artifact quality

If a product is runnable but shallow, classify it as `NEEDS_V2_BEFORE_LAUNCH`, `EXPERIMENT`, `PARK`, or `INTERNAL_FACTORY_TOOL`.

