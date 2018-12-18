// Grupo XYZ, Fulano y Mengano
// Comentario general sobre la solucio´n,
// explicando co´mo se resuelve el problema
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <assert.h>
#include <stdio.h>
#include <algorithm>
#include "Matriz.h"

using namespace std;

const int INF = numeric_limits<int>::max();

// funcio´n que resuelve el problema
// comentario sobre el coste, O(f(N))
void caminoMinimo(const int &start,vector<int> &sol,vector<int> &solFinal, const int &V, const Matriz<int> &distancias,
	vector<bool> &marcas, int &contVert, int &k, int &suma, int &sumaMin) {
	
	for (int i = 0; i < V; i++) {

		if (distancias[k][i] != 0 && distancias[k][i] != -1) {

			if (i == start && contVert == V) {
				sol[contVert] = i + 1;
				suma += distancias[k][i];
				contVert++;
				
				if (suma <= sumaMin) {
					sumaMin = suma;
					suma = 0;

					for (int i = 0; i < sol.size(); i++) {
						solFinal[i] = sol[i];
					}
				}
			}
			else if (!marcas[i]) {
				marcas[i] = true;
				sol[contVert] = i + 1;
				contVert++;
				suma += distancias[k][i];

				caminoMinimo(start, sol,solFinal, V, distancias, marcas, contVert, i, suma, sumaMin);

				marcas[i] = false;
				contVert--;
				suma -= distancias[k][i];

			}
		}
	}
}

// Resuelve un caso de prueba, leyendo de la entrada la
// configuracio´n, y escribiendo la respuesta
void resuelveCaso() {
	// leer los datos de la entrada
	int ini, fin, valor;
	int E, V;
	int start;//Donde quieres empezar camino minimo y terminarlo vertice


	/*
	--------------------PARA METER LOS DATOS POR CONSOLA-------------------------

	cout << "Introduce el numero de vertices = ";
	cin >> V;
	
	
	
	Matriz<int> distancias(V, V);
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			if(i == j) distancias[i][j] = 0; //La distancia de un vertice a el mismo  es 0
			else distancias[i][j] = -1; //Para los vertices a los que no puedes ir desde el vertice actual
		}
	}

	//Crear grafo con todas las aristas porque luego solo voy a utilizar las necesarias para calcular el 
	//camino minimo
	cout << "Introduce las aristas y su distancia (3 numeros separados)= ";
	cin >> ini;
	while(ini != -1) {
		cin >> fin >> valor;
		distancias[ini - 1][fin - 1] = valor;
		distancias[fin - 1][ini - 1] = valor;
		cout << "Introduce las aristas y su distancia (3 numeros separados)= ";
		cin >> ini;
		
	}

	//Mostrando matriz de prueba
	/*
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			cout << distancias[i][j] << " ";
		}
		cout << "\n";
	}
	*/
	/*
	cout << "inicio del camino = ";
	cin >> start;
	start--;
	*/

	//--------------------DATOS DESDE TXT-----------------------
	cin >> V >> start;
	Matriz<int> distancias(V, V);
	
	for (int i = 0; i < V; i++) {
		for (int j = 0; j < V; j++) {
			if (i == j) distancias[i][j] = 0; //La distancia de un vertice a el mismo  es 0
			else distancias[i][j] = -1; //Para los vertices a los que no puedes ir desde el vertice actual
		}
	}
	cin >> ini;

	while (ini != -1) {
		cin >> fin >> valor;
		distancias[ini - 1][fin - 1] = valor;
		distancias[fin - 1][ini - 1] = valor;
		cin >> ini;
	}


	vector<bool> marcas(V, false);
	vector<int> sol(V + 1, 0);
	vector<int> solFinal(V + 1, 0);
	sol[0] = start;
	start--;
	marcas[start] = true;

	int suma = 0, sumaMin = INF, contVert = 1;
	caminoMinimo(start, sol,solFinal, V, distancias, marcas, contVert, start, suma, sumaMin);
	for (int i = 0; i < solFinal.size(); i++) {
		cout << solFinal[i] << " ";
	}
	cout << sumaMin << endl;
}

int main() {
	// Para la entrada por fichero.
	// Comentar para acepta el reto
#ifndef DOMJUDGE
	std::ifstream in("DATOS.TXT");
	auto cinbuf = std::cin.rdbuf(in.rdbuf()); //save old buf and redirect std::cin to casos.txt
#endif 

	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		resuelveCaso();
	}
	
	


	// Para restablecer entrada. Comentar para acepta el reto
#ifndef DOMJUDGE // para dejar todo como estaba al principio
	std::cin.rdbuf(cinbuf);
	system("PAUSE");
#endif

	return 0;
}