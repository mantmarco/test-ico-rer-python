import os

def scrivi_file_di_prova(nome_file):
    with open(nome_file, 'w') as file:
        file.write("Questo è un file di prova.\n")
        file.write("Puoi scrivere quello che vuoi qui.\n")

if __name__ == "__main__":
    nome_file = "test.txt"
    scrivi_file_di_prova(nome_file)
    print(f"Il file di prova '{nome_file}' è stato creato con successo.")
