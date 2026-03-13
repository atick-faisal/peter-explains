# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`peter-explains` is a CLI tool that translates Linux commands into humorous explanations using Google's Gemini AI, styled after Peter Griffin from Family Guy. The tool accepts commands, queries the Gemini API, and returns entertaining yet educational explanations with caching for performance.

## Build System & Development Commands

This project uses **uv** as the package manager. Always use `uv` commands instead of `pip`.

### Setup
```bash
uv sync --all-extras --dev  # Install all dependencies including dev dependencies
```

### Testing
```bash
# Run all tests across all Python versions (3.10, 3.11, 3.12)
uv tool run hatch test --parallel --all --retries 2

# Run tests with pytest directly
uv tool run pytest

# Tests require GOOGLE_API_KEY environment variable:
export GOOGLE_API_KEY=<YOUR_API_KEY>
```

### Linting
```bash
uv tool run ruff check
```

### Building
```bash
# Version the package
uv tool run hatch version rc

# Build distribution
uv tool run hatch build
```

### Running Locally
```bash
# After installing with: pip install -e .
peter <command>                    # Explain a command
peter --api <API_KEY>              # Set API key
peter --delete-api                 # Delete stored API key
peter --delete-cache               # Clear explanation cache
```

## Architecture

### Core Components

**Entry Point (`main.py:peter()`)**
- CLI entry point using Click
- Handles API key management, cache operations, and help display
- Dispatches to async `main()` for command explanations

**AI Integration (`peter_ai.py:PeterAi`)**
- Wraps Google Gemini API (`google-genai` library)
- Uses model: `gemini-2.5-flash` (defined in `__init__.py`)
- Two explanation modes:
  - Simple commands (no arguments): returns `CommandExplanation` with syntax, options, examples
  - Commands with arguments: returns `CommandExplanationWithArguments` with breakdown
- Safety settings configured to `BLOCK_NONE` to allow Peter Griffin's humor

**Caching System (`cache.py:PeterCache`)**
- Uses `diskcache` library for persistent local caching
- Cache location varies by OS:
  - macOS: `~/Library/Application Support/peter-explains/cache`
  - Linux: `~/.config/peter-explains/cache`
  - Windows: `%LOCALAPPDATA%/peter-explains/cache`
- Significantly speeds up repeated command lookups

**API Key Management (`api_key.py:GoogleApiKey`)**
- Stores API key in JSON file (not keyring despite docstrings)
- File location varies by OS (similar structure to cache)
- Validates key length (30-50 characters)

**Data Models (`schema.py`)**
- `CommandExplanation`: For simple commands (command, purpose, syntax, options, examples)
- `CommandExplanationWithArguments`: For complex commands (command, purpose, breakdown)
- Both use `json_repair` library to handle potentially malformed JSON from LLM

**Prompts (`prompts.py`)**
- Contains `PromptType` enum with two prompt templates
- `WITHOUT_ARGUMENTS`: Requests JSON with command structure and examples
- `WITH_ARGUMENTS`: Requests JSON with detailed breakdown of each part

### Flow

1. User invokes `peter <command>`
2. Click parses arguments, checks for flags (--api, --delete-cache, etc.)
3. If explaining command: async `main()` is called
4. Check cache first; if miss, query Gemini API with loading animation
5. Parse JSON response into appropriate schema object
6. Pretty-print result with formatting from `format.py`
7. Save result to cache for future use

## Testing Strategy

Tests in `tests/test_peter.py` cover:
- Version and help options
- API key set/delete operations
- Command explanation (both with and without arguments)
- Cache functionality (timing-based validation)

All tests use Click's `CliRunner` for isolated CLI invocations.

## CI/CD Pipeline

**CI Pipeline (`.github/workflows/ci.yml`)**
- Lint: Runs Ruff on Ubuntu with Python 3.12
- Test: Runs full test suite on Windows across Python 3.10-3.12
- Test Release: Builds and publishes to TestPyPI

**CD Pipeline (`.github/workflows/cd.yml`)**
- Triggers on version tags (e.g., `0.0.12`)
- Publishes to PyPI

## Version Management

Version is defined in `src/peter_explains/__init__.py` as `__version__`
Model name is also defined there as `__model__` (currently `gemini-2.5-flash`)

## Important Notes

- The project uses async/await for API calls and loading animations
- All LLM responses are parsed with `json_repair` to handle malformed JSON
- Commands are normalized with `.strip().lower()` before processing
- API key is required; tool provides helpful error messages if missing
- Cache dramatically improves performance for repeated queries
