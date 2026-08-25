---
name: grapho-3d-visualizer-agent-skill
type: runner-tooling
description: Interactive 3D/2.5D visualizer generator for Grapho data with Sci-Fi Constellation and Medieval RPG Waifu themes.
---

# 🎨 Grapho 3D Visualizer Agent Skill Directive

## Bootstrap de la Habilidad

Cuando se invoque el comando `$grapho3d` o sus variantes (`$grapho3d:scifi`, `$grapho3d:rpg`), el agente **DEBE** cargar los siguientes archivos en orden:

1. `SKILL.md` ← Matriz de temas 3D y directiva de generación de visualizador HTML.
2. `core/commands.md` ← Registro de $-comandos expuestos.
3. `core/brain.md` ← Selección de plantillas visuales y mapeo de temas.
4. `core/path_map.md` ← Ubicación de `overview/grapho/grapho_data.json` y `overview/grapho/grapho_visualizer.html`.

---

## Reglas Canónicas de Visualización 3D

1. **Ubicación Obligatoria de Salida**:
   * El visualizador generado **NUNCA** debe escribirse en la raíz del proyecto ni en la raíz de `overview/`. Debe ubicarse exclusivamente en **`overview/grapho/grapho_visualizer.html`**.

2. **Consumo del JSON de Grapho Engine**:
   * El visualizador requiere que `overview/grapho/grapho_data.json` haya sido generado por `grapho-agent-skill` (`$grapho`). Si no existe, el agente ejecutará `$grapho` primeramente.

3. **Autoconstante y Ultraligero (Three.js 60 FPS)**:
   * El archivo `grapho_visualizer.html` incluye la librería Three.js vía CDN standalone para permitir apertura directa con doble clic en cualquier navegador sin necesidad de servidor local o compilación npm.

4. **Soporte de Temas**:
   * **Sci-Fi Constellation**: Nodos como sistemas estelares/estrellas con haces neón (Jarvis UI style).
   * **Medieval RPG Waifus**: Nodos 2.5D con sprites transparentes (`waifu_mage`, `waifu_knight`, `waifu_alchemist`, `waifu_boss`, `waifu_alert`).
