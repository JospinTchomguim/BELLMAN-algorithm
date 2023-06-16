import timeit

class Graph:

    def __init__(self, vertices):

        self.M = vertices   # Nombre total de sommets dans le graphe

        self.graph = []   #Tableau d'arêtes

#L'ajout des arêtes

    def add_edge(self, a, b, c):

        self.graph.append([a, b, c])


    def print_solution(self, distance):

        print("Distance du sommet depuis de la source")

        for k in range(self.M):

            print("{0}\t\t{1}".format(k, distance[k]))



    def Bellman(self, src):

        distance = [float("Inf")] * self.M

        distance[src] = 0


        for _ in range(self.M - 1):

            for a, b, c in self.graph:

                if distance[a] != float("Inf") and distance[a] + c < distance[b]:

                    distance[b] = distance[a] + c



        for a, b, c in self.graph:

            if distance[a] != float("Inf") and distance[a] + c < distance[b]:

                print("Ce graphe contient un cycle de poids négatif")

                return



        self.print_solution(distance)



g = Graph(6)

g.add_edge(0, 1, 5) #represente le chemin 0--->1 qui a un poids 5

g.add_edge(0, 2, 4)

g.add_edge(1, 3, 6)

g.add_edge(1, 4, 8) 

g.add_edge(2, 4, 1) #represente le chemin 2--->4 qui a un poids 1

g.add_edge(2, 5, 7)

g.add_edge(4, 3, 3)

g.add_edge(4, 5, 2)

# Appel de la fonction avec le sommet de départ 
g.Bellman(0)

# Mesure du temps d'exécution avec timeit
t = timeit.timeit(number=1) 
print("Durée d'exécution : %.5f secondes" % t)
