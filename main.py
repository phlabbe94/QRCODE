import qrcode
import argparse


if __name__ == '__main__':
    # Gestion des paramètres (texte du qrcode, nom du fichier)
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--texte", help="Texte qrcode", required=True)
    parser.add_argument("-f", "--file", help="Nom du fichier", required=True)
    args = parser.parse_args()

    text_qrcode = args.texte
    name_qrcode = args.file

    # Génération du qrcode
    img = qrcode.make(text_qrcode)
    img.save("img/{}.png".format(name_qrcode))

