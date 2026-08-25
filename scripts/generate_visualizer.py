#!/usr/bin/env python3
"""
generate_visualizer.py — Generates `overview/grapho/grapho_visualizer.html` from `overview/grapho/grapho_data.json`.
Supports two themes: 'scifi' (Sci-Fi Constellation) and 'rpg' (Medieval RPG Waifu Sprites).
"""

import os
import sys
import json

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Grapho 3D Visualizer — {project_name}</title>
  <style>
    body {{
      margin: 0;
      padding: 0;
      overflow: hidden;
      background-color: #050508;
      font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      color: #fff;
    }}
    #canvas-container {{
      width: 100vw;
      height: 100vh;
      display: block;
    }}
    #ui-panel {{
      position: absolute;
      top: 20px;
      left: 20px;
      background: rgba(10, 15, 30, 0.85);
      border: 1px solid #00f0ff;
      border-radius: 12px;
      padding: 16px 20px;
      box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
      backdrop-filter: blur(10px);
      max-width: 320px;
    }}
    h2 {{
      margin: 0 0 8px 0;
      font-size: 1.2rem;
      color: #00f0ff;
      text-transform: uppercase;
      letter-spacing: 1px;
    }}
    .stat-badge {{
      display: inline-block;
      background: rgba(0, 240, 255, 0.1);
      border: 1px solid rgba(0, 240, 255, 0.3);
      padding: 4px 8px;
      border-radius: 6px;
      font-size: 0.8rem;
      margin-right: 6px;
      margin-bottom: 6px;
    }}
    #info-card {{
      position: absolute;
      bottom: 20px;
      right: 20px;
      background: rgba(15, 20, 35, 0.9);
      border: 1px solid #a855f7;
      border-radius: 10px;
      padding: 16px;
      display: none;
      max-width: 300px;
      box-shadow: 0 0 15px rgba(168, 85, 247, 0.3);
    }}
  </style>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
