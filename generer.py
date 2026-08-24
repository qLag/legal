#!/usr/bin/env python3
"""
Régénère le corps HTML d'une politique à partir de son Markdown.

Écrit parce que les deux fichiers avaient déjà divergé une fois : le `.md` était à jour et
la page publiée annonçait encore l'inverse. Le Markdown est la seule source ; l'enveloppe
HTML (en-tête, cartouche, pied) est conservée telle quelle, seul ce qui se trouve entre les
deux marqueurs est réécrit.

    python3 generer.py qelq
"""
import html
import pathlib
import re
import sys

DEBUT = "<!-- CORPS:DEBUT -->"
FIN = "<!-- CORPS:FIN -->"


def enligne(texte: str) -> str:
    """Gras, code, liens nus. Volontairement minimal : les politiques n'ont rien d'autre."""
    t = html.escape(texte, quote=True)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w>])\*(?!\s)(.+?)(?<!\s)\*", r"<em>\1</em>", t)
    t = re.sub(r"`(.+?)`", r"<code>\1</code>", t)
    return re.sub(r"(https?://[^\s<)]+)", r'<a href="\1">\1</a>', t)


def convertir(markdown: str) -> str:
    # Le titre de niveau 1 et les deux lignes d'en-tête (date, éditeur) vivent déjà dans le
    # cartouche HTML : on les retire ligne à ligne plutôt qu'en coupant au premier séparateur,
    # ce qui emportait aussi la phrase d'introduction — laquelle, elle, n'est nulle part
    # ailleurs.
    corps = "\n".join(
        l for l in markdown.split("\n")
        if not l.startswith("# ")
        and not l.startswith("**Dernière mise à jour")
        and not l.startswith("**Éditeur")
    )
    sortie, liste, paragraphe = [], [], []

    def vider_paragraphe():
        if paragraphe:
            sortie.append("<p>" + enligne(" ".join(paragraphe)) + "</p>")
            paragraphe.clear()

    def vider_liste():
        if liste:
            sortie.append("<ul>" + "".join(f"<li>{enligne(x)}</li>" for x in liste) + "</ul>")
            liste.clear()

    for ligne in corps.split("\n"):
        nue = ligne.strip()
        if not nue:
            vider_paragraphe()
            vider_liste()
        elif nue == "---":
            vider_paragraphe()
            vider_liste()
            sortie.append("<hr>")
        elif nue.startswith("## "):
            vider_paragraphe()
            vider_liste()
            sortie.append(f"<h2>{enligne(nue[3:])}</h2>")
        elif nue.startswith("- "):
            vider_paragraphe()
            liste.append(nue[2:])
        elif liste and ligne.startswith("  "):
            liste[-1] += " " + nue          # continuation d'une puce sur plusieurs lignes
        else:
            paragraphe.append(nue)
    vider_paragraphe()
    vider_liste()
    return "\n".join(sortie)


def main(dossier: str) -> None:
    base = pathlib.Path(__file__).parent / dossier
    md = (base / "politique-de-confidentialite.md").read_text(encoding="utf-8")
    page = base / "index.html"
    html_actuel = page.read_text(encoding="utf-8")

    if DEBUT not in html_actuel or FIN not in html_actuel:
        sys.exit(f"{page} : marqueurs {DEBUT} / {FIN} absents.")

    avant, reste = html_actuel.split(DEBUT, 1)
    _, apres = reste.split(FIN, 1)

    # La date du cartouche suit celle du Markdown, sinon elle mentirait sans prévenir.
    date = re.search(r"\*\*Dernière mise à jour : (.+?)\*\*", md)
    if date:
        avant = re.sub(r"mise à jour le [^<]+", f"mise à jour le {date.group(1)}", avant)

    resultat = avant + DEBUT + "\n" + convertir(md) + "\n" + FIN + apres

    # Contrôle de fermeture des balises de structure.
    #
    # Écrit après avoir cassé la page une fois : le marqueur d'ouverture avait été posé
    # trop haut, à l'intérieur du cartouche d'en-tête, et la première génération a emporté
    # le `</div>` qui le fermait. Le navigateur ne s'en plaint pas — il imbrique
    # silencieusement tout le document dans un conteneur flex, et la politique s'affiche en
    # colonnes illisibles. Une page publiée ne doit pas pouvoir sortir d'ici dans cet état.
    for balise in ("div", "main", "ul", "p"):
        ouvrants = len(re.findall(rf"<{balise}[ >]", resultat))
        fermants = len(re.findall(rf"</{balise}>", resultat))
        if ouvrants != fermants:
            sys.exit(
                f"{page} : {ouvrants} <{balise}> pour {fermants} </{balise}>. "
                "Rien n'a été écrit. Vérifiez que le marqueur CORPS:DEBUT est bien placé "
                "après la fermeture du cartouche d'en-tête."
            )

    page.write_text(resultat, encoding="utf-8")
    print(f"{page} régénérée ({len(convertir(md))} caractères de corps), balises équilibrées.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "qelq")
