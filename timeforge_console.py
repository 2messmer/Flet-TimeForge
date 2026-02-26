def afficher_matieres(liste):
    if not liste:
        print("⚠️ Aucune matière ajoutée !")
        return

    print("\n📚 Tes matières :")
    for i, matiere in enumerate(liste, start=1):
        print(f"  {i}. {matiere['nom']} ➡️ {matiere['heures']}h/semaine")


def ajouter_matiere(liste, nom, heures):
    if any(m["nom"].lower() == nom.lower() for m in liste):
        print(f"⛔ '{nom}' existe déjà !")
        return

    liste.append({"nom": nom.strip(), "heures": heures})
    print(f"✅ '{nom}' ajoutée avec succès !")


def chercher_matiere(liste, nom):
    for m in liste:
        if m["nom"].lower() == nom.lower():
            print(f"📌 {m['nom']} ➡️ {m['heures']}h/semaine")
            return
    print(f"⛔ '{nom}' n'existe pas !")


def supprimer_matiere(liste, nom):
    for m in liste:
        if m["nom"].lower() == nom.lower():
            liste.remove(m)
            print(f"✅ '{nom}' supprimée !")
            return
    print(f"⛔ '{nom}' introuvable !")


def calculer_total(liste):
    total = sum(m["heures"] for m in liste)
    print(f"📊 Total : {total}h/semaine")
    return total


def menu():
    matieres = []

    while True:
        print("\n" + "=" * 50)
        print("🎓 TIMEFORGE - GESTIONNAIRE CONSOLE")
        print("=" * 50)
        print("1 ➡️ Ajouter")
        print("2 ➡️ Rechercher")
        print("3 ➡️ Supprimer")
        print("4 ➡️ Afficher tout")
        print("5 ➡️ Quitter")

        choix = input("👉 Choix (1-5) : ").strip()

        if choix == "1":
            nom = input("Nom : ").strip()
            if not nom:
                print("⚠️ Nom invalide.")
                continue

            try:
                heures = int(input("Heures/semaine : "))
                if heures <= 0:
                    print("⚠️ Heures invalides.")
                    continue
            except ValueError:
                print("⚠️ Entrez un nombre valide.")
                continue

            ajouter_matiere(matieres, nom, heures)

        elif choix == "2":
            chercher_matiere(matieres, input("Nom : ").strip())

        elif choix == "3":
            supprimer_matiere(matieres, input("Nom : ").strip())

        elif choix == "4":
            afficher_matieres(matieres)
            if matieres:
                calculer_total(matieres)

        elif choix == "5":
            print("👋 À bientôt !")
            break

        else:
            print("⚠️ Choix invalide.")


if __name__ == "__main__":
    menu()
