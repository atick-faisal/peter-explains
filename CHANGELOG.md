### Bug Fixes
- Raise the `google-genai` floor to `>=2.0.0`. The declared floor was `>=1.5.0`, but
  the client calls `aio.aclose()`, which only exists from 2.0.0 onward — any install
  that resolved a 1.x release failed on every command.
- Create the config directory before writing the API key, so `peter --api` no longer
  crashes on a clean install.

### Security
- Write the API key file as `0600` inside a `0700` directory.
- Restrict the cache directory to the owner, since `diskcache` unpickles its contents.
- Redact the API key from error output, including the `key=` URL query-parameter form.
- Strip control characters from model output so a response cannot emit terminal escape
  sequences.

### Changes
- Drop `keyring` (unused) and `ruff` (a linter) from the runtime dependencies.

### Internal
- The test suite now stubs the Gemini client and needs no API key; live tests moved
  behind a `live` marker and a scheduled smoke workflow.
- Pin all GitHub Actions to commit SHAs and apply least-privilege permissions.
- Refresh locked dependencies.
