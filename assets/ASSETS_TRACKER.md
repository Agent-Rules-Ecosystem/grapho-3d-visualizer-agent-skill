# 🎨 Assets Tracker — `grapho-3d-visualizer-agent-skill`

> Estado de los assets visuales para cada template. Usar `generate_image` del agente para crear los PNGs definitivos y reemplazar los placeholders.

---

## 📂 Estructura

```text
assets/
├── ASSETS_TRACKER.md         ← Este archivo
├── rpg/                      ← Sprites 2.5D Medieval RPG Waifus
│   ├── waifu_placeholder.png ← Fantasma genérico (reemplazar cada sprite)
│   ├── waifu_mage.png        ← 🧙‍♀️ Presentation Layer    [PENDIENTE]
│   ├── waifu_knight.png      ← ⚔️  Domain Layer          [PENDIENTE]
│   ├── waifu_alchemist.png   ← 🧪  Data Layer            [PENDIENTE]
│   ├── waifu_boss.png        ← 👑  Core / App Root       [PENDIENTE]
│   └── waifu_alert.png       ← 🚨  Monolito / Violación  [PENDIENTE]
└── scifi/                    ← Texturas 3D Sci-Fi Constellation
    ├── planet_placeholder.png ← Planeta gris genérico (reemplazar)
    ├── planet_presentation.png ← 🩵 Cian  — Presentation  [PENDIENTE]
    ├── planet_domain.png       ← 💚 Verde — Domain        [PENDIENTE]
    ├── planet_data.png         ← 💜 Violeta — Data        [PENDIENTE]
    ├── planet_core.png         ← 🟡 Dorado — Core Root    [PENDIENTE]
    └── planet_alert.png        ← 🔴 Rojo  — Alerta/Mono  [PENDIENTE]
```

---

## 📋 Estado General

| Template | Asset | Archivo | Estado | Descripción |
|---|---|---|---|---|
| **RPG** | Placeholder | `rpg/waifu_placeholder.png` | ✅ Listo | Fantasma genérico para todos los slots |
| **RPG** | Mago | `rpg/waifu_mage.png` | ⏳ Pendiente | Maga neón — UI/Presentation Layer |
| **RPG** | Caballero | `rpg/waifu_knight.png` | ⏳ Pendiente | Paladín medieval — Domain Layer |
| **RPG** | Alquimista | `rpg/waifu_alchemist.png` | ⏳ Pendiente | Alquimista — Data/DB Layer |
| **RPG** | Boss | `rpg/waifu_boss.png` | ⏳ Pendiente | Reina/Boss — Core App Root |
| **RPG** | Alerta | `rpg/waifu_alert.png` | ⏳ Pendiente | Dragón rojo — Monolito o Violación |
| **Sci-Fi** | Placeholder | `scifi/planet_placeholder.png` | ✅ Listo | Planeta gris genérico |
| **Sci-Fi** | Presentation | `scifi/planet_presentation.png` | ⏳ Pendiente | Planeta cian — Presentation Layer |
| **Sci-Fi** | Domain | `scifi/planet_domain.png` | ⏳ Pendiente | Planeta verde — Domain Layer |
| **Sci-Fi** | Data | `scifi/planet_data.png` | ⏳ Pendiente | Planeta violeta — Data Layer |
| **Sci-Fi** | Core | `scifi/planet_core.png` | ⏳ Pendiente | Planeta dorado — Core Root |
| **Sci-Fi** | Alert | `scifi/planet_alert.png` | ⏳ Pendiente | Planeta rojo pulsante — Monolito |

---

## 🚀 Instrucción de Generación (para el agente)

Para generar cada imagen definitiva usa el comando `generate_image` con los siguientes prompts sugeridos:

### RPG Waifus (512x512 PNG fondo transparente)

- **`waifu_mage.png`**: `"Anime chibi waifu mage with glowing cyan robes and floating UI runes, RPG medieval fantasy style, transparent background, 512x512 sprite art"`
- **`waifu_knight.png`**: `"Anime chibi paladin waifu knight in emerald green medieval armor, RPG fantasy sprite, transparent background, 512x512"`
- **`waifu_alchemist.png`**: `"Anime chibi alchemist waifu with purple glowing potions and mystical lab equipment, fantasy RPG sprite, transparent background, 512x512"`
- **`waifu_boss.png`**: `"Anime chibi queen boss waifu in golden royal crown and regal robes, RPG fantasy final boss sprite, transparent background, 512x512"`
- **`waifu_alert.png`**: `"Anime chibi red dragon girl waifu with warning flames, danger alert sprite, RPG fantasy, transparent background, 512x512"`

### Sci-Fi Planets (512x512 PNG fondo transparente)

- **`planet_presentation.png`**: `"Glowing neon cyan sci-fi planet sphere with blue atmosphere rings, space game icon, transparent background, 512x512"`
- **`planet_domain.png`**: `"Emerald green glowing sci-fi planet with organic biome texture, space icon, transparent background, 512x512"`
- **`planet_data.png`**: `"Deep violet purple sci-fi data planet with digital grid texture and purple glow, space icon, transparent background, 512x512"`
- **`planet_core.png`**: `"Golden fiery sci-fi core planet with molten surface and golden rings, space icon, transparent background, 512x512"`
- **`planet_alert.png`**: `"Glowing red pulsing danger sci-fi planet with warning cracks, alert icon, space game, transparent background, 512x512"`

---

> **Nota**: Hasta que se generen los definitivos, el visualizador usa automáticamente `waifu_placeholder.png` y `planet_placeholder.png` respectivamente. Completar este tracker a medida que cada imagen sea creada.
