## Time Blocks 

Skrypt pozwalający na szybkie, zautomatyzowane tworzenie zadań w kalendarzu google.
Tworzone są eventy w kolejności tak jak w pliku wejściowym. Dodawane do agendy 
w wybranym dniu -> informacja podana wraz z danymi wejściowymi. 

### Wprowadzanie danych:
    1. plik podawany do funkcji main *python timeBlocks.py input_data_as_text*
    2. format zapisu danych: nazwa zadania ;[czas w minutach] np.:
		+ instalacja oprogramowania ;20m
		+ medytacja;15m
		+ drzemka;25m
	3. możliwość zdefiniowania przerw czasowych (nie jako wydarzenie, a odstęp pomiędzy eventami):
		- " --- ; 30m "

    
