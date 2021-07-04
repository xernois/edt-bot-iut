# UNILIBOT
## Bot Discord et API
### par 
### BAURI Antoine | DRON Jérémy | RATEL Alexandre
### Etudiants en DUT informatique à l'IUT du Limousin (2020 - 2021)
*Le projet tuteuré étant terminné, certains liens ne sont plus accessible*

# Sommaire  <a id="sommaire"></a> 
- [I.Prérequis et configuration](#I)
- [1.1 - Le materiel hardware](#I1)
- [1.2 - Installation du systeme d'exploitation et configuration SSH](#I2)
- [1.3 - Installation de python et tests](#I3)
- [II.Conception du projet](#II)
- [2.1 - Présentation du projet](#II1)
- [2.2 - Récuperation des EDTs](#II2)
- [2.3 - Conversion des EDTs et json](#II3)
- [2.4 - Mise en place de l'API](#II4)
- [III.Utilisation de l'API](#III)
- [3.1 - Bot Discord](#III1)
- [3.2 - Page web](#III2)
- [3.3 - Application desktop en python](#III3)
- [Conslusion](#Conclusion)
- [Glossaire](#Glossaire)
- [Bibliographie](#Biblio)

# I.Prérequis et configuration <a id="I"></a> 
## 1.1 - Le matériel hardware <a id="I1"></a> 
Afin de préparer le terrain pour notre future [projet tuteuré](#II), nous avons à disposition divers matériels et cables, prêté par l'université.

![figure 1: Le materiel](https://github.com/xernois/edt-bot-iut/blob/master/images-RM/fig1.png)

Le composant principal est le Raspberry Pi. Un micro-ordinateur condensé en une seule et unique carte, non plus grande qu’une carte à jouer. Le Raspberry Pi est très accessible par son prix, bien moins chère qu’un ordinateur classique. Il permet de créer divers système à moindre coût. Il est possible d’ajouter des composants supplémentaires au micro-ordinateur. Depuis ses débuts, il y a eu plusieurs versions de Raspberry Pi : Pi 2, Pi 3, Pi Zero, Pi 4, et plus récemment le Raspberry Pi 400 inclut dans un clavier et vendu comme un vrai ordinateur.

![figure 2: Raspberry Pi 400](https://github.com/xernois/edt-bot-iut/blob/master/images-RM/fig2.jpg)

Le Raspberry Pi étant un micro-ordinateur, il nécessite l’installation d’un système d’exploitation. Le choix du système est libre : Pidora, Arch linux, Debian ou encore Windows 10 IOT. Dans notre cas, nous utiliserons le système d’exploitation Raspberry Pi OS anciennement Raspbian.

![figure 3: Bureau Raspberry Pi OS](https://github.com/xernois/edt-bot-iut/blob/master/images-RM/fig3.jpg)


##### [Retour au sommaire](#sommaire)
## 1.2 - Installation du systeme d'exploitation et configuration SSH <a id="I2"></a> 

Pour l’installation, notre équipe c’est rejoint à l’IUT. Cette étape commence par télécharger le système d’exploitation et de l’installer sur une carte SD, nous servant de mémoire. La carte SD fait 8go, ce qui est très convenable pour l’utilisation que nous allons en faire. Le logiciel Raspberry Pi Imager nous a permis d’installer le système sur notre carte SD.


![figure 4: Interface Raspberry PI Imager](https://github.com/xernois/edt-bot-iut/blob/master/images-RM/fig4.jpg)

Cette phase d’installation faite, nous avons connecté le Raspberry Pi à un moniteur branché en HDMI, et nous avons lancé la machine.

![figure 5: Démarrage du micro-ordinateur](https://github.com/xernois/edt-bot-iut/blob/master/images-RM/fig5.jpg)

Quelques paramétrages étaient nécessaires comme changer la reconnaissance du clavier. Notre clavier français dit « AZERTY » était reconnu par défaut comme un clavier américain dit « QWERTY ».

Nous devions prendre par la suite le Raspberry Pi à distance. Pour se faire nous avons utilisé un programme informatique et protocole de communication sécurisé. C’est le Secure Shell ou SSH. Nous récupérons l’adresse IP local du Raspberry Pi, que nous avons saisi depuis une autre machine connecté sur le même réseau.

![figure 6: Prise du Raspberry PI à distance via le SSH](https://github.com/xernois/edt-bot-iut/blob/master/images-RM/fig6.jpg)

Durant l’installation nous nous sommes confrontés à deux problèmes. Tout d’abord pour connecter notre micro-ordinateur au moniteur, nous avions utilisé un câble VGA qui visiblement n’était pas compatible avec notre machine. Le second problème, a été la configuration du SSH. Nous avons pris de longue minutes avant de comprendre pourquoi le Raspberry nous refusait la connexion. La machine nous ressortait un message d’erreur nous refusant l’accès. Finalement, il suffisait d’autoriser le SSH dans les paramètres du système d’exploitation du Raspberry Pi

![figure 7: Message d'erreur pour le refus de la prise en SSH](https://github.com/xernois/edt-bot-iut/blob/master/images-RM/fig7.jpg)

##### [Retour au sommaire](#sommaire)
## 1.3 - Installation de python et tests <a id="I3"></a> 

Après vérification les versions python 3 et python 2 étaient préalablement installé avec le système d’exploitation. De plus, Geany, l’éditeur par défaut que propose Raspberry Pi OS, était préalablement installé, cependant nous allons utiliser le Raspberry qu'en SSH, nous utiliserons donc le shell.

Afin de vérifier si tout fonctionne correctement, nous avons utilisé un programme archive qu’un des membres du groupe a fait il y a quelques années. Le programme chiffre un message avec la méthode de [Vigenère](#Glossaire)

![figure 8: Capture d'écran du programme de chiffrement de Vigenère](https://github.com/xernois/edt-bot-iut/blob/master/images-RM/fig8.jpg)

Pour continuer, nous avons développé un petit jeu plutôt connu. Le jeu du plus ou moins. Dans notre programme l’utilisateur joue contre l’ordinateur en essayant de trouver le nombre secret auquel pense l’ordinateur. Le nombre en question est compris dans l’intervalle que saisi l’utilisateur. À chaque fois, l’utilisateur propose un nombre et l’ordinateur lui indique si le nombre secret est inférieur ou supérieur. Le nombre de question pour trouver l’inconnu est défini par l’utilisateur dans le menu avec le choix *option*. Le jeu est entièrement paramétrable.

##### [Retour au sommaire](#sommaire)

# II.Conception du projet <a id="II"></a>
## 2.1 - Présentation du projet <a id="II1"></a>
Une fois le Raspberry prêt à l’emploi, notre groupe est passé en phase deux du projet tuteuré. Dans
cette seconde étape, nous devions faire le choix d’un projet permettant de mettre en avant la praticité et
l’utilité d’un Raspberry. Pour ce faire, après une réunion, nous avons décidé de faire un bot Discord qui
notifie les utilisateurs du prochain cours.

Pour mener à bien le projet nous nous sommes organisés et hiérarchisé en deux équipes, Team API
et Team bot, coordonnées par le chef de projet, dans notre cas Jérémy a assuré ce rôle. Afin de mieux
distribuer le travail, la Team API a subdivisé leur travail, pour obtenir finalement : la récupération de l’emploi
du temps (abrégé par EDT régulièrement dans ce dossier), le convertisseur d’EDT en JSON et l’API en ellemême.
La partie « Récupération de l’EDT » va permettre de récupérer l’EDT puis de le transformer du format
PDF en JPEG afin de finalement l’envoyer au convertisseur.

La partie « Convertisseur EDT en JSON » va permettre de transformer le format JPEG en un format
JSON qui est un format standard compris par de nombreux langages de programmation.
La partie « API » va permettre de proposer aux développeurs voulant acquérir les informations de
l’EDT de juste exécuter une requête pour obtenir ce qu’ils veulent.
Par la suite, nous avons voulu montrer que l’API était indépendante du bot et que tout le monde
pouvait la requêter, nous avons décidé d'élaborer 2 projets annexes, un site web et une application de
bureau.

Ce projet étant d’une certaine envergure, une organisation précise était nécessaire pour mener à son
terme le projet. Tout d’abord, nous avons utilisé le gestionnaire de versions github. Dans ce gestionnaire,
nous avons déployé une branche par division du projet. Pour conserver une trace de ce travail et permettant
de saisir le sujet, nous avons commencé également à alimenter le Readme. Le fait d’utiliser un gestionnaire
de versions nous a permis de décentraliser le projet afin que tous les membres du groupe y aient l'accès.
Une organisation efficace du projet passe également sur une connaissance exacte des tâches a
réalisé, par qui et en combien de temps. Le chef de projet a ainsi élaboré un tableau des tâches à effectuer
et un diagramme de PERT

Tout bien considéré, notre projet va permettre de montrer l’utilité et les possibilités d’un Raspberry,
car notre bot Discord doit pouvoir fonctionner en permanence. Pour ce faire, il faut qu’il soit installé sur une
machine qui fonctionne continuellement. Un ordinateur classique ne demeure pas une solution adéquate
sachant que l’utilisateur peut malencontreusement éteindre le programme ou l’ordinateur. Notre API est
également installée sur le Raspberry pour les mêmes raisons que le bot Discord. Quant aux projets annexes,
ils ne sont pas déployés dessus, car dans le cas de l’application de bureau, elle représente un logiciel installé
sur l’ordinateur d’un client. La page web sera déployé temporairement sur
https://siteedt.000webhostapp.com/ pour coller au plus à la réalité. Le but est de montrer qu’un site web
externe puisse requêter notre API. Si la page web était sur le Raspberry, nous ne pourrions pas rendre
compte, réellement, de ce phénomène en sachant qu’ils ont la même IP.

##### [Retour au sommaire](#sommaire)
## 2.2 - Récuperation des EDTs <a id="II2"></a>

Dans cette partie, nous observerons l’étape de pré-traitement de l’emploi du temps, du
programme. Le projet tuteuré contient plusieurs mécanismes essentiels, comme dit précédemment, dans
un premier temps, avant même de commencer quoi que ce soit, il nous faut obtenir la liste des EDT qui est
disponible sur le site de l’IUT du Limousin edt-iut-info. unilim.fr.

Pour ce faire, nous avons commencé avec une première librairie python appelé sélénium qui permet
de contrôler un navigateur internet depuis un programme externe. Les résultats étaient convainquant et
prometteur. Cependant, avec le nombre d’emplois du temps à récupérer et le nombre de données que cela
implique, nous en avons rapidement atteint certaines limites qui nous ont posés problème. Ces limites
étaient liées au temps de traitement. Premièrement, le temps de récupération des emplois du temps était
trop long, et deuxièmement lancer le navigateur prenait également des ressources et du temps. En effet, la
librairie sélénium ouvrait un navigateur internet à chaque fois que l’on souhaitait récupérer un fichier. Pour
pallier ces problèmes, il n’y avait pas d’autres solutions que de trouver une alternative à sélénium. La librairie
python requests a été le dénouement de nos problèmes. Elle permet de faire comme nos navigateurs
internet, c’est-à-dire envoyer une requête à un serveur contenant la page que l’on souhaite, afin d’en
récupérer le contenu.

À présent, nous avons récupéré le contenue du site avec la liste des emplois du temps des différentes
promotions de l’IUT du Limousin, et plus particulièrement du département informatique. Nous avons
navigué avec ces données exactement comme un humain aurait pu le faire.

Dès que nous arrivons sur le site edt-iut-info.unilim.fr, nous sommes positionnés au niveau de la liste
des différentes promotions puis grâce à cette liste, on peut accéder à leur page. Finalement, dans ces sousdossiers, se trouvent les EDT. Notre programme va parcourir les différentes promotions des premières
années aux licences professionnelles. Dans chaque dossier, nous faisons récupérer au programme les
emplois du temps.

Le traitement de l’enregistrement des emplois du temps se passe en deux étapes. La première
consiste à vérifier si nous possédons déjà ou non l’emploi du temps en question. Pour ce faire nous
recherchons dans le dossier du Raspberry où est enregistré les fichiers s’il existe. Dans ce cas, nous passons
à la deuxième étape sinon nous le téléchargeons.

La deuxième étape du traitement consiste à vérifier, si le fichier existant est la dernière mis à jour de
l’emploi du temps ou non. En effet, l’EDT peut changer au cours de la semaine dans ce cas, il faut remplacer
l’EDT qu’a enregistré notre programme précédemment par le nouveau. Pour ce faire nous consultonsla date
de sortie des fichiers, accessibles directement sur le site et celle des fichiers du Raspberry. Si les dates sont
identiques alors nous ne téléchargeons pas l’emploi du temps. Dans le cas contraire, nous lançons le
téléchargement. Nous renouvelons l’opération jusqu’à obtenir tous les emplois du temps, de toutes les
promotions à jour.

La fonction permettant de télécharger les emplois du temps ne lestélécharge pas réellement en PDF.
Elle réutilise la librairie requests, vu précédemment, afin de récupérer le contenue du PDF que l’on converti
en image de type PNG. Par la suite, c’est cette version de l’emploi du temps que l’on stock, parce que le
convertisseur permettant d’analyser les EDT ne supporte que les fichiers image.
Toutes ces étapes se trouvent dans une boucle qui se répète toutes les deux heures afin d’avoir le
temps de télécharger et traiter complètement plusieurs emplois du temps en cas de besoin. De plus, les
emplois du temps ne sont pas forcément disponibles, le même jour, à la même heure selon les semaines. Le
programme, mis à part les librairies est entièrement indépendant.

##### [Retour au sommaire](#sommaire)
## 2.3 - Conversion des EDTs et json <a id="II3"></a>

Pour pouvoir notifier les utilisateurs du Discord de leurs prochains cours, TD ou TP, il faut que le bot
comprenne ce qu’il y a écrit sur l’emploi du temps. Seulement, un PDF ou une image au format JPEG n’est
pas très parlant pour lui. Nous devions par la suite trouver une solution pour faire comprendre au bot les
informations de l’emploi du temps. Un format très pratique pour transporter des informations est le format
JSON. Il prend la forme d’une structure de données, ou d’un dictionnaire en python, ce qui le rend pratique
et rapide de lecture et écriture. Nous devions alors développer un convertisseur de PDF en JSON pour les
emplois du temps. Pour cela, nous avons fait le choix du python. Le JSON devait contenir le type de cours
(CM, TD ou TP) et le nom du module pour chaque groupe de TP.

Pour le moteur de notre convertisseur, il y avait plusieurs solutions, comme utiliser une librairie qui
transforme un PDF en XML un format proche du JSON. Le problème de cette méthode, c’est que XML en
sortit n’était pas très compréhensible et plutôt hasardeux.
Nous avons opté pour une autre méthode orientée colorimétrie. La solution pour identifier les types
de cours est de reconnaître la couleur de chaque cours, c’est-à-dire, bleu pour les TP, jaune pour les CM, etc.
Pour pouvoir accomplir ce travail une librairie python était très pratique, c’est la librairie PIL. Mais cette
dernière, nécessite un fichier d’entrée au format JPEG. C’est pour quoi dans la partie précédente, nous avons
fait le choix de sortir un fichier en JPEG quand nous récupérions l’EDT. Notre schéma de fonctionnement est
donc légèrement modifié.

La conversion de l’emploi du temps de PDF en JPEG, se faisant lors de la récupération de l’emploi du
temps, notre convertisseur ne s’occupera ainsi pas d'accomplir ce travail.
En premier lieu, le convertisseur doit savoir à quelle promotion appartient l’EDT passé en entrée.
L’information est contenue dans le nom du fichier. De là, le programme va appeler la fonction engine et lui
passer en paramètre le JPEG de l’emploi du temps et le niveau associé.
La fonction engine va tout d’abord préparer le terrain, pour lancer le traitement, en ouvrant l’image
et en créant la base des dictionnaires, c’est-à-dire des structures de données, du niveau des étudiants. Une
fois le travail préparatoire fait, le programme s’engage dans le traitement de l’EDT en passant dans une
première boucle for, qui va s’occuper de chaque groupe de TP un par un. Le programme rentre dans une
seconde boucle for qui s’occupe de chaque demi-heure de l’EDT. Pour chaque groupe de TP, à chaque demiheure, le programme va créer 5 pipettes qui détectent la couleur.

Une fois les pipettes créées, le convertisseur va essayer de trouver à quelle couleur cela correspond.
Pour ce faire, il passe dans la fonction getColor. Cette fonction prend en paramètre d’entrée toutes les
pipettes et va comparer leurs valeurs sur un intervalle de couleur. Si une couleur pipée correspond à un
intervalle défini, la couleur est fixée. Pour savoir si la couleur est dans l’intervalle, il a fallu réaliser une
fonction que nous avons appelé intervalleCouleur. La difficulté, ici, c’est d’avoir un intervalle de couleur assez
large pour considérer toutes les valeurs de couleurs, mais pas trop large non plus pour ne pas créer
d’intersection entre les ensembles de couleurs.

Quand la couleur est reconnue, la fonction renvoie au programme principal le type de couleur en
types chaîne de caractère : « Rose », « bleu », « jaune », etc. À présent, le programme n’a plus qu’à associer
la couleur au type de cours puis à l’ajouter au bon endroit dans le dictionnaire.
Quand le type de couleur est trouvé, le système doit à partir de maintenant chercher le numéro du
module. Pour cela, il va découper l’emploi du temps dans la demi-heure où il se trouve et va analyser
l’écriture qu’il y a sur l’image. Pour ce faire, nous utilisons la technologie de la Reconnaissance Optique de
Caractère, dit OCR. Cette technologie permet de reconnaître des mots, des lettres ou encore des chiffres
dans une image. La libraire pytesseract permet de faire de l’OCR. Avant de lancer l’analyse de l’image, nous
la passons en noir et blanc, car nous obtenons de meilleurs résultats.

L’analyse n’étant pas parfaite, notre convertisseur admet alors une marge d’erreur. Nous avons
estimé que les erreurs représentaient en moyenne 3 à 5 % des 720 résultats. Les erreurs peuvent être un
cours qui n’est pas reconnu ou un module mal rédigé.

Toutes ces étapes vont être répétées pour traiter toutes les demi-heures de chaque groupe de TP
tous les jours. À la fin, le dictionnaire complet de toutes les données est envoyé dans une fonction qui va
écrire jusqu’à 3 470 lignes dans le fichier JSON. Le temps de traitement va varier en fonction de l’année à qui
appartient l’emploi du temps. Cette différence s’explique, car il y a moins de groupes de TP en troisième
année qu’en première année, ce qui implique un nombre de pipette moins grand et des analyses OCR moins
nombreuses.

Le développement de ce convertisseur a été une tache fastidieuse pour laquelle nous avons
rencontré beaucoup de difficulté entre la mise en place de l’OCR, de la gestion des intersections des couleurs
ou encore le positionnement des pipettes, sans compter un algorithmie complexe.
Comment fonctionne la librairie pytesseract et la technologie d’OCR ?
Avant d’implémenter dans notre code, la librairie permettant d'identifier le numéro des modules,
nous avons souhaité en savoir plus sur le fonctionnement de l’OCR. Cette technologie se réalise en quatre
étapes distinctes. Tout d’abord, l’étape de la préanalyse, cette étape consiste à améliorer la qualité d’image
et à la redresser afin de pouvoir déchiffrer au mieux son contenu. La deuxième étape consiste à isoler l’image
de chaque ligne de texte, c’est la segmentation. La reconnaissance se fait qu’à l’étape 3. Dans cette étape,
le programme va comparer le trait et forme à une large base de données. Finalement, le post-traitement
apparaît en quatrièmes et dernières étapes. Cette phase consiste à appliquer des règles au traitement de
l’étape précédente. Ces règles sont des règles linguistiques basées sur une base syllabique.

##### [Retour au sommaire](#sommaire)
## 2.4 - Mise en place de l'API <a id="II4"></a>

Après avoir fait un système aussi complexe, nous avons fait le choix de le rendre accessible à tous les
développeurs et programme le souhaitant. Dans cette optique, une API est de bon augure. Les programmes
voulant récupérer les données n’ont qu’à effectuer des requêtes HTTP avec des paramètres. Ce modèle d’API
est très pratique, car nous possédons tous sur nos ordinateurs ou nos smartphones un navigateur internet
qui sait interpréter ces requêtes. En effet, le navigateur internet est, à dire vrai, un logiciel qui passe son
temps à faire des requêtes, on peut par conséquent très aisément tester notre API via un navigateur internet.

Il nous a fallu faire un service qui écoutait continuellement si une requête était effectuée. Pour ce
faire, nous avons fait le choix d’utiliser la librairie python Flask qui nous permet de créer une application qui
va justement écouter les requêtes et appeler des fonctions différentes selon les requêtes.
Dans le code de ce service, se trouve une liste de route correspondante à des requêtes différentes.
On y trouve entre autres une route pour chaque promotion, mais également une route pour accéder à la
documentation de notre API. Nous avons le choix de retourner un fichier au format JSON ou une page web.
Le service admet une dernière route un plus spécifique, celle-ci correspond à toutes les routes nonexistantes afin de rediriger les utilisateurs vers la documentation de l’API. 

Ces routes correspondent à des méthodes, il existe plein, mais dans le cadre du projet nous utilisons
la méthode « GET ». Cette méthode permet à l’utilisateur de récupérer des données. Lorsque ces routes,
sont « empruntées » elle déclenche une fonction qui va retourner des données différentes selon les
paramètres de la requête.

Une fois toutes ces routes et fonctions créées, nous pouvons lancer ce service qui écoute sur le port
80, qui est une sorte de porte au niveau de la machine. Le port 80 étant réservé pour de l’HTTP pile ce qu’il
nous faut puisque nos requêtes utilisent le protocole HTTP.

De nos jours, une API est très utile pour faire de nombreux programmes, mais encore faut-il savoir
s’en servir. Certaines sont plus ou moins difficiles d’utilisations, afin d’aider les développeurs qui souhaitent
l’utiliser, le plus souvent, une documentation leur est mis à disposition. Pour aider, les éventuels
programmeurs qui envisagent d’utiliser notre API nommé uniliBOT, nous leur avons préparé une
documentation claire. Cette documentation est programmée en HTML 5 et CSS 3. Néanmoins, avant de
programmer quoi que ce soit, nous avons élaboré une maquette.

Dans le souci d’une cohérence graphique, là aussi, nous avons repris une partie de la charte graphique
de www.unilim.fr. Après cette étape de maquettage, nous avons programmé la page en scindant le code
HTML et CSS sur deux fichiers différents. Une fois développées, nous avons déployé le site sur le Raspberry.
À présent, la documentation est accessible à cette adresse :http://109.220.5.61/doc

##### [Retour au sommaire](#sommaire)

# III.Utilisation de l'API <a id="III"></a>
## 3.1 - Bot Discord <a id="III1"></a>

Dans cette partie, nous aborderons le bot Discord. Contrairement, au reste du projet, le bot a été
développé en JavaScript. Le choix, ici, est plutôt celui du développeur, Alexandre, car l’utilisation du langage
python était possible également. La décision a cependant été cornélienne puisque pour JavaScript, la
documentation de l’API Discord était plus lisible et documentée par rapport à celle de python, cependant
python représente un langage simple d’apprentissage et d’implémentation. Finalement, notre choix, c’est
porté sur le JavaScript. Utiliser ce langage pour faire un bot Discord, cela implique l’utilisation de node.js qui
est selon l’organisation officiel de node.js : « Un environnement d’exécution JavaScript asynchrone et
orienté événement ».
Un bot Discord est un programme interagissant avec Discord, un réseau social, initialement utilisé
pour les joueurs en ligne, par le biais d’une API de manière automatisée. Un bot est un client qui sert à
interagir avec un serveur. Le client, qu’est le bot Discord, peut être utilisé afin de modérer les propos tenus
par d’autres clients, par le biais de permissions. Le bot peut également gérer les salons de discussion, ou
encore d’interagir avec d’autres clients qui peuvent, eux, être des utilisateurs réels.
La création d’un bot Discord peu importe le langage commence par se rendre sur la page que dédie
Discord aux développeurs via le lien ci-après : https://Discord.com/developers/applications. Depuis cette
page, il est possible de créer une nouvelle application.

De là, nous lui ajoutons un nom via le menu OAUTH2. Une fois ces quelques paramétrages effectués.
Le site nous renvoie vers une page sur laquelle nous récupérons des informations essentielles pour le
fonctionnement du bot. Ces informations peuvent être dite « sensible » comme le token d’identification.
Sans ce dernier, nous ne pourrions pas nous connecter au compte du bot et ainsi le contrôler. Il est capital
de garder un token secret, et si un autre utilisateur l’obtenait, alors il pourrait prendre le contrôle du bot et
détourner son utilisation. Il est à garder précieusement et il va donc de soit de limiter le nombre de
personnes à qui vous le donnez. Si le cas venait a arrivé, Discord nous propose une option pour le régénérer.
Cette étape de configurations terminées, nous allons nous attarder sur le fonctionnement des
fonctions de Discord. Dans le cadre du Projet Tuteuré, le bot adoptera deux comportements :
- Envoyer un message dans un salon automatiquement. Dans ce cas, il est presque nécessaire de
passer par le second comportement. En effet, si un problème survient, l’administrateur du
serveur sera obligé d’interagir avec le bot, car si le salon dans lequel le bot essaie de délivrer un
message est supprimé ou modifié, alors le bot ne répondra plus du tout. Pareillement, il pourrait
être ainsi, intéressant d’ajouter des interactions entre l’utilisateur et la machine.
- Répondre à un message. Dans le premier cas, il est nécessaire, quasiment inévitable de passer
par le second cas.

Pour que, les utilisateurs et administrateur d’un serveur Discord puissent interagir avec le bot, une
fonction Discord admet un schéma spécifique.
- Un identificateur [Essentiel] : cet élément est un caractère, souvent « ! », ou un préfixe
permettant de se différencier du flot de messages. L’identificateur est généralement aussi appelé
préfixe ou tag. Le choix de ce dernier est au libre-arbitre du développeur.
- La commande [Essentiel] : cet élément va permettre de définir un accord entre l’utilisateur et le
bot de quelle action doit être fait. La commande est précédée de l’identificateur.
- Les arguments [Optionnel] : le ou les argument(s) permett(ent) de compléter des commandes si
la fonction est complexe.

Le bot n’est pas portable à d’autres serveurs, car les informations indispensables de ce dernier son
contenu dans un fichier JSON propre au serveur. Son exportation sans maintenance pourrait aboutir à des
conflits.
Avec la commande set et l’avancement des semaines, le bot doit pouvoir s’y retrouver entre les
salons, l’identificateur et les semaines qui s’écoulent. C’est là, qu’intervient, le fichier de configuration du
serveur, ce fichier est un JSON très pratique comme nous l’avons vu depuis le début pour contenir des
informations.
Durant le développement du bot, nous avons été face à de nombreuses difficultés : gestion
asynchrone du bot (gain en performance), gestion de l’arborescence du bot et compréhension approfondie
du fonctionnement de Discord. Cependant, nous avons appris certaines connaissances comme : le langage
JavaScript, la programmation synchrone et asynchrone et les objets globaux (modules, export, dirname ou
encore filename).


##### [Retour au sommaire](#sommaire)
## 3.2 - Page web <a id="III2"></a>

Afin de montrer que notre API en est effectivement une, et non-juste une partie du programme du
bot Discord. Nous avons choisi de développer deux projets annexes qui montreraient que l’API est disponible
pour tous. Nous avons développé une page web et une application de bureau2 avec une interface humainmachine. La page web est programmé en HTML 5 et CSS pour le frontend et en JavaScript pour le backend.
Nonobstant, avant de commencer à coder, nous avons conçu une maquette. La charte graphique utilisée
pour le site web est similaire à celle de www.unilim.fr. Pour pouvoir utiliser cette charte graphique, nous
nous sommes renseignés auprès du service support aux usagers du département.

Cette étape faites nous nous sommes penchés sur le développement du site. Tout d’abord avec la
partie frontend, puis le backend. Lors du développement du backend nous nous sommes confrontés à une
erreur durant la requête.

L’erreur retournée ici est de type CORS policy. Elle survient lorsqu’une source extérieure à
l’application essai d'émettre une requête. Cette erreur est en fait une fonctionnalité permettant de gérer les
droits de requêtes et ainsi éviter les intrusions malveillantes. Il nous a juste fallu autoriser les requêtes depuis
l’extérieur. Le problème ayant persisté durablement, il nous ralentissait. Par conséquent, nous avons installé
une extension de navigateur qui nous a permis de reprendre le développement et de corriger l’erreur un
peu plus tard.

Ce projet annexe, de site web, au projet principal permet de montrer que l’API est bel et bien
fonctionnelle, accessible à tous. Ils nous a permis de découvrir ce qu’était le CORS et de corriger les droits
de requête. Le site est temporairement accessible dans le cadre du projet tuteuré à l’adresse suivante
https://siteedt.000webhostapp.com/. 

##### [Retour au sommaire](#sommaire)
## 3.3 - Application desktop en python <a id="III3"></a>

Afin de montrer de nouveau que notre API en est bien une. Nous avons choisi de développer deux
projets annexes qui permettent de montrer que l’API est disponible pour tous. Nous avons développé une
page web, vu dans la partie précédente, et nous avons fait le choix de développer une application de bureau
avec une interface humain-machine. Nous avons choisi une fois de plus le langage python pour développer
l’application.
Avant même de commencer le code, nous avons composé une maquette de l’application pour
connaître les différents composants et leur position. Pour conserver une certaine cohérence, la charte
graphique de l’application reprend celle du site de l’université, www.unilim.fr.

La maquette faite, nous avons pu commencer la programmation. Pour la clarté du code et sa modularité,
nous avons conçu notre code sur 3 couches logicielles distinctes basé sur le modèle MVC :
- La couche présentation : l’interface visuelle que voit l’utilisateur
- La couche application : la partie logique de l’application
- La couche de données : manipulation des données et transfère entre le fichier source et la couche
application
Ces trois couches logicielles sont représentées généralement par les symboles comme dans la figure. Ces 3 symboles sont associés aux stéréotypes de Jacobson utilisés en UML.

Tout d’abord, nous avons développé la partie graphique en plaçant les labels et bouton. Puis nous avons
programmé l’interaction qu’avait le bouton. La difficulté était de gérer les erreurs éventuelles et de les 
signaler à l’utilisateur le plus clairement possible. Une fois l’API en place, nous avons modifié légèrement le
code qui permettait jusqu’à lors de lire un fichier se trouvant dans le dossier pour qu’il puisse réaliser des
requêtes vers l’API. Pour effectuer, ces requêtes la librairie requests en python convenait parfaitement.

Finalement, dans sa version finale l’application bureau ressemble à la figure (cf. figure 39). De plus, nous
constatons que les cours d’application et de l’emploi du temps de la semaine 27, le mardi pour les G1B
correspondent.

Ce projet annexe au projet principal permet de montrer que l’API est bel et bien fonctionnelle et
accessible à tous.
##### [Retour au sommaire](#sommaire)

# Conclusion <a id="Conclusion"></a>
En conclusion, le projet tuteuré de notre deuxième semestre de DUT informatique à l’IUT du
Limousin, a représenté un travail sur le long terme qui a requis une organisation en amont. Notre projet
étant conséquent, nous avons fait le choix de le scinder en sous-projet en divisant également le groupe en
deux équipes, c’est-à-dire Team Bot et Team API. Pour l’API, nous avons développé un programme
permettant de récupérer les emplois du temps, puis un convertisseur d’EDT en JSON, et finalement l’API en
elle-même afin de rendre l’emploi du temps en JSON accessible à tous. Quant au bot, nous lui avons intégré
de nombreuses fonctionnalités permettant de simplifier la création d’un Discord adapté au bot et d’interagir
pour être informé des cours prochains. Pour accentuer le fait que l’API en est réellement une, nous avons
réalisé deux projets annexes. Ce sont deux projets qui illustrent des cas d’utilisations réelles que peut
concevoir des développeurs qui auraient besoin de notre API. Ces projets annexes sont un site web et une
application de bureau. L’ensemble du projet tuteuré équivaut à plus de 2300 lignes de codes et des dizaines
d’heures de développement.
Ce projet nous a apportées de nouvelles connaissances dans les différentes technologies utilisé, que
ce soit en python, JavaScript ou encore l’OCR. Ce travail nous a permis d’apprendre à s’organiser pour un
projet de groupe et également dans le code. Cependant, le projet admet certaines failles comme un retard
dans les tâches liées au développement, des erreurs dans le convertisseur d’EDT en JSON ou encore le temps
de traitement des emplois du temps. Ces failles peuvent être comblées et corrigées dans le futur, cependant
ces problèmes n'entravent pas le fonctionnement correct des éléments entre eux, donc le bon
fonctionnement du projet global.
Notre projet démontre les capacités d’un Raspberry pi, et n’est qu’une ébauche de l’entièreté de ces
aptitudes. Il peut être complété par de nouvelles fonctionnalités sur le bot ou encore un programme qui
génèrent un emploi du temps en PNG par groupe, comme sur le site edt-iut-info.unilim.fr.

##### [Retour au sommaire](#sommaire)
# Glossaire <a id="Glossaire"></a>

Discord
Terme | Définition
------------ | -------------
Client | Le client Discord désigne généralement un bot, parfois un utilisateur interagissant avec Discord.
Tag | Le tag est une combinaison du nom de l’utilisateur et son discriminant. Il permet la mention d’un client en général.
Token | Un token est une clé unique permettant d’identifier chaque utilisateur sur la plateforme afin de pouvoir prendre contrôle du compte.

Technique et metier
Terme | Définition
------------ | -------------
API - Application Programming Interface |  L’API est un programme informatique qui vient faire l’interface,un pont entre deux programmes. Le programme client effectué des requêtes sur l’API qui lui renvoi des données récupéré sur une application servant de moteur. Une API permet aux développeurs d'obtenir l’accès à des fonctionnalités et données qui leur sont inaccessible.
Backend | Le backend est la partie fonctionnelle d’un site web.
Bot | Le bot est un programme informatique qui fonctionne automatiquement. Son comportement étant similaire à un robot, il extrait donc son nom du mot « robot » tronqué. 
Frontend | Le frontend est la partie visible d’un site web.
JSON |Le JSON est un format de fichier permettant de stocker des données sous forme de structure de données. C’est un standard dans l’échange de données et est similaire au XML.
Librairie informatique | Une librairie informatique ou bibliothèque est un ensemble, une collection de fonctions généralement d’un niveau complexe, utilisable dans un programme afin de simplifier son développement.
MVC - Modele Vue Controleur | Le MVC est une architecture logicielle destiné à la création d’interface graphique conçu en 1978.
PDF - Portable Document Format |  Le PDF est un format fichier informatique, développé par Adobe.
PNG - Portable Network Graphics | Le PNG est un format informatique d’image permettant de gérer les couches alpha et animations.
Serveur | Un serveur est une machine, le plus souvent distante, permettant l’exécution de service de manière continue
Shell |Le Shell est un programme informatique permettant d'obtenir des commandes systèmes par le biais de l’utilisateur à partir de l’entrée standard, connecté à un périphérique, le clavier, afin de les faire exécuter.
Système d’exploitation | Le système d’exploitation ou SE ou OS est un ensemble de programmes qui font fonctionner une machine. Le système admet 3 composantes : un noyau (kernel), un interpréteur de commande (Shell) et un système de fichiers (file system).
UML - Langage de Modelisation Unifié | UML – Langage de Modélisation Unifié : L’UML est un langage de modélisation normalisé, utilisé dans la conception de logicielle utilisant des symboles graphiques. 

##### [Retour au sommaire](#sommaire)

# Bibliographie  <a id="Biblio"></a>
[Secure Shell. (2020). In Wikipédia.](https://fr.wikipedia.org/w/index.php?title=Secure_Shell&oldid=175558618)

[Raspberry Pi. (2021). In Wikipédia.](https://fr.wikipedia.org/w/index.php?title=Raspberry_Pi&oldid=180363147)

[Reconnaissance optique de caractères. (2021). In Wikipédia.](https://fr.wikipedia.org/w/index.php?title=Reconnaissance_optique_de_caract%C3%A8res&oldid=180608413)

[Ivar Jacobson. (2020). In Wikipédia.](https://fr.wikipedia.org/w/index.php?title=Ivar_Jacobson&oldid=166908730)

[UML (informatique). (2021). In Wikipédia.](https://fr.wikipedia.org/w/index.php?title=UML_(informatique)&oldid=179459791)

[Modèle-vue-contrôleur. (2021). In Wikipédia](https://fr.wikipedia.org/w/index.php?title=Mod%C3%A8le-vue-contr%C3%B4leur&oldid=180227976)
##### [Retour au sommaire](#sommaire)
