import matplotlib.pyplot as plt

def mergeSort(list_to_sort):
    """
    Sortiert eine Liste in aufsteigender Reihenfolge mithilfe des Merge-Sort-Algorithmus.

    Parameter:
    list_to_sort (list): Die zu sortierende Liste.

    Rückgabe:
    None: Die Funktion modifiziert die Eingangsliste direkt.

    """
    if len(list_to_sort) > 1:
        # Teile die Liste in zwei Hälften
        mid = len(list_to_sort) // 2
        left_half = list_to_sort[:mid]
        right_half = list_to_sort[mid:]

        # Sortiere beide Hälften der Liste (Rekursion)
        mergeSort(left_half)
        mergeSort(right_half)

         # Initialisiere die Indizes für die linke Hälfte, die rechte Hälfte und die sortierte Liste
        left_index = 0
        right_index = 0
        sorted_index = 0

        # Füge die Elemente der linken und rechten Hälften sortiert in die sortierte Liste ein
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                list_to_sort[sorted_index] = left_half[left_index]
                left_index += 1
            else:
                list_to_sort[sorted_index] = right_half[right_index]
                right_index += 1
            sorted_index += 1

        # Füge die restlichen Elemente der linken und rechten Hälften hinzu
        while left_index < len(left_half):
            list_to_sort[sorted_index] = left_half[left_index]
            left_index += 1
            sorted_index += 1

        while right_index < len(right_half):
            list_to_sort[sorted_index] = right_half[right_index]
            right_index += 1
            sorted_index += 1


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# Erstelle eine Liste von Indizes für die x-Achse
x = range(len(my_list))

# Zeichne die ursprüngliche Liste
plt.plot(x, my_list)
plt.show()

# Sortiere die Liste
mergeSort(my_list)

# Zeichne die sortierte Liste
plt.plot(x, my_list)
plt.show()
