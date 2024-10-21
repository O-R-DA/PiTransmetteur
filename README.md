# PiTransmetteur

## Introduction
PiTransmetteur est une application innovante conçue pour simplifier le transfert et l'exécution de fichiers Python entre un ordinateur et un Raspberry Pi. 

## Fonctionnalités principales
- **Transfert de fichiers Python**: PiTransmetteur permet d'envoyer facilement des fichiers Python d'un ordinateur vers un Raspberry Pi.
- **Exécution automatique**: Une fois le fichier transféré, l'application l'exécute automatiquement sur le Raspberry Pi.
- **Interface conviviale**: PiTransmetteur est doté d'une interface utilisateur intuitive qui facilite la gestion des transferts de fichiers.

## Public cible
PiTransmetteur est idéal pour les développeurs Python, les amateurs de Raspberry Pi et les professionnels de l'informatique qui souhaitent automatiser le déploiement et l'exécution de scripts Python sur un Raspberry Pi.

## Avantages
- **Gain de temps**: Élimine le besoin de transférer manuellement des fichiers et d'exécuter des commandes sur le Raspberry Pi.
- **Efficacité**: Automatisation complète du processus de transfert et d'exécution des scripts.
- **Simplicité**: Interface utilisateur intuitive et facile à utiliser.

## Conclusion
PiTransmetteur est un outil qui simplifie le transfert et l'exécution de fichiers Python entre un ordinateur et un Raspberry Pi, rendant ainsi les processus de développement et de déploiement plus efficaces et fluides.

# Configuration de l'Environnement pour PiTransmetteur

## Instructions

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir Python installé.
3. Ouvrez un terminal et naviguez vers l'emplacement du dépôt cloné.
4. Exécutez le script de préparation pour installer les biliothèque nécessaire :
   ```bash
   python setup_env.py

# Mode de fonctionnement

1. Rendez-vous à l'emplacement du dépôt cloné.
2. Double-cliquez sur le fichier exéucutable nommé PiTransmetteur.
   Astuce: Si vous voulez ajouter l'application au menu démarrer faite un clic droit sur le fichier exécutable puis sélectionné Épingler au menu Démarrer.
3. Dans l'app renseigner l'ip, le nom d'utillisateur et le mot de passe ssh de votre raspberry pi. Puis appuyer sur Enregistrer le Profil pour enregistrer les informations
4. Sélectionnez le profil dans le menu déroulant.
5. Appuyez sur Se connecter pour vous connecter au raspberry pi. si le voyant clignote en passant du vert au rouge c'est a dire que le rpi n'est pas connecter a l'inverse si le voyant reste vert c'est à dire que le rpi est connecter.
6. Sélectionner le fichier python que vous voulais executer sur votre rpi en appuyant sur Sélectionner un fichier.
7. Ils ne vous reste plus qu'à appuyer sur Envoyer pour envoyer et exécuter voter script python.

---
