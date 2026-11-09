# Zuhause Zen – Home Assistant Dashboard & Themes

Ein ruhiges Home-Assistant-Dashboard im Stil eines japanischen Gartens: echte Naturfotos im Hintergrund, darüber mattes Glas wie bei Apple. Farbe nur dort, wo gerade etwas passiert – ein Raum leuchtet in der Farbe seines Lichts, ein Bereich füllt sich, wenn dort etwas läuft.

*A calm Home Assistant dashboard inspired by Japanese gardens: real nature photos, frosted glass cards, colour only where something is happening. German labels; entity IDs are examples from a real home and must be adapted.*

## Inhalt

| Ordner | Was |
|---|---|
| `dashboard/zuhause.yaml` | Das komplette Dashboard (33 Seiten: Start, Räume, Haushalt, Klima, Licht, Media, Alarm …) |
| `themes/optik_glas.yaml` | Haupt-Theme „Optik Glas“ (hell und dunkel) |
| `themes/fest.yaml` | Fest-Themes: Weihnachten, Silvester, Ostern, Halloween |
| `www/zuhause/` | Hintergrundfotos (Wikimedia Commons, Lizenzen in `QUELLEN.md`) |
| `werkzeuge/theme_fest.py` | Erzeugt `themes/fest.yaml` – Farben dort anpassen |

## Voraussetzungen (HACS)

- [Bubble Card](https://github.com/Clooos/Bubble-Card) – fast alle Karten
- [card-mod](https://github.com/thomasloven/lovelace-card-mod) – Glas-Optik im Theme
- [Universal Remote Card](https://github.com/Nerwyn/universal-remote-card) – Fernbedienungen
- [Appliance Cards](https://github.com/skyrotter/ha-appliance-electromenager-cards) – Waschmaschine, Trockner, Spülmaschine, Saugroboter …
- Love Lock Card (HACS) – PIN-Seite (siehe Hinweis unten)

## Installation

1. `themes/*.yaml` nach `/config/themes/` kopieren. In der `configuration.yaml` muss stehen:
   ```yaml
   frontend:
     themes: !include_dir_merge_named themes/
   ```
   Danach Aktion `frontend.reload_themes` ausführen.
2. Den Ordner `www/zuhause/` nach `/config/www/zuhause/` kopieren (gab es `/config/www` vorher nicht: Home Assistant einmal neu starten).
3. Neues Dashboard anlegen → ⋮ → Bearbeiten → ⋮ → Raw-Konfigurationseditor → Inhalt von `dashboard/zuhause.yaml` einfügen.
4. **Entitäten anpassen:** Die IDs (z. B. `light.living_…`, `sensor.waschmaschine_…`) stammen aus einem echten Haus und müssen durch eure ersetzt werden. Personen heißen im Beispiel „Alex“, „Sam“, „Kind 1“ und „Kind 2“.

## Hinweise

- **PIN-Seite:** Die Love Lock Card prüft den PIN nur im Browser, er steht lesbar in der Dashboard-Konfiguration. Für echte Sicherheit (Garagentor, Alarm) lieber Codes in der Integration selbst verwenden. Im Beispiel steht der Platzhalter `1234`.
- **Fest-Themes:** Jede Seite im Dashboard hat ein eigenes Theme und Foto. Ein Fest-Theme im Profil färbt deshalb nur die Kopfleiste – für die volle Stimmung pro Seite `theme: Fest Weihnachten` und ein `xmas_*.jpg` als Hintergrund setzen.
- **Statusleiste Android:** Die Android-App färbt die Statusleiste nach `app-header-background-color`. Die Themes nutzen dort sechsstellige Hexwerte, denn achtstellige Werte (`#RRGGBBAA`) liest die Android-App als `#AARRGGBB` – die Statusleiste wird dann z. B. lila.

## Lizenz

Konfiguration, Themes und Skript: MIT (siehe `LICENSE`). Fotos: jeweilige Lizenz laut `www/zuhause/QUELLEN.md` (CC0, CC BY, CC BY-SA) – bei Weitergabe Urheber nennen, CC-BY-SA-Bilder bleiben unter CC BY-SA.
