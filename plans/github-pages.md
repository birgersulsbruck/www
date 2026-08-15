# Plan: Udgiv "Static HTML conversion ready (1)" som GitHub Pages site

## Fase 1 — Klargør indhold i repo-roden
- [x] Flyt sitets filer (*.dc.html, support.js, _ds/) fra upload-mappen til repo-roden
- [x] Tilføj `.nojekyll` (så `_ds/` ikke ignoreres af Jekyll)
- [x] Opret `index.html` som forside (Welcome)

## Fase 2 — Lokalisér billeder
- [x] Kør `download-assets.sh` så billederne hentes til `./assets/` og HTML omskrives til lokale stier
- [x] Omdøb assets med procent-enkodede filnavne (%20/%26) til dekodede navne

## Fase 3 — Commit & push
- [x] Konfigurer git-identitet (niels.johansen@nexigroup.com)
- [x] Commit i separate commits (site-filer / assets)
- [x] Push til `origin main`

## Fase 4 — Aktivér GitHub Pages
- [x] Pages aktiveret med build_type=workflow — deploy via .github/workflows/pages.yml på hvert push til main
- [x] Verificeret: https://birgersulsbruck.github.io/www/ svarer 200, test.html udgivet
