     
  ## Institut des Algorithmes du Sénégal
   ```ruby
# Usefull funtions that make it possible to give a list of numbers 
# And calculate it's max and min
liste = []
# Une liste de taille n
def create_lite(n):
    for i in range(n):
        # Entrer les éléments de la liste
        x = input("entrer un entier ")
        liste.append(x)
    return liste
# Calculer le max et le min
def max_min_val(liste):
      max_value = max(liste)
      min_value = min(liste)
      print("The max value of the list is: ",max_value)
      print("The min value of the list is: ",min_value)
      return [max_value,min_value]
   ```
