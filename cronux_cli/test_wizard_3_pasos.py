#!/usr/bin/env python3
"""
Test del wizard de 3 pasos para Cronux v0.1.1
"""

import flet as ft

def main(page: ft.Page):
    page.title = "Wizard 3 Pasos - Test"
    page.window.width = 800
    page.window.height = 600
    
    paso_actual = {"valor": 1}
    categoria_sel = {"key": "software", "nombre": "Software"}
    tipo_software_sel = {"key": "nodejs", "nombre": "Node.js", "icono": "🌐"}
    
    # Categorías (Paso 1)
    categorias = [
        {"nombre": "Software", "icono": "💻", "key": "software"},
        {"nombre": "Documentos", "icono": "📄", "key": "documentos"},
        {"nombre": "Imágenes", "icono": "🖼️", "key": "imagenes"},
    ]
    
    # Tipos de software (Paso 2)
    tipos_software = [
        {"nombre": "Node.js", "icono": "🌐", "key": "nodejs"},
        {"nombre": "Python", "icono": "🐍", "key": "python"},
        {"nombre": "Java", "icono": "☕", "key": "java"},
    ]
    
    paso1_container = ft.Container()
    paso2_container = ft.Container()
    paso3_container = ft.Container()
    
    def actualizar_paso():
        paso1_container.visible = paso_actual["valor"] == 1
        paso2_container.visible = paso_actual["valor"] == 2
        paso3_container.visible = paso_actual["valor"] == 3
        page.update()
    
    def ir_paso_2():
        if categoria_sel["key"] == "software":
            paso_actual["valor"] = 2
        else:
            paso_actual["valor"] = 3
            tipo_software_sel["key"] = categoria_sel["key"]
            tipo_software_sel["nombre"] = categoria_sel["nombre"]
        actualizar_paso()
    
    def ir_paso_3():
        paso_actual["valor"] = 3
        actualizar_paso()
    
    def volver_paso_1():
        paso_actual["valor"] = 1
        actualizar_paso()
    
    def volver_paso_2():
        paso_actual["valor"] = 2
        actualizar_paso()
    
    # Paso 1: Categoría
    paso1_container.content = ft.Column([
        ft.Text("Paso 1: Selecciona la categoría", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=20),
        ft.Row([
            ft.ElevatedButton(
                f"{cat['icono']} {cat['nombre']}",
                on_click=lambda e, c=cat: [
                    categoria_sel.update(c),
                    ir_paso_2()
                ]
            ) for cat in categorias
        ]),
    ])
    
    # Paso 2: Tipo de software
    paso2_container.content = ft.Column([
        ft.Text("Paso 2: Tipo de software", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=20),
        ft.Row([
            ft.ElevatedButton(
                f"{tipo['icono']} {tipo['nombre']}",
                on_click=lambda e, t=tipo: [
                    tipo_software_sel.update(t),
                    ir_paso_3()
                ]
            ) for tipo in tipos_software
        ]),
        ft.Container(height=20),
        ft.ElevatedButton("← Atrás", on_click=lambda _: volver_paso_1()),
    ])
    
    # Paso 3: Detalles
    paso3_container.content = ft.Column([
        ft.Text("Paso 3: Detalles del proyecto", size=24, weight=ft.FontWeight.BOLD),
        ft.Container(height=20),
        ft.Text(f"Categoría: {categoria_sel['nombre']}"),
        ft.Text(f"Tipo: {tipo_software_sel['nombre']} {tipo_software_sel.get('icono', '')}"),
        ft.Container(height=20),
        ft.TextField(label="Nombre del proyecto"),
        ft.Container(height=20),
        ft.Row([
            ft.ElevatedButton("← Atrás", on_click=lambda _: volver_paso_2() if categoria_sel["key"] == "software" else volver_paso_1()),
            ft.ElevatedButton("Crear Proyecto", on_click=lambda _: print("Crear!")),
        ]),
    ])
    
    page.add(
        ft.Column([
            paso1_container,
            paso2_container,
            paso3_container,
        ])
    )
    
    actualizar_paso()

ft.app(target=main)
