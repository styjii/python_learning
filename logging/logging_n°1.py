import logging

logging.basicConfig(level=logging.DEBUG,
                    # écrire à l'itérieur d'un fichier log
                    filename="app.log", # chemin de la fichier
                    filemode="w", # mode de l'écriture : w ou a
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug("Le script a bien été exécutée.")
logging.info("Message d'information général.")
logging.warning("Attention !")
logging.error("Une erreur est arrivée.")
logging.critical("Erreur critique.")
