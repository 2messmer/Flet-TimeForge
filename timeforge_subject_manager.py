import flet as ft

def main(page: ft.Page):
    # ============================================
    # SECTION 1 : CONFIGURATION DE LA PAGE
    # ============================================
    page.title = "TimeForge - Mes Matières"
    page.padding = 40
    page.vertical_alignment = ft.MainAxisAlignment.START

    matieres = []

    titre = ft.Text(
        "📚 Gestion des Matières",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_400,
    )

    champ_matiere = ft.TextField(
        label="Nom de la matière",
        hint_text="Ex: Mathématiques",
        width=300,
        prefix_icon=ft.Icons.BOOK,
    )

    champ_heures = ft.TextField(
        label="Heures/semaine",
        hint_text="Ex: 6",
        width=150,
        prefix_icon=ft.Icons.ACCESS_TIME,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    message_erreur = ft.Text("", color=ft.Colors.RED_400, size=14)

    liste_visuelle = ft.ListView(
        spacing=10,
        height=300,
        expand=False,
    )

    texte_total = ft.Text(
        "📊 Total : 0h/semaine",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.GREEN_400,
    )

    # ============================================
    # VALIDATION
    # ============================================

    def valider_nom(nom):
        if not nom or not nom.strip():
            return (False, "⚠️ Le nom de la matière est requis !")

        nom_nettoye = nom.strip()

        for m in matieres:
            if m["nom"].lower() == nom_nettoye.lower():
                return (False, f"⚠️ '{nom_nettoye}' existe déjà !")

        return (True, nom_nettoye)

    def valider_heures(valeur):
        if not valeur or not valeur.strip():
            return (False, "⚠️ Le nombre d'heures est requis !")

        try:
            heures = int(valeur)
        except ValueError:
            return (False, "⚠️ Entrez un nombre entier valide !")

        if heures <= 0 or heures > 168:
            return (False, "⚠️ Les heures doivent être > 0 et <= 168 !")

        return (True, heures)

    def calculer_total():
        if len(matieres) == 0:
            return "📊 Total : 0h/semaine"
        total = 0
        for m in matieres:
            total += m["heures"]
        return f"📊 Total : {total}h/semaine"

    # ============================================
    # GÉNÉRATION UI
    # ============================================

    def creer_fonction_suppression(nom_matiere):
        def supprimer(e):
            for m in matieres:
                if m["nom"] == nom_matiere:
                    matieres.remove(m)
                    break
            liste_visuelle.controls = generer_liste_visuelle()
            texte_total.value = calculer_total()
            page.update()

        return supprimer

    def generer_liste_visuelle():
        elements = []

        if len(matieres) == 0:
            elements.append(
                ft.Text(
                    "Aucune matière ajoutée. Commence par en ajouter une ! 🚀",
                    color=ft.Colors.GREY_400,
                    italic=True,
                    size=14,
                )
            )
            return elements

        # Define container background depending on theme
        dark = (page.theme_mode == ft.ThemeMode.DARK)
        container_bg = ft.Colors.GREY_900 if dark else ft.Colors.GREY_100
        text_color = ft.Colors.WHITE if dark else ft.Colors.BLACK

        for m in matieres:
            element = ft.Container(
                content=ft.Row(
                    [
                        ft.Icon(ft.Icons.BOOK, color=ft.Colors.BLUE_400, size=20),
                        ft.Text(
                            m["nom"],
                            size=16,
                            color=text_color,
                            weight=ft.FontWeight.W_500,
                            expand=True,
                        ),
                        ft.Text(
                            f"{m['heures']}h/sem", size=14, color=ft.Colors.GREY_400
                        ),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_OUTLINE,
                            icon_color=ft.Colors.RED_400,
                            icon_size=20,
                            tooltip="Supprimer cette matière",
                            on_click=creer_fonction_suppression(m["nom"]),
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
                bgcolor=container_bg,
                border_radius=10,
                padding=10,
                
            )
            elements.append(element)

        return elements
    
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            bouton_theme.icon = ft.Icons.BRIGHTNESS_3_ROUNDED
        else:
            page.theme_mode = ft.ThemeMode.DARK
            bouton_theme.icon = ft.Icons.BRIGHTNESS_6
        
        # Rebuild l'interface de la liste pour appliquer les changements de couleurs
        liste_visuelle.controls = generer_liste_visuelle()
        page.update()
        


    # ============================================
    # ÉVÉNEMENT BOUTON
    # ============================================

    def on_click_ajouter(e):
        nom_brut = champ_matiere.value
        heures_brut = champ_heures.value

        nom_valide, nom_ou_erreur = valider_nom(nom_brut)
        if not nom_valide:
            message_erreur.value = nom_ou_erreur
            page.update()
            return

        heures_valide, heures_ou_erreur = valider_heures(heures_brut)
        if not heures_valide:
            message_erreur.value = heures_ou_erreur
            page.update()
            return

        matieres.append(
            {
                "nom": nom_ou_erreur,
                "heures": heures_ou_erreur,
            }
        )

        champ_matiere.value = ""
        champ_heures.value = ""
        message_erreur.value = ""

        liste_visuelle.controls = generer_liste_visuelle()
        texte_total.value = calculer_total()

        page.update()
        champ_matiere.focus()

    bouton_ajouter = ft.ElevatedButton(
        "➕ Ajouter",
        on_click=on_click_ajouter,
        style=ft.ButtonStyle(color=ft.Colors.WHITE, bgcolor=ft.Colors.BLUE_700),
        height=56,
    )

    page.theme_mode = ft.ThemeMode.DARK
    bouton_theme = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=toggle_theme)

    page.add(
        ft.Row(
            [
                bouton_theme
            ],
            alignment=ft.MainAxisAlignment.END
        ),
        ft.Column(
            [
                titre,
                ft.Divider(height=20, color="transparent"),
                ft.Row([champ_matiere, champ_heures, bouton_ajouter], spacing=10),
                message_erreur,
                ft.Divider(height=10, thickness=2),
                ft.Text("Mes matières :", size=18, weight=ft.FontWeight.BOLD),
                liste_visuelle,
                ft.Divider(height=10, thickness=2),
                texte_total,
            ],
            spacing=15,
        )
    )


ft.run(main)
