from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial
import math

def get_similar_two_lists(list1, list2, seuil = 0):
  dic_similarity = {}
  for entity in list1:
    similarities = get_similar_entity_VS_list(entity, list2, seuil)
    dic_similarity[entity] = similarities[entity]
  return dic_similarity   

def get_similar_entity_VS_list(entity, liste, seuil =  0):
  liste = list(set(liste))
  out = {entity:[]}
  V = CountVectorizer(ngram_range = (3,3), analyzer = "char")
  X = V.fit_transform([entity]+liste).toarray()
  vecteur_entite = X[0]
  for cpt, vecteur_compare in enumerate(X[1:]):
    dist = spatial.distance.cosine(vecteur_entite, vecteur_compare)
    if math.isnan(dist)==True:
      sim = 0
    else:
      sim = 1 - dist
    if sim<=seuil:
      continue
    entite_comparee = liste[cpt]
    out[entity].append([sim, entite_comparee])
  out = {cle:sorted(liste, reverse=True) for cle, liste in out.items()} 
  return out
    
def get_similar_in_list(liste, seuil = 0):
  dic_similarity = {}
  for entity in liste:
    liste_filter = [x for x in set(liste) if x!=entity]
    similarities = get_similar_entity_VS_list(entity, liste_filter, seuil)
    dic_similarity[entity] = similarities[entity]
  return dic_similarity
# -


