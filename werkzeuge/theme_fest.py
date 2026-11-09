"""Erzeugt die Fest-Themes (Weihnachten, Silvester, Ostern, Halloween) auf Basis von „Optik Glas“.
Ausgabe: homeassistant/themes/fest.yaml, Ziel auf HA: /config/themes/fest/fest.yaml.
Hintergrund kommt als Farbverlauf aus dem Theme; Seiten mit eigenem Hintergrundbild zeigen weiter ihr Bild.
"""
import json, pathlib
FONT = '-apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Segoe UI", Roboto, sans-serif'
FESTE = {
 "Fest Weihnachten": dict(acc="#B85C5C", acc2="#CDB27A", light="#E6C994", bg="#0A1A13", bg2="#0E241A", glow1="rgba(184,92,92,0.10)", glow2="rgba(205,178,122,0.07)",
     card="rgba(14,32,24,0.82)", tint="rgba(205,178,122,0.03)", chip="rgba(16,36,27,0.86)", text="#F7F2E8", text2="#CFC6B4", ok="#6FBF8A", lbg="#FAF6EE", lcard="rgba(255,252,246,0.86)", ltext="#2A1E14", bild="weihnachten_dezent.jpg"),
 "Fest Silvester": dict(acc="#FFD166", acc2="#C7B8FF", light="#FFE29A", bg="#070A1E", bg2="#121A3D", glow1="rgba(255,209,102,0.20)", glow2="rgba(199,184,255,0.18)",
     card="rgba(16,20,46,0.80)", tint="rgba(255,209,102,0.06)", chip="rgba(18,23,52,0.84)", text="#FFFDF5", text2="#C9CCE6", ok="#4ADE80", lbg="#F4F2FB", lcard="rgba(252,251,255,0.84)", ltext="#16163A"),
 "Fest Ostern": dict(acc="#F48FB1", acc2="#9CCC65", light="#FFE082", bg="#14141F", bg2="#1F2433", glow1="rgba(244,143,177,0.18)", glow2="rgba(156,204,101,0.16)",
     card="rgba(30,32,46,0.80)", tint="rgba(255,224,130,0.05)", chip="rgba(33,36,52,0.84)", text="#FFF9FB", text2="#D8D2E0", ok="#81C784", lbg="#FBF7EF", lcard="rgba(255,253,248,0.86)", ltext="#3A2E3A"),
 "Fest Halloween": dict(acc="#FF7A1A", acc2="#9B5DE5", light="#FFB347", bg="#0E0814", bg2="#1E0F2A", glow1="rgba(255,122,26,0.22)", glow2="rgba(155,93,229,0.20)",
     card="rgba(26,14,36,0.82)", tint="rgba(255,122,26,0.06)", chip="rgba(30,16,42,0.86)", text="#FFF4EA", text2="#D6C6E3", ok="#9BE564", lbg="#F7F0FA", lcard="rgba(253,249,255,0.84)", ltext="#2A1636"),
}
def theme(name, c):
    dark_bg = f"radial-gradient(120% 60% at 15% 0%, {c['glow1']} 0%, transparent 60%), radial-gradient(90% 50% at 100% 100%, {c['glow2']} 0%, transparent 60%), linear-gradient(180deg, {c['bg2']} 0%, {c['bg']} 70%) fixed, {c['bg']}"
    if c.get("bild"):  # Bild aus /config/www/zuhause, Verlauf bleibt als Schleier darüber
        dark_bg = f"linear-gradient(180deg, {c['bg']}66 0%, {c['bg']}B3 100%) fixed, url('/local/zuhause/{c['bild']}') center / cover no-repeat fixed, {c['bg']}"
    light_bg = f"radial-gradient(120% 60% at 15% 0%, {c['glow1']} 0%, transparent 60%), radial-gradient(90% 50% at 100% 100%, {c['glow2']} 0%, transparent 60%), {c['lbg']}"
    return {
      "primary-font-family": FONT, "ha-font-family-body": FONT,
      "ha-card-border-radius": "24px", "ha-card-border-width": "1px", "ha-card-border-style": "solid",
      "ha-card-border-color": "var(--fest-border)", "ha-card-background": "var(--fest-card)", "ha-card-backdrop-filter": "blur(14px) saturate(120%)",
      "ha-card-box-shadow": "var(--fest-shadow)", "card-background-color": "var(--fest-card-solid)",
      "mush-chip-border-radius": "16px", "mush-chip-height": "36px", "mush-chip-spacing": "8px", "mush-chip-background": "var(--fest-chip)",
      "mush-card-primary-font-weight": "600", "mush-card-secondary-font-weight": "400",
      "primary-color": c["acc"], "accent-color": c["acc2"], "dark-primary-color": c["acc"], "light-primary-color": c["acc2"],
      "state-active-color": c["acc"], "state-icon-active-color": c["acc"], "state-light-active-color": c["light"],
      "state-switch-active-color": c["acc"], "state-cover-open-color": c["acc2"], "state-media_player-active-color": c["acc2"],
      "state-person-home-color": c["ok"], "state-lock-locked-color": c["ok"], "success-color": c["ok"],
      "bubble-accent-color": c["acc"], "bubble-border-radius": "22px", "bubble-main-background-color": "var(--fest-chip)", "bubble-secondary-background-color": "var(--fest-control)",
      "ha-dialog-surface-border-radius": "28px", "ha-dialog-surface-background": "var(--fest-dialog)",
      "card-mod-theme": name,
      "card-mod-card": "ha-card {\n  background: var(--fest-card);\n  border: 1px solid var(--fest-border);\n  box-shadow: var(--fest-shadow);\n  backdrop-filter: blur(14px) saturate(120%);\n  -webkit-backdrop-filter: blur(14px) saturate(120%);\n}",
      "modes": {
        "dark": {
          "fest-card": f"linear-gradient(135deg, rgba(255,255,255,0.06) 0%, rgba(255,255,255,0.015) 46%, {c['tint']} 100%), {c['card']}",
          "fest-card-solid": c["card"], "fest-chip": c["chip"], "fest-control": "rgba(255,255,255,0.10)", "fest-border": "rgba(255,255,255,0.11)",
          "fest-shadow": "0 6px 16px rgba(0,0,0,0.28), inset 0 1px 0 rgba(255,255,255,0.10)", "fest-dialog": c["card"].replace("0.80","0.96").replace("0.82","0.96"),
          "lovelace-background": dark_bg, "primary-background-color": c["bg"], "secondary-background-color": c["bg2"],
          "app-header-background-color": c["bg"] + "CC", "app-theme-color": c["bg"], "app-header-text-color": c["text"], "app-header-border-bottom": "1px solid rgba(255,255,255,0.08)",
          "primary-text-color": c["text"], "secondary-text-color": c["text2"], "divider-color": "rgba(255,255,255,0.10)", "state-icon-color": c["text2"],
        },
        "light": {
          "fest-card": f"linear-gradient(135deg, rgba(255,255,255,0.20) 0%, rgba(255,255,255,0.05) 48%, {c['tint']} 100%), {c['lcard']}",
          "fest-card-solid": c["lcard"], "fest-chip": c["lcard"], "fest-control": "rgba(0,0,0,0.06)", "fest-border": "rgba(255,255,255,0.45)",
          "fest-shadow": "0 4px 12px rgba(40,30,20,0.10), inset 0 1px 0 rgba(255,255,255,0.5)", "fest-dialog": c["lcard"].replace("0.84","0.97").replace("0.86","0.97"),
          "lovelace-background": light_bg, "primary-background-color": c["lbg"], "app-header-background-color": c["lbg"] + "D9", "app-theme-color": c["lbg"],
          "app-header-text-color": c["ltext"], "primary-text-color": c["ltext"], "secondary-text-color": c["ltext"] + "AA", "divider-color": "rgba(0,0,0,0.10)",
        },
      },
    }
out = pathlib.Path(__file__).resolve().parents[1] / "themes" / "fest.yaml"
out.write_text("# Fest-Themes, erzeugt von werkzeuge/theme_fest.py. JSON ist gültiges YAML. Ziel: /config/themes/fest/fest.yaml\n" + json.dumps({n: theme(n, c) for n, c in FESTE.items()}, ensure_ascii=False, indent=1) + "\n")
print(out, len(FESTE), "Themes")
