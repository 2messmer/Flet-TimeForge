import flet as ft


def main(page: ft.Page):

    # ===== Configuration page =====
    page.title = "TimeForge"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 40
    page.theme_mode = ft.ThemeMode.DARK

    # ===== Widgets =====
    titre = ft.Text(
        "⏰ TimeForge",
        size=40,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_400,
    )

    sous_titre = ft.Text(
        "Générez un emploi du temps parfait en quelques clics !",
        size=18,
        text_align=ft.TextAlign.CENTER,
    )

    champ_nom = ft.TextField(label="Nom(s)", width=300)
    champ_prenom = ft.TextField(label="Prénom(s)", width=300)

    message = ft.Text("", size=18, text_align=ft.TextAlign.CENTER)

    # ===== Fonctions =====
    def reset(e):
        champ_nom.value = ""
        champ_prenom.value = ""
        message.value = ""
        page.update()

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT
            if page.theme_mode == ft.ThemeMode.DARK
            else ft.ThemeMode.DARK
        )
        page.update()

    def afficher_bienvenue(type_utilisateur, emoji, tutoiement=True):

        if not champ_prenom.value.strip():
            message.value = "⚠️ Veuillez entrer au moins votre prénom !"
            message.color = ft.Colors.ORANGE_400
            page.update()
            return

        pronom = "TE" if tutoiement else "VOUS"

        nom_complet = champ_prenom.value
        if champ_nom.value.strip():
            nom_complet += f" {champ_nom.value}"

        message.value = (
            f"{emoji} NOUS {pronom} SOUHAITONS LA BIENVENUE,\n"
            f"{type_utilisateur.upper()} {nom_complet.upper()} ! {emoji}"
        )
        message.color = ft.Colors.GREEN_400
        page.update()

    # ===== Boutons =====
    bouton_etudiant = ft.ElevatedButton(
        "🎓 Étudiant",
        on_click=lambda e: afficher_bienvenue("étudiant", "🎓", True),
        bgcolor=ft.Colors.BLUE_700,
        color=ft.Colors.WHITE,
    )

    bouton_prof = ft.ElevatedButton(
        "👨‍🏫 Professeur",
        on_click=lambda e: afficher_bienvenue("professeur", "👨‍🏫", False),
        bgcolor=ft.Colors.PURPLE_700,
        color=ft.Colors.WHITE,
    )

    bouton_reset = ft.ElevatedButton(
        "Réinitialiser",
        on_click=reset,
        bgcolor=ft.Colors.RED_500,
        color=ft.Colors.WHITE,
    )

    bouton_theme = ft.IconButton(
        icon=ft.Icons.BRIGHTNESS_6,
        on_click=toggle_theme,
    )

    # ===== Layout =====
    page.add(
        ft.Row([bouton_theme], alignment=ft.MainAxisAlignment.END),
        ft.Column(
            [
                titre,
                sous_titre,
                champ_nom,
                champ_prenom,
                ft.Row(
                    [bouton_etudiant, bouton_prof],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=20,
                ),
                message,
                bouton_reset,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
        ),
    )


ft.app(target=main)
