# 🎨 Grapho 3D Visualizer Agent Skill

> **Skill Transversal de Visualización Interactivas en 3D / 2.5D para Grafos de Código**  
> Transforma el JSON técnico de `grapho-agent-skill` (`overview/grapho/grapho_data.json`) en una experiencia web interactiva 3D standalone en `overview/grapho/grapho_visualizer.html`.

---

## 📌 Temas Disponibles

1. 🌌 **Sci-Fi Constellation ("Galaxia de Código")**:
   * Los módulos son sistemas estelares.
   * Los archivos son estrellas neón brillantes con código de colores según su capa (Presentation, Domain, Data).
   * Los imports son rayos de luz parpadeante de alta energía.

2. ⚔️ **Medieval RPG Waifus (Sprites 2.5D en Three.js)**:
   * **Mago (`waifu_mage.png`)**: Presentation Layer (UI, Views, Widgets).
   * **Caballero (`waifu_knight.png`)**: Domain Layer (Use Cases, Entities).
   * **Alquimista (`waifu_alchemist.png`)**: Data Layer (Repositories, DB, APIs).
   * **Boss (`waifu_boss.png`)**: Core App Root (`main.dart` / `app.py`).
   * **Alerta (`waifu_alert.png`)**: Monolitos (>300 líneas) o violaciones Clean Arch.

---

## ⚡ $-Comandos de Visualización

| Comando | Acción | Descripción |
|---|---|---|
| `$grapho3d` | Generador | Genera `overview/grapho/grapho_visualizer.html` con tema Sci-Fi. |
| `$grapho3d:scifi` | Tema Galaxia | Genera el mapa 3D neón estilo constelación. |
| `$grapho3d:rpg` | Tema Medieval RPG | Genera el mapa 2.5D de sprites Medieval RPG. |

---

## ⚡ Quick Start

**1. Instala la skill como submódulo**
```bash
git submodule add git@github.com:Agent-Rules-Ecosystem/grapho-3d-visualizer-agent-skill.git .skill/grapho-3d-visualizer-agent-skill
```

**2. Activa la skill con `$boot`**
```text
$boot
```

**3. Ejecuta el primer comando de la skill**
```text
$grapho3d:serve
```

---

