# Plan: Udgiv "Static HTML conversion ready (1)" som GitHub Pages site

## Fase 1 — Klargør indhold i repo-roden
- [ ] Flyt sitets filer (*.dc.html, support.js, _ds/) fra upload-mappen til repo-roden
- [ ] Tilføj `.nojekyll` (så `_ds/` ikke ignoreres af Jekyll)
- [ ] Opret `index.html` som forside (Welcome)

## Fase 2 — Lokalisér billeder
- [ ] Kør `download-assets.sh` så billederne hentes til `./assets/` og HTML omskrives til lokale stier

## Fase 3 — Commit & push
- [ ] Konfigurer git-identitet (niels.johansen@nexigroup.com)
- [ ] Commit i separate commits (site-filer / assets)
- [ ] Push til `origin main`

## Fase 4 — Aktivér GitHub Pages
- [ ] Slå Pages til: Settings → Pages → Deploy from branch `main` / root
