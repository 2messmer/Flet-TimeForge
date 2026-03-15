import flet as ft


def main(page: ft.Page):
    page.title = "TimeForge - Navigation"
    page.padding = 0

    def vue_accueil():
        """Affiche la page d'accueil."""
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text("🏠 Accueil", size=40, weight=ft.FontWeight.BOLD),
                    ft.Text("Bienvenue dans l'application !", size=18),
                    ft.ElevatedButton("Action principale"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.BLUE_50,
            expand=True,
            padding=40,
        )

    def vue_profil():
        """Affiche la page de profil."""
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "👤 Profil",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.BLUE_700,
                    ),
                    ft.Text("Nom : Jean Dupont", size=18),
                    ft.Text("E-mail : jeandupont@gmail.com", size=18),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.GREEN_50,
            expand=True,
            padding=40,
        )

    def vue_parametres():
        """Affiche la page des paramètres."""
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "⚙️ Paramètres",
                        size=40,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.AMBER_700,
                    ),
                    ft.Switch(label="Mode sombre"),
                    ft.Switch(label="Notifications"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor=ft.Colors.GREY_100,
            expand=True,
            padding=40,
        )

    def afficher_page(index):
        """Retourne la vue correspondant à l’onglet sélectionné."""
        if index == 0:
            return vue_accueil()
        elif index == 1:
            return vue_profil()
        elif index == 2:
            return vue_parametres()
        return vue_accueil()

    def on_change_navigation(e):
        """Met à jour le contenu selon l’onglet sélectionné."""
        index = e.control.selected_index
        zone_contenu.content = afficher_page(index)
        page.update()

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.HOME_OUTLINED,
                selected_icon=ft.Icons.HOME,
                label="Accueil",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.PERSON_OUTLINED,
                selected_icon=ft.Icons.PERSON,
                label="Profil",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SETTINGS_OUTLINED,
                selected_icon=ft.Icons.SETTINGS,
                label="Paramètres",
            ),
        ],
        on_change=on_change_navigation,
    )

    zone_contenu = ft.Container(
        content=vue_accueil(),
        expand=True,
    )

    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                zone_contenu,
            ],
            expand=True,
        )
    )


ft.run(main)
