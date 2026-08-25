# 🎨 Guide for Medieval RPG Waifu Sprites

Guía para personalizar las 5 imágenes PNG fijas reutilizables con la herramienta `generate_image` o cualquier motor de IA visual:

## Asset PNG / Rol Representado

1. **`waifu_mage.png`**: Presentation Layer (UI, Widgets, Screens, Controllers). Estilo: Mago / Hechicera Neón.
2. **`waifu_knight.png`**: Domain Layer (Use Cases, Entities, Reglas de Negocio). Estilo: Paladín / Caballero Medieval.
3. **`waifu_alchemist.png`**: Data Layer (Repositories, APIs, DB, HTTP Services). Estilo: Alquimista / Pócimas.
4. **`waifu_boss.png`**: Core Main (`main.dart` / `app.py` / App Root). Estilo: Reina / Boss Final.
5. **`waifu_alert.png`**: Alerta / Monolito (>300 líneas o violaciones de capas). Estilo: Dragón o Alerta Roja.

## Especificación Técnica
- **Formato**: PNG transparente o WebP con canal Alpha (`.png`).
- **Dimensión**: 512x512 px.
- **Renderizado**: Three.js los carga como `THREE.Sprite` 2.5D con rotación billboarding mirando siempre a la cámara.
