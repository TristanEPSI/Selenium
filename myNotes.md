# Projet Sélénium

Nous avons décidé de travailler avec Sélénium pour chrome.

## IDE Sélénium Browser extensions

  Sélénium IDE consiste en une extension permettant de créer un pattern / chemin que l'on suhaite faire tester sur un site. Depuis celui-ci il est possible de tester des inputs, réaliser un chemin, tester des "issus"

  Dans notre cas, nous avons testé le site suivant : http://testphp.vulnweb.com/login.php

  Notre chemin a été assez simple : 

  1) tester un un mot de passe qui n'était pas le bon
  2) tester avec un bon mot de passe
  3) Tester une inscription
  4) Se connecter avec notre récente inscription


  ## Sélénium framework

  Sélénium framework utilise en complément des drivers spécialisés selon le navigateur utilisé. ici nosu utilisons Chrome. Nous avons donc télécharger le chromedriver.exe correspondant et l'avons placé pour ce test dans le même dossier parent que notre configuration.

  Une fois l'installation faite, nous avons créé un ficher 'config_selenium' dans lequel nous avons importé sélénium.

  Après cela nous avons défini notre nom d'utilisateur et password dans des variables et utilisé la librairie sélénium pour donner l'url que nous allons tester ainsi que le chemin d'accès à notre driver.

  Après cela on peut définir l'ensemble de nos tests, notamment grâce à des IDs sur la page HTML.

  Cependant http://testphp.vulnweb.com/login.php, ne dispose pas d'id sur le login et le password, il nous est donc impossible d'automatiser grâce au framework notre test fait avec le plugin.