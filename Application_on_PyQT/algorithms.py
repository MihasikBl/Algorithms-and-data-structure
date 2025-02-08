import sys 
import os
import time
from check import *
from PyQt5 import QtCore, QtDesigner, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QMessageBox
from PyQt5.QtCore import QSize
from math import *
from collections import defaultdict


def writefile(text):                                                  # Запись в файл элементов графа                         
     file_txt = open('results1.txt','a+')
     file_txt.write(f"{text}\n")
     file_txt.close()

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_addBFS.clicked.connect(self.add_vertex_in_graphBFS)
        self.ui.pushButton_addDFS.clicked.connect(self.add_vertex_in_graphDFS)
        self.ui.pushButton_addVertexJH.clicked.connect(self.add_vertex_in_graphJH)
        self.ui.pushButton_resultBFS.clicked.connect(self.resultBFS)
        self.ui.pushButton_resultDFS.clicked.connect(self.resultDFS)
        self.ui.pushButton_resultJH.clicked.connect(self.resultJH)
        self.ui.action.triggered.connect(self.Info)
        self.ui.pushButton.clicked.connect(self.delete_cache)
        
    def delete_cache(self):                                            # Чистка кэша    
         os.remove('results1.txt')
         self.ui.Pole_Otvet.setText("кэш очищен")
         
    def Info(self):
          QMessageBox.about(self, "Автор программы = Ермошкин МВ ИСИТ4-1Б", "Программа была написана студентом 2020-ФГИИБ-ИСИТ-1Б \ Ермошкин М.В.")
    def add_vertex_in_graphDFS(self):                            
         key_dfs = self.ui.textEdit_verDFS.toPlainText()
         value_dfs = self.ui.textEdit_kudaDFS.toPlainText()
         data_dfs = f"{key_dfs}: {value_dfs}"
         print(data_dfs)
         self.ui.Pole_Otvet.setText("Добавлена пара ключ:значение")
         writefile(data_dfs)
    def add_vertex_in_graphBFS(self):
         key_bfs = self.ui.textEdit_verBFS.toPlainText()
         value_bfs = self.ui.textEdit_kudaBFS.toPlainText()
         data_bfs = f"{key_bfs}: {value_bfs}"
         print(data_bfs)     
         self.ui.Pole_Otvet.setText("Добавлена пара ключ:значение")
         writefile(data_bfs)
    def add_vertex_in_graphJH(self):
         key_JH = self.ui.textEdit_verJH.toPlainText()
         print(key_JH)
         self.ui.Pole_Otvet.setText("Вершина добавлена")
         writefile(key_JH)
    def resultDFS(self):
         self.ui.Pole_Otvet.setText(' ')
         dfs_graph_txt = 'results1.txt'
         with open(dfs_graph_txt, 'r') as dfs_graph_txt:
              lines = dfs_graph_txt.readlines()
         graph = {}
         for line in lines:
              key, value = line.strip().split(':')
              graph[key.strip()] = list(value.strip())
         print("Dictionary created") 
         self.ui.Pole_BaseGraph.setText(f"Создан граф:\n {graph}")

         visited = set() # Создаем множество для отслеживания посещенных узлов графика.
         f = open('dfs_otvet1.txt','a+')

         def dfs(visited, graph, node = []):  #функция dfs 
            if node not in visited:
                f.write(f'{node} -> ')
                print(node, end=" ")
                visited.add(node)
                for neighbour in graph[node]:
                    dfs(visited, graph, neighbour)
         based_vertex = self.ui.textEdit_BaseVertex.toPlainText()      
         print(based_vertex)  
         dfs(visited, graph, based_vertex) 
         f.close()       
         
         f = open('dfs_otvet1.txt','r')
         result = f.read()
         result = result[:-3]
        
         self.ui.Pole_Otvet.setText(f'Результат работы DFS: {result}')
         f.close()
         os.remove('dfs_otvet1.txt')
    def resultBFS(self):
         self.ui.Pole_Otvet.setText(' ')
         bfs_graph_txt = 'results1.txt'
         with open(bfs_graph_txt, 'r') as bfs_graph_txt:
              lines = bfs_graph_txt.readlines()
         graph = {}
         for line in lines:
              key, value = line.strip().split(':')
              graph[key.strip()] = list(value.strip())
         print("Dictionary created") 
         self.ui.Pole_BaseGraph.setText(f"Создан граф:\n {graph}")   
         visited = [] # посещенные вершины 
         queue = []   # очередь узлов 
         f = open('bfs_otvet1.txt','a+') 
         def bfs(visited, graph, start_node): 
             visited.append(start_node)  # добавление в посещенные
             queue.append(start_node)    # добавление в очередь
    
             while queue:
                 s = queue.pop(0)        # удаляем элемент из очереди и возвращаем его
                 f.write(f'{s} -> ')
                 print (s, end = " ")    # печать элемента 
        
                 for neighbor in graph[s]:  
                     if neighbor not in visited:
                         visited.append(neighbor)
                         queue.append(neighbor)
         based_vertex = self.ui.textEdit_BaseVertex.toPlainText()
         bfs(visited,graph,based_vertex)
         f.close()       
         
         f = open('bfs_otvet1.txt','r')
         result = f.read()
         result = result[:-3]
        
         self.ui.Pole_Otvet.setText(f'Результат работы BFS: {result}')
         f.close()
         os.remove('bfs_otvet1.txt')

    def resultJH(self):
