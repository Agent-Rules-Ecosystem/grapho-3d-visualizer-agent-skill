# 🎨 Registro de $-Comandos de Grapho 3D Visualizer

## Comandos de Visualización

- `$grapho3d`: Lee `overview/grapho/grapho_data.json` y genera `overview/grapho/grapho_visualizer.html` utilizando el tema Sci-Fi Constellation.
- `$grapho3d:scifi`: Genera la experiencia 3D estilo Constelación Neón / Galaxia de código.
- `$grapho3d:rpg`: Genera la experiencia 2.5D con sprites Medieval RPG Waifus (`waifu_mage`, `waifu_knight`, `waifu_alchemist`, `waifu_boss`, `waifu_alert`).

## Comandos de Aprendizaje y Evolución

- `$learngrapho3d "<descripción>"`: Registra una mejora candidata en `overview/learning.md` del proyecto, **marcada con el tag `[grapho-3d-visualizer-agent-skill]`**, para ser promovida al repositorio oficial. Incluir: qué mejorar, por qué y en qué archivo de la skill aplica.
- `$revlearngrapho3d`: Revisa todas las entradas `[grapho-3d-visualizer-agent-skill]` pendientes en `overview/learning.md` y propone cuáles están listas para ser aplicadas en el repositorio oficial.

### Formato de entrada en `overview/learning.md`

```markdown
### [grapho-3d-visualizer-agent-skill] <título del aprendizaje>

- **Fecha**: YYYY-MM-DD
- **Skill**: `grapho-3d-visualizer-agent-skill`
- **Descripción**: <Qué mejorar y por qué>
- **Archivo objetivo en la skill**: `scripts/generate_visualizer.py` (ejemplo)
- **Estado**: `PENDIENTE` | `APLICADO`
```

> Para aplicar mejoras al repositorio oficial, usar `$revlearngrapho3d` y luego hacer PR en `github.com/Agent-Rules-Ecosystem/grapho-3d-visualizer-agent-skill`.
