# Review Architecture

Read-only grep audit of the Pulse v2 architecture contract. **Never edit a file
while running this command.** Report findings only.

Run each check against the `v2/` tree and report matches with file:line.

1. **Hex colours outside tokens** — hex colour literals anywhere except `v2/frontend/src/styles/_tokens.scss`:
   `grep -rniE "#[0-9a-f]{3,8}\b" v2/frontend/src --include=*.scss --include=*.tsx --include=*.ts | grep -v "_tokens.scss"`
2. **fetch() outside src/api/**:
   `grep -rn "fetch(" v2/frontend/src --include=*.ts --include=*.tsx | grep -v "src/api/"`
3. **fastapi imported in services/ or repositories/**:
   `grep -rn "from fastapi\|import fastapi" v2/backend/services v2/backend/repositories`
4. **Endpoint decorators in main.py**:
   `grep -n "@app\.\|@router\." v2/backend/main.py`
5. **Engine imports outside provider.py**:
   `grep -rln "engines\." v2/backend/repositories | grep -v "provider.py"`
6. **Forbidden catch-all filenames**:
   `find v2 -type f \( -name "models.py" -o -name "schemas.py" -o -name "routes.py" -o -name "utils.py" -o -name "helpers.py" -o -name "common.py" -o -name "mock_data.py" \)`
7. **Raw @media outside _mixins.scss**:
   `grep -rn "@media" v2/frontend/src --include=*.scss | grep -v "_mixins.scss"`
8. **Inline style={{ in any .tsx**:
   `grep -rn "style={{" v2/frontend/src --include=*.tsx`
9. **Route paths missing /api/v1**:
   `grep -rn "@router\.\(get\|post\|put\|delete\|patch\)(" v2/backend/api | grep -v "/api/v1"`

For each check, list violating file:line pairs (or "clean" if none). Do not
modify, stage, or suggest inline fixes — this command only reports. End the
output with exactly one line, the total count across all checks:

`VIOLATIONS: <n>`