#----------Cоздание графа для алгоритма----------         
         self.ui.Pole_Otvet.setText(' ')  
         JH_graph_txt = 'results1.txt'
         with open(JH_graph_txt, 'r') as JH_graph_txt:
              lines = JH_graph_txt.readlines()
         graph_JH = []
         for line in lines:
              list_JH = line.strip().split('_')
              for i in range(0,len(list_JH)):
                   list_JH[i] = int(list_JH[i]) 
              graph_JH.append(list(list_JH))
         print(graph_JH) 
         self.ui.Pole_BaseGraph.setText(f"Создан граф:\n {graph_JH}")

#----------Алгоритм Джонсона---------------
         MAX_INT = float('Inf')
         x = 0
         xv = 0
         # Возвращаем вершину с минимальным 
         # расстоянием от исходной вершины
         def minDistance(dist, visited):
          
             (minimum, minVertex) = (MAX_INT, 0)
             for vertex in range(len(dist)):
                 if minimum > dist[vertex] and visited[vertex] == False:
                     (minimum, minVertex) = (dist[vertex], vertex)
          
             return minVertex
 
 
# Алгоритм Дейкстры для обновленного 
# Графа (с помощью удаления отрицательных весов между вершинами)
         def Dijkstra(graph, modifiedGraph, src):
          
             # Номер вершины в графе 
             num_vertices = len(graph)
          
             # Создаем словарь, чтобы проверить, включена ли вершина 
             # в дерево кратчайших путей 
             sptSet = defaultdict(lambda : False)
          
             # Кратчайшее расстояние всех вершин от исходной 
             dist = [MAX_INT] * num_vertices
          
             dist[src] = 0
          
             for count in range(num_vertices):
          
                 # Текущая вершина, которая находится на мин. расстоянии
                 # от исходной вершины и еще не включена в 
                 # дерево кратч. путей
                 curVertex = minDistance(dist, sptSet)
                 sptSet[curVertex] = True
          
                 for vertex in range(num_vertices):
                     if ((sptSet[vertex] == False) and
                         (dist[vertex] > (dist[curVertex] +
                         modifiedGraph[curVertex][vertex])) and
                         (graph[curVertex][vertex] != 0)):
                          
                         dist[vertex] = (dist[curVertex] +
                                         modifiedGraph[curVertex][vertex]);
          
             # Печатаем кратч. расстояние от исх. вершины
             for vertex in range(num_vertices):
                 xv = vertex + 1
                 print ('Вершина ' + str(xv) + ': ' + str(dist[vertex]))
 
         # Функция для вычисления кратч. расстояний от исх. вершины
         # до всех остальных вершин с использование алгоритма Беллмана-Форда
         def BellmanFord(edges, graph, num_vertices):
          
             # Добавляем счетчик и присваеваем ему мин. расстояние
             # от всех вершин графа до фиксированной вершины
             dist = [MAX_INT] * (num_vertices + 1)
             dist[num_vertices] = 0
          
             for i in range(num_vertices):
                 edges.append([num_vertices, i, 0])
          
             for i in range(num_vertices):
                 for (src, des, weight) in edges:
                     if((dist[src] != MAX_INT) and
                             (dist[src] + weight < dist[des])):
                         dist[des] = dist[src] + weight
          
             # Передаем кратч. расстояние
             return dist[0:num_vertices]
          
         # Функция реализации алгоритма Джонсона
         def JohnsonAlgorithm(graph):
             edges = []
          
             # Создаем список из всех весов графа для алгоритма Беллмана-Ф         орда
             for i in range(len(graph)):
                 for j in range(len(graph[i])):
                     if graph[i][j] != 0:         
                         edges.append([i, j, graph[i][j]])
          
             # Веса вершин, которые используются для изменения исх. весов
             modifyWeights = BellmanFord(edges, graph, len(graph)) 
             modifiedGraph = [[0 for x in range(len(graph))] for y in range(len(graph))]
 
    # Изменение веса, чтобы избавиться от отрицательных значений
             for i in range(len(graph)):
                 for j in range(len(graph[i])):
                     if graph[i][j] != 0:
                         modifiedGraph[i][j] = (graph[i][j] + modifyWeights[i] - modifyWeights[j]);
 
             print ('Конечный граф Джонсона: ' + str(modifiedGraph))
             self.ui.Pole_Otvet.setText(f"Конечный граф Джонсона {modifiedGraph}")
 
    # Run Dijkstra for every vertex as source one by one
             for src in range(len(graph)):
                 x = src + 1
                 print ('\nКратчайшее расстояние с вершиной ' + str(x) + ':\n')
                 Dijkstra(graph, modifiedGraph, src)
         JohnsonAlgorithm(graph_JH)


if __name__=="__main__":
       app = QtWidgets.QApplication(sys.argv)
       myapp = MyWin()
       myapp.show()
       sys.exit(app.exec_())
