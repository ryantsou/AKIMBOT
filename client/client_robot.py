import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
# import martypy
# import requests

class MartyController:
    # Gère la connexion et les commandes directes au robot Marty
    def __init__(self, ip_address="192.168.0.100"):
        self.ip_address = ip_address
        self.connected = False
        self.marty = None  # TODO: Initialiser l'objet martypy.Marty() plus tard

    def connect(self):
        # TODO: Implémenter la vraie connexion WiFi ou USB
        print(f"Tentative de connexion à Marty sur {self.ip_address}...")
        self.connected = True
        return self.connected

class DanceParser:
    # Décode les fichiers .dance pour extraire les séquences de mouvements
    def parse(self, filepath: str) -> list:
        # TODO: Lire le fichier et parser les instructions
        print(f"Lecture de la chorégraphie : {filepath}")
        return []

class ChoreographyPlayer:
    # Exécute une liste de mouvements sans bloquer l'interface principale
    def __init__(self, controller: MartyController):
        self.controller = controller

    def play(self, sequence: list):
        # TODO: Exécuter les commandes dans un QThread
        print(f"Lancement de la chorégraphie ({len(sequence)} mouvements)")

class ArbitreAPIClient:
    # Communique avec le serveur REST pour envoyer les actions et récupérer le score
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url

    def send_movement(self, action_type: str, color: str = None):
        # TODO: Faire un POST via requests
        payload = {"action_type": action_type, "color_detected": color}
        print(f"Envoi de l'action à l'arbitre : {payload}")

class MainWindow(QMainWindow):
    # Fenêtre principale de l'application PyQt
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AKIMBOT - Client Robot")
        self.resize(800, 600)
        
        # Instanciation des sous-composants
        self.controller = MartyController()
        self.api_client = ArbitreAPIClient()
        self.parser = DanceParser()
        self.player = ChoreographyPlayer(self.controller)

        # Interface temporaire basique
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Interface AKIMBOT en cours de construction..."))
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())