grafo = {
  'Arad' : ['Zerind','Timisoara' , 'Sibiu'],
  'Zerind' : ['Oradea', 'Arad'],
  'Oradea' : ['Sibiu', 'Zerind'],
  'Sibiu' : ['Fagaras', 'Rimnicu Vilcea','Arad', 'Oradea'],
  'Timisoara' : ['Lugoj', 'Arad'],
  'Lugoj' : ['Mehadia', 'Timisoara'],
  'Mehadia' : ['Dobreta', 'Lugoj'],
  'Dobreta' : ['Craivota', 'Mehadia'],
  'Rimnicu Vilcea' : ['Craivota', 'Pitesti', 'Sibiu'],
  'Craivota' : ['Pitesti', 'Dobreta', 'Rimnicu Vilcea'],
  'Fagaras' : ['Bucharest', 'Sibiu'],
  'Pitesti' : ['Bucharest', 'Rimnicu Vilcea', 'Craivota'],
  'Bucharest' : ['Giurgiu', 'Urziceni', 'Pitesti', 'Fagaras'],
  'Giurgiu' : ['Bucharest'],
  'Urziceni' : ['Hirsova', 'Vaslui', 'Bucharest'],
  'Vaslui' : ['Iasi', 'Urziceni'],
  'Iasi' : ['Neamt', 'Vaslui'],
  'Neamt' : ['Iasi'],
  'Hirsova' : ['Eforie', 'Urziceni'],
  'Eforie' : ['Hirsova']
}

visitados = []
fila = []

def bfs(visitados, grafo, no, fim):
  visitados.append(no)
  fila.append(no)

  while fila:
    s = fila.pop(0)
    print (s, end = "  ")
    if s == fim:
      break
    for vizinho in grafo[s]:
      if vizinho not in visitados:
        visitados.append(vizinho)
        fila.append(vizinho)

cidade_atual = 'Arad'
destino = 'Oradea'

bfs(visitados, grafo, cidade_atual, destino)