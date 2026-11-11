import os

# --- ALGORITMUL 1: Insertion Sort ---
def insertion_sort(lista):
    # Nu folosim sorted() sau list.sort() conform cerintei
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = key
    return lista

# --- ALGORITMUL 2: Merge Sort ---
def merge_sort(lista):
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        R = lista[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lista[k] = R[j]
            j += 1
            k += 1
    return lista

# --- LOGICA PRINCIPALA ---
def main():
    nume_fisier = "date.txt"
    
    # Validare 1: Verificam daca exista fisierul
    if not os.path.exists(nume_fisier):
        print(f"Eroare: Fisierul '{nume_fisier}' nu a fost gasit!")
        return

    # Citim din fisier
    with open(nume_fisier, "r") as f:
        linii = f.readlines()
    
    # Validare 2: Trebuie sa avem cel putin 2 linii
    if len(linii) < 2:
        print("Eroare: Fisierul nu contine date suficiente. Trebuie sa aiba minim 2 linii.")
        return
    
    # Extragem linia 1 (numerele) si linia 2 (algoritmul)
    # Citim din date.txt doar doua linii, nu se citeste numarul elementelor separat.
    numere_text = linii[0].strip().split()
    nume_algoritm = linii[1].strip()
    
    # Validare 3: Verificam daca numerele sunt valide (daca pot fi transformate in intregi)
    try:
        lista_numere = [int(x) for x in numere_text]
    except ValueError:
        print("Eroare: Date invalide pe prima linie! Asigura-te ca ai doar numere intregi separate prin spatiu.")
        return

    # Validare 4: Verificam daca algoritmul cerut exista in aplicatia noastra
    algoritmi_suportati = ["Insertion", "Merge"]
    if nume_algoritm not in algoritmi_suportati:
        print(f"Eroare: Algoritmul '{nume_algoritm}' nu este recunoscut! Alege intre: {algoritmi_suportati}")
        return

    # Executam DOAR algoritmul indicat in fisier (sortare crescatoare)
    if nume_algoritm == "Insertion":
        rezultat = insertion_sort(lista_numere)
    elif nume_algoritm == "Merge":
        rezultat = merge_sort(lista_numere)

    # Scriere rezultat in acelasi fisier, pastrand datele initiale
    # Formatul va fi: Nume_Algoritm: numere sortate
    text_rezultat = f"\n{nume_algoritm}: " + " ".join(str(num) for num in rezultat)
    
    with open(nume_fisier, "a") as f:
        f.write(text_rezultat)
    
    print(f"Sortare reusita cu algoritmul {nume_algoritm}. Verifica fisierul date.txt!")

if __name__ == "__main__":
    main()