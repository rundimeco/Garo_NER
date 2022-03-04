# Garo_NER

Données texte initiales : https://lejeunegael.fr/resources/2022/corpora_txt.zip

Comparaison de listes d'éntités pour établir des rapprochements. Trois fonctions dans tools_compare.py :

 - get_similar_two_lists(list1, list2): compare deux listes d'entités
 - get_similar_entity_VS_list(entity, liste): compare une entité à une lsite d'entités
 - get_similar_in_list(liste): compare toutes les entités d'une liste entre elles
 
 Toutes ces fonctions retournent un dictionnaire python avec pour chaque entité traitée, les entités comparées par ordre décroissant de similarité. Exemple :

{'amerique': [[1.0, 'Amerique'],
  [0.8660254037844386, "l'Amerique"],
  [0.7302967433402215, 'Aerique'],
  [0.6546536707079771, 'Amerique du Nord'],
  [0.4629100498862757, "l'Afrique"],
  [0.4330127018922193, 'Americains'],
  [0.4330127018922193, 'Americaine'],
  [0.408248290463863, 'Utique'],
  [0.408248290463863, 'Americaines']...
}

Toutes ces fonctions disposent d'un paramètre **seuil** qui définit la valeur minimale de similarité admise. Par défaut ce seuil est fixé à **0**.

Un notebook est disponible pour tester : compare_NER.ipynb

Améliorations à venir :
 - clustering d'entités
 - raffinement de la similarité avec des poids selon les caractères substitués
