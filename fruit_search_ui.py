import flet as ft


def main(page: ft.Page):
    page.title = "Recherche de fruits"
    page.padding = 20

    # Liste de base utilisée pour la recherche
    fruits = ["Pomme", "Banane", "Orange", "Mangue", "Ananas", "Fraise"]

    # Champ de recherche
    champ_recherche = ft.TextField(
        label="Rechercher un fruit",
        hint_text="Tapez un nom...",
        expand=True,
    )

    # Zone où les fruits filtrés seront affichés
    liste_affichee = ft.Column(spacing=5)

    def afficher_fruits(liste_filtree):
        """Met à jour l'affichage avec la liste reçue."""
        liste_affichee.controls.clear()

        if not liste_filtree:
            liste_affichee.controls.append(
                ft.Text("Aucun fruit trouvé.", color=ft.Colors.RED_400)
            )
        else:
            for fruit in liste_filtree:
                liste_affichee.controls.append(ft.Text(fruit, size=16))

        page.update()

    def filtrer_fruits(e):
        """Filtre les fruits selon le texte saisi."""
        texte = champ_recherche.value.strip().lower()

        fruits_filtres = [fruit for fruit in fruits if texte in fruit.lower()]

        afficher_fruits(fruits_filtres)

    # Mise à jour automatique à chaque changement dans le champ
    champ_recherche.on_change = filtrer_fruits

    # Affichage initial de tous les fruits
    afficher_fruits(fruits)

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Recherche dynamique de fruits",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                ),
                champ_recherche,
                ft.Divider(),
                liste_affichee,
            ],
            spacing=15,
        )
    )


ft.app(target=main)