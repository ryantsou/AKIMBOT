import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# import martypy
# import requests

class MartyController:
    """
    Rôle : Faire le pont entre l'UI et le robot physique.
    Encapsule la librairie martypy.
    """
    def connect(self):
        pass

class DanceParser:
    """
    Rôle : Lire, décoder et valider les fichiers .dance.
    """
    def parse(self, filepath):
        pass

class ChoreographyPlayer:
    """
    Rôle : Jouer les mouvements dans l'ordre (via un Thread pour ne pas bloquer l'UI).
    """
    def play(self):
        pass

class ArbitreAPIClient:
    """
    Rôle : Communiquer avec le serveur FastAPI (envoi de score, validation d'action).
    """
    def send_movement(self):
        pass

class MainWindow(QMainWindow):
    """
    Rôle : Gérer l'affichage PyQt5 (Boutons, jauges, labels).
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AKIMBOT - Client Robot")
        self.resize(800, 600)
        
        # Instanciation des sous-composants
        self.controller = MartyController()
        self.api_client = ArbitreAPIClient()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())