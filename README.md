# UNF Montreal — English website

English version of the UNF Montreal website, translated from [UNFmontreal/fr](https://github.com/UNFmontreal/fr).

Deployed at: https://unfmontreal.github.io/en/

## Development

```bash
pip install jupyter-book
myst start
```

## Initial setup (one-time)

### 1. Translate all content from the French repo

Run the one-shot translation script (requires an Anthropic API key):

```bash
ANTHROPIC_API_KEY=sk-ant-... python translate_all.py
```

Then delete `translate_all.py` — it is not needed after the initial translation.

### 2. Create a GitHub PAT for cross-repo sync

The sync action in the fr repo needs write access to this repo to open pull requests.

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens
2. Create a token scoped to `UNFmontreal/en` with:
   - **Contents:** Read and write
   - **Pull requests:** Read and write
3. Add it as secret `GH_PAT` in the **fr repo's** Settings → Secrets and variables → Actions

### 3. Add the Anthropic API key to the fr repo

Add your Anthropic API key as secret `ANTHROPIC_API_KEY` in the **fr repo's** Settings → Secrets and variables → Actions. This is used by the sync action to translate changed files.

### 4. Enable GitHub Pages for this repo

Go to this repo's Settings → Pages → Source → select **GitHub Actions**.

## Translation sync

Content is kept in sync with the French source automatically:

- Any push to the `main` branch of the fr repo that touches `.md` files or `myst.yml` triggers the `sync-en.yml` action in the fr repo.
- That action detects which files changed, translates them to English using Claude, and opens a pull request here for review.
- Merge the PR once you are satisfied with the translation quality.

The flag links (🇫🇷 / 🇬🇧) on each page point to the equivalent page in the other language — the path is preserved, so `/en/facility/access` links to `/fr/facility/access` and vice versa.
