import flet as ft


def main(page: ft.Page):
    page.title = "TimeForge Planner Pro"
    page.padding = 0
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 1280
    page.window_height = 760
    page.scroll = ft.ScrollMode.AUTO

    # =========================
    # Données de l'application
    # =========================
    subjects = [
        {"name": "Mathématiques", "hours": 6, "priority": "Haute"},
        {"name": "Python", "hours": 5, "priority": "Haute"},
        {"name": "Réseaux", "hours": 3, "priority": "Moyenne"},
    ]

    slots = [
        {"day": "Lundi", "start": "08:00", "end": "10:00"},
        {"day": "Mercredi", "start": "14:00", "end": "16:00"},
    ]

    days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    time_options = [f"{h:02d}:00" for h in range(7, 22)]
    priorities = ["Haute", "Moyenne", "Basse"]

    # =========================
    # Widgets partagés
    # =========================
    title_text = ft.Text(
        "TimeForge Planner Pro",
        size=26,
        weight=ft.FontWeight.BOLD,
    )

    subtitle_text = ft.Text(
        "Organise tes matières, tes créneaux et ton planning d'étude.",
        size=14,
        color=ft.Colors.GREY_700,
    )

    subject_name = ft.TextField(
        label="Nom de la matière",
        hint_text="Ex: Cybersécurité",
        width=260,
    )

    subject_hours = ft.TextField(
        label="Heures / semaine",
        hint_text="Ex: 4",
        width=180,
        keyboard_type=ft.KeyboardType.NUMBER,
    )

    subject_priority = ft.Dropdown(
        label="Priorité",
        width=180,
        options=[ft.dropdown.Option(p) for p in priorities],
        value="Moyenne",
    )

    subject_error = ft.Text("", color=ft.Colors.RED_400, size=13)
    subjects_list = ft.Column(spacing=10)

    slot_day = ft.Dropdown(
        label="Jour",
        width=180,
        options=[ft.dropdown.Option(d) for d in days],
    )

    slot_start = ft.Dropdown(
        label="Début",
        width=140,
        options=[ft.dropdown.Option(h) for h in time_options],
    )

    slot_end = ft.Dropdown(
        label="Fin",
        width=140,
        options=[ft.dropdown.Option(h) for h in time_options],
    )

    slot_error = ft.Text("", color=ft.Colors.RED_400, size=13)
    slots_list = ft.Column(spacing=10)

    weekly_board = ft.Column(spacing=14)
    dashboard_content = ft.Column(spacing=18)

    # =========================
    # Fonctions utilitaires
    # =========================
    def reset_subject_inputs():
        subject_name.value = ""
        subject_hours.value = ""
        subject_priority.value = "Moyenne"
        subject_error.value = ""

    def reset_slot_inputs():
        slot_day.value = None
        slot_start.value = None
        slot_end.value = None
        slot_error.value = ""

    def parse_hour(hour_str: str) -> int:
        return int(hour_str.split(":")[0])

    def duration_hours(start: str, end: str) -> int:
        return parse_hour(end) - parse_hour(start)

    def total_subject_hours() -> int:
        return sum(item["hours"] for item in subjects)

    def total_slot_hours() -> int:
        return sum(duration_hours(s["start"], s["end"]) for s in slots)

    def count_high_priority() -> int:
        return sum(1 for item in subjects if item["priority"] == "Haute")

    def slots_by_day():
        grouped = {d: [] for d in days}
        for item in slots:
            grouped[item["day"]].append(item)
        return grouped

    def busiest_day():
        grouped = slots_by_day()
        best_day = None
        best_total = -1
        for day, entries in grouped.items():
            current = sum(duration_hours(e["start"], e["end"]) for e in entries)
            if current > best_total:
                best_total = current
                best_day = day
        if best_total <= 0:
            return "Aucun"
        return f"{best_day} ({best_total}h)"

    # =========================
    # Validation
    # =========================
    def validate_subject():
        name = (subject_name.value or "").strip()
        hours_str = (subject_hours.value or "").strip()
        priority = subject_priority.value

        if not name or not hours_str or not priority:
            return False, "Tous les champs matière sont requis."

        try:
            hours = int(hours_str)
        except ValueError:
            return False, "Les heures doivent être un nombre entier."

        if hours <= 0 or hours > 60:
            return False, "Les heures doivent être comprises entre 1 et 60."

        for item in subjects:
            if item["name"].lower() == name.lower():
                return False, "Cette matière existe déjà."

        return True, {"name": name, "hours": hours, "priority": priority}

    def validate_slot():
        day = slot_day.value
        start = slot_start.value
        end = slot_end.value

        if not day or not start or not end:
            return False, "Tous les champs créneau sont requis."

        if end <= start:
            return False, "L'heure de fin doit être après l'heure de début."

        for item in slots:
            if item["day"] == day and item["start"] == start and item["end"] == end:
                return False, "Ce créneau existe déjà."

        return True, {"day": day, "start": start, "end": end}

    # =========================
    # Composants UI
    # =========================
    def build_stat_card(title: str, value: str, icon: str, color: str):
        return ft.Container(
            width=250,
            padding=18,
            border_radius=16,
            bgcolor=color,
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Icon(icon, size=22, color=ft.Colors.WHITE),
                            ft.Text(title, color=ft.Colors.WHITE, size=14),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                    ft.Text(
                        value,
                        size=28,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                    ),
                ],
                spacing=10,
            ),
        )

    def build_subject_card(subject):
        color_map = {
            "Haute": ft.Colors.RED_100,
            "Moyenne": ft.Colors.AMBER_100,
            "Basse": ft.Colors.GREEN_100,
        }

        def delete_subject(e):
            subjects.remove(subject)
            refresh_all()

        return ft.Container(
            padding=14,
            border_radius=14,
            bgcolor=color_map.get(subject["priority"], ft.Colors.BLUE_50),
            content=ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text(
                                subject["name"],
                                size=17,
                                weight=ft.FontWeight.BOLD,
                            ),
                            ft.Text(
                                f"{subject['hours']}h / semaine • Priorité {subject['priority']}",
                                size=13,
                                color=ft.Colors.GREY_700,
                            ),
                        ],
                        spacing=4,
                        expand=True,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        tooltip="Supprimer cette matière",
                        icon_color=ft.Colors.RED_500,
                        on_click=delete_subject,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def build_slot_card(slot):
        def delete_slot(e):
            slots.remove(slot)
            refresh_all()

        return ft.Container(
            padding=14,
            border_radius=14,
            bgcolor=ft.Colors.BLUE_50,
            content=ft.Row(
                [
                    ft.Row(
                        [
                            ft.Icon(ft.Icons.SCHEDULE, color=ft.Colors.BLUE_500),
                            ft.Text(
                                f"{slot['day']} • {slot['start']} - {slot['end']}",
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                        spacing=10,
                        expand=True,
                    ),
                    ft.Text(
                        f"{duration_hours(slot['start'], slot['end'])}h",
                        color=ft.Colors.GREY_700,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.DELETE_OUTLINE,
                        tooltip="Supprimer ce créneau",
                        icon_color=ft.Colors.RED_500,
                        on_click=delete_slot,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )

    def build_day_panel(day: str, day_slots: list):
        if not day_slots:
            content = ft.Text("Aucun créneau défini.", color=ft.Colors.GREY_500)
        else:
            content = ft.Column(
                [
                    ft.Container(
                        padding=10,
                        border_radius=10,
                        bgcolor=ft.Colors.SURFACE_CONTAINER,
                        content=ft.Row(
                            [
                                ft.Text(
                                    f"{slot['start']} - {slot['end']}",
                                    weight=ft.FontWeight.BOLD,
                                ),
                                ft.Text(
                                    f"{duration_hours(slot['start'], slot['end'])}h",
                                    color=ft.Colors.GREY_700,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                    )
                    for slot in day_slots
                ],
                spacing=8,
            )

        return ft.Container(
            padding=16,
            border_radius=16,
            bgcolor=ft.Colors.GREY_100,
            content=ft.Column(
                [
                    ft.Text(day, size=18, weight=ft.FontWeight.BOLD),
                    content,
                ],
                spacing=12,
            ),
        )

    # =========================
    # Rafraîchissement des vues
    # =========================
    def refresh_subjects():
        subjects_list.controls.clear()

        if not subjects:
            subjects_list.controls.append(
                ft.Text(
                    "Aucune matière pour le moment. Ajoute ta première matière.",
                    color=ft.Colors.GREY_600,
                    italic=True,
                )
            )
        else:
            for item in subjects:
                subjects_list.controls.append(build_subject_card(item))

    def refresh_slots():
        slots_list.controls.clear()

        if not slots:
            slots_list.controls.append(
                ft.Text(
                    "Aucun créneau défini pour le moment.",
                    color=ft.Colors.GREY_600,
                    italic=True,
                )
            )
        else:
            sorted_slots = sorted(
                slots,
                key=lambda x: (days.index(x["day"]), x["start"], x["end"]),
            )
            for item in sorted_slots:
                slots_list.controls.append(build_slot_card(item))

    def refresh_dashboard():
        dashboard_content.controls = [
            ft.Row(
                [
                    build_stat_card(
                        "Matières",
                        str(len(subjects)),
                        ft.Icons.MENU_BOOK,
                        ft.Colors.BLUE_600,
                    ),
                    build_stat_card(
                        "Heures matière",
                        f"{total_subject_hours()}h",
                        ft.Icons.TIMER,
                        ft.Colors.GREEN_600,
                    ),
                    build_stat_card(
                        "Créneaux libres",
                        str(len(slots)),
                        ft.Icons.EVENT_AVAILABLE,
                        ft.Colors.AMBER_700,
                    ),
                    build_stat_card(
                        "Priorité haute",
                        str(count_high_priority()),
                        ft.Icons.PRIORITY_HIGH,
                        ft.Colors.RED_600,
                    ),
                ],
                wrap=True,
                spacing=16,
            ),
            ft.Container(
                padding=18,
                border_radius=16,
                bgcolor=ft.Colors.GREY_100,
                content=ft.Column(
                    [
                        ft.Text(
                            "Résumé hebdomadaire",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                        ),
                        ft.Text(
                            f"Heures de travail prévues : {total_subject_hours()}h"
                        ),
                        ft.Text(
                            f"Heures de créneaux disponibles : {total_slot_hours()}h"
                        ),
                        ft.Text(f"Jour le plus chargé : {busiest_day()}"),
                        ft.Text(
                            "Conseil : garde toujours plus de créneaux disponibles que d'heures de travail prévues."
                        ),
                    ],
                    spacing=10,
                ),
            ),
        ]

    def refresh_weekly_board():
        grouped = slots_by_day()
        weekly_board.controls = [build_day_panel(day, grouped[day]) for day in days]

    def refresh_all():
        refresh_dashboard()
        refresh_subjects()
        refresh_slots()
        refresh_weekly_board()
        page.update()

    # =========================
    # Actions
    # =========================
    def add_subject(e):
        valid, result = validate_subject()
        if not valid:
            subject_error.value = result
            page.update()
            return

        subjects.append(result)
        reset_subject_inputs()
        refresh_all()

    def add_slot(e):
        valid, result = validate_slot()
        if not valid:
            slot_error.value = result
            page.update()
            return

        slots.append(result)
        reset_slot_inputs()
        refresh_all()

    def toggle_theme(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        page.update()

    # =========================
    # Vues
    # =========================
    def dashboard_view():
        return ft.Container(
            expand=True,
            padding=24,
            content=ft.Column(
                [
                    ft.Text("Tableau de bord", size=24, weight=ft.FontWeight.BOLD),
                    dashboard_content,
                ],
                spacing=18,
                scroll=ft.ScrollMode.AUTO,
            ),
        )

    def subjects_view():
        return ft.Container(
            expand=True,
            padding=24,
            content=ft.Column(
                [
                    ft.Text("Gestion des matières", size=24, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            subject_name,
                            subject_hours,
                            subject_priority,
                            ft.ElevatedButton(
                                "Ajouter",
                                icon=ft.Icons.ADD,
                                on_click=add_subject,
                                height=56,
                            ),
                        ],
                        wrap=True,
                        spacing=10,
                    ),
                    subject_error,
                    ft.Divider(),
                    subjects_list,
                ],
                spacing=16,
                scroll=ft.ScrollMode.AUTO,
            ),
        )

    def slots_view():
        return ft.Container(
            expand=True,
            padding=24,
            content=ft.Column(
                [
                    ft.Text("Créneaux disponibles", size=24, weight=ft.FontWeight.BOLD),
                    ft.Row(
                        [
                            slot_day,
                            slot_start,
                            slot_end,
                            ft.ElevatedButton(
                                "Ajouter",
                                icon=ft.Icons.ADD_ALARM,
                                on_click=add_slot,
                                height=56,
                            ),
                        ],
                        wrap=True,
                        spacing=10,
                    ),
                    slot_error,
                    ft.Divider(),
                    slots_list,
                ],
                spacing=16,
                scroll=ft.ScrollMode.AUTO,
            ),
        )

    def planner_view():
        return ft.Container(
            expand=True,
            padding=24,
            content=ft.Column(
                [
                    ft.Text("Vue hebdomadaire", size=24, weight=ft.FontWeight.BOLD),
                    ft.Text(
                        "Visualise rapidement tes créneaux libres par jour.",
                        color=ft.Colors.GREY_700,
                    ),
                    weekly_board,
                ],
                spacing=16,
                scroll=ft.ScrollMode.AUTO,
            ),
        )

    def get_view(index: int):
        if index == 0:
            return dashboard_view()
        if index == 1:
            return subjects_view()
        if index == 2:
            return slots_view()
        return planner_view()

    # =========================
    # Navigation
    # =========================
    content_area = ft.Container(expand=True)

    def on_nav_change(e):
        """Met à jour la zone principale selon l'onglet sélectionné."""
        content_area.content = get_view(e.control.selected_index)
        page.update()

    nav = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=92,
        min_extended_width=210,
        extended=False,
        height=760,
        leading=ft.Column(
            [
                ft.Container(height=12),
                ft.IconButton(
                    icon=ft.Icons.DARK_MODE,
                    tooltip="Changer le thème",
                    on_click=toggle_theme,
                ),
            ]
        ),
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.DASHBOARD_OUTLINED,
                selected_icon=ft.Icons.DASHBOARD,
                label="Dashboard",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.MENU_BOOK_OUTLINED,
                selected_icon=ft.Icons.MENU_BOOK,
                label="Matières",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.SCHEDULE_OUTLINED,
                selected_icon=ft.Icons.SCHEDULE,
                label="Créneaux",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.VIEW_WEEK_OUTLINED,
                selected_icon=ft.Icons.VIEW_WEEK,
                label="Planning",
            ),
        ],
        on_change=on_nav_change,
    )

    header = ft.Container(
        padding=ft.Padding.symmetric(horizontal=24, vertical=18),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        content=ft.Column(
            [
                title_text,
                subtitle_text,
            ],
            spacing=4,
        ),
    )

    refresh_all()
    content_area.content = dashboard_view()

    page.add(
        ft.Row(
            [
                nav,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [
                        header,
                        content_area,
                    ],
                    expand=True,
                    spacing=0,
                ),
            ],
            expand=True,
            spacing=0,
        )
    )


ft.run(main)
