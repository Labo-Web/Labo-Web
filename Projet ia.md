# Document pour labo-web

- Le projet AI a pour ambition de fournir un outil pédagogique et ludique d'initiation au developpement d'intelligence artificiel à l'aide du langage python. Celui est possible autour d'une course automobile. Le but du developpeur est de réaliser une intelligence artificielle à l'aide du langage python en fonction des instructions fournies par la plateforme.

Déroulement d'une partie : Le joueur commence par s'authentifier sur la plateforme. Il peut ensuite accéder à la partie développement qui va lui permettre de développer en python son intelligence artificielle à l'aide des différentes spécifications qui lui sont fournies par la plateforme. Une fois l'ia terminé il a la possibilité de la soummettre et ainsi la tester pour suivre en temps réel l'avancement de sa voiture face à un autre membre du site. 

L'application disponible sur le web s'articule autour de trois parties :

- Le site internet qui permettra à chaque nouvel utilisateur de s'incrire, de s'authentifier afin de developper son intelligence artificielle. La plateforme web comportera aussi un tableau de score des meilleurs IA. 

- La partie conception de l'intelligence artificielle consiste à un champs de texte incluant une coloration synthaxique. Une fois l'intelligence artificielle terminé l'utilisateur aura la possibilité de la soumettre et ainsi affronter un autre utilisateur de la plateforme en temps réel.

- La piste de course est une page web comportant une piste générée automatiquement d'une taille de 800*600. Les voitures se déplacent à la vitesse de 20 frames par seconde et doivent parcourir le parcour le plus rapidement possible. 


Spécications techniques : 

- La plateforme web est développer intégralement en NodeJS avec une base de donnée mongodb.
- L'affichage de la carte ainsi que des voitures sont affichées en HTML5/JS à travers un canvas.
- La gestion de l'interprétation de l'intelligence artificiel est développer à l'aide du langage python. 