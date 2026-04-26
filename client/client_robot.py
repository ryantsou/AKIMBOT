import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
import martypy
# import requests

class MockMarty:
    # Faux robot pour pouvoir tester l'interface sans le matériel
    def celebrate(self):
        print("MOCKMarty fait une danse de célébration !")
        
    def walk(self, num_steps=2, turn=0):
        print(f"[MOCK] 🚶 Le faux robot marche : {num_steps} pas, rotation {turn}")

class MartyController:
    # Gère la connexion et les commandes directes au robot Marty
    def __init__(self, method="wifi", address="mock"):
        self.method = method
        self.address = address
        self.connected = False
        self.marty = None  # TODO: Initialiser l'objet martypy.Marty() plus tard

    def connect(self):
        print(f"Tentative de connexion à Marty via {self.method} sur {self.address}...")
        try:
            if self.address == "mock":
                self.marty = MockMarty()
            else:
                self.marty = martypy.Marty(self.method, self.address)
            self.connected = True
            print("Connexion à Marty réussie !")
            return True
        except Exception as e:
            print(f"Erreur de connexion à Marty : {e}")
            self.connected = False
            return False

    def test_mouvement(self):
        if self.connected and self.marty:
            print("Test basique : Marty célèbre !")
            self.marty.celebrate()
        else:
            print("Marty n'est pas connecté. Impossible de tester le mouvement.")

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
        
        self.status_label = QLabel("Statut : Déconnecté")
        layout.addWidget(self.status_label)
        
        self.btn_connect = QPushButton("Connecter Marty")
        self.btn_connect.clicked.connect(self.connect_marty)
        layout.addWidget(self.btn_connect)
        
        self.btn_test = QPushButton("Test : Célébrer")
        self.btn_test.clicked.connect(self.test_marty)
        self.btn_test.setEnabled(False)
        layout.addWidget(self.btn_test)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def connect_marty(self):
        self.status_label.setText("Connexion en cours...")
        
        QApplication.processEvents()  # Force le rafraîchissement de l'UI
        if self.controller.connect():
            self.status_label.setText(f"Statut : Connecté à Marty ({self.controller.method} - {self.controller.address}) !")
            self.btn_test.setEnabled(True)
        else:
            self.status_label.setText("Statut : Échec de la connexion (vérifiez l'adresse et le robot).")

    def test_marty(self):
        self.controller.test_mouvement()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())