</head>
<body>
  <div id="ui-panel">
    <h2>🕸️ Grapho 3D — {project_name}</h2>
    <div style="margin-top: 10px;">
      <span class="stat-badge">Archivos: <strong>{total_files}</strong></span>
      <span class="stat-badge">Líneas: <strong>{total_lines}</strong></span>
      <span class="stat-badge" style="border-color: #ff0055; color: #ff0055;">Monolitos: <strong>{monolith_count}</strong></span>
      <span class="stat-badge">Tema: <strong>{theme_name}</strong></span>
    </div>
    <p style="font-size: 0.8rem; color: #8899ac; margin-top: 10px;">
      Haz clic y arrastra para orbitar en 3D. Haz clic en un nodo para inspeccionar detalles.
    </p>
  </div>

  <div id="info-card">
    <h3 id="card-title" style="margin:0 0 6px 0; color:#a855f7;">-</h3>
    <p id="card-body" style="font-size:0.85rem; margin:0; color:#ccc;">-</p>
  </div>

  <div id="canvas-container"></div>

  <script>
    const graphData = {graph_data_json};
    const theme = "{theme}";

    // Setup Scene, Camera, Renderer
    const container = document.getElementById('canvas-container');
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x050508, 0.002);

    const camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 0.1, 2000);
    camera.position.set(0, 100, 250);

    const renderer = new THREE.WebGLRenderer({{ antialias: true }});
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(window.devicePixelRatio);
    container.appendChild(renderer.domElement);

    const controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;

    // Ambient & Point Lights
    scene.add(new THREE.AmbientLight(0xffffff, 0.8));
    const pointLight = new THREE.PointLight(0x00f0ff, 2, 500);
    pointLight.position.set(0, 50, 0);
    scene.add(pointLight);

    // Color Palette
    const layerColors = {{
      'presentation': 0x00f0ff,
      'domain': 0x00ff66,
      'data': 0xa855f7,
      'core': 0xffd700,
      'root': 0xffa500,
      'other': 0x8899ac
    }};

    // Position Nodes in 3D Space by Layer
    const layerRadius = {{
      'root': 0,
      'domain': 40,
      'presentation': 90,
      'data': 140,
      'core': 180,
      'other': 220
    }};

    const nodeObjects = [];
    const nodeMap = {{}};

    graphData.nodes.forEach((node, index) => {{
      const radius = layerRadius[node.layer] || 100;
      const angle = (index / graphData.nodes.length) * Math.PI * 2;
      const x = Math.cos(angle) * radius + (Math.random() - 0.5) * 20;
      const y = (Math.random() - 0.5) * 40;
      const z = Math.sin(angle) * radius + (Math.random() - 0.5) * 20;

      let mesh;
      const color = node.is_monolith ? 0xff0055 : (layerColors[node.layer] || 0x00f0ff);

      if (theme === 'rpg') {{
        // 2.5D Sprite Mesh
        const canvas = document.createElement('canvas');
        canvas.width = 128;
        canvas.height = 128;
        const ctx = canvas.getContext('2d');
        ctx.fillStyle = '#' + color.toString(16).padStart(6, '0');
        ctx.beginPath();
        ctx.arc(64, 64, 50, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#ffffff';
        ctx.font = 'bold 20px sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        const roleIcon = node.layer === 'presentation' ? '🧙‍♀️' : node.layer === 'domain' ? '⚔️' : node.layer === 'data' ? '🧪' : '👑';
        ctx.fillText(roleIcon, 64, 64);

        const texture = new THREE.CanvasTexture(canvas);
        const material = new THREE.SpriteMaterial({{ map: texture }});
        mesh = new THREE.Sprite(material);
        mesh.scale.set(20, 20, 1);
      }} else {{
        // Sci-Fi Glowing Sphere Node
        const geometry = new THREE.SphereGeometry(node.is_monolith ? 6 : 3.5, 16, 16);
        const material = new THREE.MeshBasicMaterial({{ color: color, wireframe: false }});
        mesh = new THREE.Mesh(geometry, material);
      }}

      mesh.position.set(x, y, z);
      mesh.userData = node;
      scene.add(mesh);
      nodeObjects.push(mesh);
      nodeMap[node.id] = mesh;
    }});

    // Draw Beam Edges
    const lineMaterial = new THREE.LineBasicMaterial({{ color: 0x00f0ff, transparent: true, opacity: 0.3 }});
    graphData.edges.forEach(edge => {{
      const src = nodeMap[edge.from];
      const dst = nodeMap[edge.to];
      if (src && dst) {{
        const geometry = new THREE.BufferGeometry().setFromPoints([src.position, dst.position]);
        const line = new THREE.Line(geometry, lineMaterial);
        scene.add(line);
      }}
    }});

    // Raycaster for Clicking
    const raycaster = new THREE.Raycaster();
    const mouse = new THREE.Vector2();

    window.addEventListener('click', (event) => {{
      mouse.x = (event.clientX / window.innerWidth) * 2 - 1;
      mouse.y = -(event.clientY / window.innerHeight) * 2 + 1;
      raycaster.setFromCamera(mouse, camera);
      const intersects = raycaster.intersectObjects(nodeObjects);

      if (intersects.length > 0) {{
        const node = intersects[0].object.userData;
        document.getElementById('card-title').innerText = node.label;
        document.getElementById('card-body').innerHTML = `
          <strong>Ruta:</strong> ${{node.id}}<br>
          <strong>Capa:</strong> ${{node.layer}}<br>
          <strong>Líneas:</strong> ${{node.lines}}<br>
          <strong>Estado:</strong> ${{node.is_monolith ? '🚨 Monolito (>300L)' : '✅ Saludable'}}
        `;
        document.getElementById('info-card').style.display = 'block';
      }}
    }});

    // Animation Loop
    function animate() {{
      requestAnimationFrame(animate);
      controls.update();
      scene.rotation.y += 0.0005;
      renderer.render(scene, camera);
    }}
    animate();

    window.addEventListener('resize', () => {{
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
    }});
  </script>
</body>
</html>
"""

def generate_html_visualizer(target_dir='.', theme='scifi'):
    json_path = os.path.join(target_dir, 'overview', 'grapho', 'grapho_data.json')
    
    if not os.path.exists(json_path):
        print(f"❌ Error: {json_path} no existe. Ejecuta $grapho primero para escanear el proyecto.")
        sys.exit(1)

    with open(json_path, 'r', encoding='utf-8') as f:
        graph_data = json.load(f)

    metrics = graph_data.get('metrics', {})
    theme_name = 'Medieval RPG Waifus 2.5D' if theme == 'rpg' else 'Sci-Fi Constellation 3D'

    html_content = HTML_TEMPLATE.format(
        project_name=graph_data.get('project_name', 'Proyecto'),
        total_files=metrics.get('total_files', 0),
        total_lines=metrics.get('total_lines', 0),
        monolith_count=metrics.get('monolith_count', 0),
        theme_name=theme_name,
        theme=theme,
        graph_data_json=json.dumps(graph_data)
    )

    output_dir = os.path.join(target_dir, 'overview', 'grapho')
    os.makedirs(output_dir, exist_ok=True)
    output_html = os.path.join(output_dir, 'grapho_visualizer.html')

    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✨ [Grapho 3D] Visualizador generado exitosamente en: {output_html}")
    print(f"🌐 Abre el archivo con tu navegador para ver la experiencia 3D ({theme_name}).")

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    theme_choice = sys.argv[2] if len(sys.argv) > 2 else 'scifi'
    generate_html_visualizer(target, theme_choice)
