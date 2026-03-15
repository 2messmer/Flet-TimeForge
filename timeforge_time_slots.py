import flet as ft


def main(page: ft.Page):
    page.title = "TimeForge - Créneaux"
    page.padding = 40
    page.scroll = "auto"

    # Liste des créneaux ajoutés
    creneaux = []

    # Données de référence
    jours_semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    heures = [f"{h:02d}:00" for h in range(7, 21)]

    # Widgets de saisie
    dropdown_jour = ft.Dropdown(
        label="Jour",
        options=[ft.dropdown.Option(jour) for jour in jours_semaine],
        width=200,
    )

    dropdown_debut = ft.Dropdown(
        label="Heure de début",
        options=[ft.dropdown.Option(h) for h in heures],
        width=150,
    )

    dropdown_fin = ft.Dropdown(
        label="Heure de fin",
        options=[ft.dropdown.Option(h) for h in heures],
        width=150,
    )

    message_erreur = ft.Text("", color=ft.Colors.RED_400, size=14)
    liste_creneaux = ft.Column(spacing=10)

    def valider_creneau(jour, debut, fin):
        """Vérifie qu'un créneau est complet, cohérent et non dupliqué."""
        if not (jour and debut and fin):
            return False, "⚠️ Tous les champs sont requis."

        if fin <= debut:
            return False, "⚠️ L'heure de fin doit être après l'heure de début."

        for creneau in creneaux:
            if (
                creneau["jour"] == jour
                and creneau["debut"] == debut
                and creneau["fin"] == fin
            ):
                return False, "⚠️ Ce créneau existe déjà."

        return True, ""

    def creer_fonction_suppression(creneau_a_supprimer):
        """Crée une fonction de suppression liée au créneau concerné."""

        def supprimer(e):
            creneaux.remove(creneau_a_supprimer)
            afficher_creneaux()

        return supprimer

    def creer_carte_creneau(creneau):
        """Crée une carte visuelle pour afficher un créneau."""
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(
                        ft.Icons.CALENDAR_TODAY,
                        color=ft.Colors.BLUE_400,
                        size=20,
                    ),
                    ft.Text(
                        f"{creneau['jour']} | {creneau['debut']} - {creneau['fin']}",
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        expand=True,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        icon_color=ft.Colors.RED_400,
                        icon_size=20,
                        tooltip="Supprimer ce créneau",
                        on_click=creer_fonction_suppression(creneau),
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
            bgcolor=ft.Colors.GREY_100,
            border_radius=10,
            padding=10,
        )

    def afficher_creneaux():
        """Met à jour l'affichage de tous les créneaux enregistrés."""
        liste_creneaux.controls.clear()

        if len(creneaux) == 0:
            liste_creneaux.controls.append(
                ft.Text(
                    "Aucun créneau ajouté pour le moment. Commence par en ajouter un.",
                    color=ft.Colors.GREY_500,
                    italic=True,
                    size=14,
                )
            )
        else:
            for creneau in creneaux:
                liste_creneaux.controls.append(creer_carte_creneau(creneau))

        page.update()

    def ajouter_creneau(e):
        """Ajoute un créneau après validation."""
        jour = dropdown_jour.value
        debut = dropdown_debut.value
        fin = dropdown_fin.value

        valide, erreur = valider_creneau(jour, debut, fin)

        if not valide:
            message_erreur.value = erreur
            page.update()
            return

        creneaux.append(
            {
                "jour": jour,
                "debut": debut,
                "fin": fin,
            }
        )

        dropdown_jour.value = None
        dropdown_debut.value = None
        dropdown_fin.value = None
        message_erreur.value = ""

        afficher_creneaux()

    btn_ajouter = ft.ElevatedButton(
        "➕ Ajouter",
        on_click=ajouter_creneau,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE_700,
        ),
        height=56,
    )

    afficher_creneaux()

    page.add(
        ft.Column(
            [
                ft.Text(
                    "📆 Mes créneaux libres",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color=ft.Colors.BLUE_400,
                ),
                ft.Divider(height=20),
                ft.Row(
                    [dropdown_jour, dropdown_debut, dropdown_fin, btn_ajouter],
                    spacing=10,
                ),
                message_erreur,
                ft.Divider(height=20, thickness=2),
                ft.Text(
                    "📤 Créneaux ajoutés",
                    size=18,
                    weight=ft.FontWeight.BOLD,
                ),
                liste_creneaux,
            ],
            spacing=15,
        )
    )


ft.run(main)
