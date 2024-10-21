import os

def read_single_number_from_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return float(f.readline().strip().replace(",", "."))
    except ValueError:
        print(f"Erreur de conversion dans le fichier {filepath}")
        return None

def compare_single_numbers(file1, file2, tolerance=0.01):
    number1 = read_single_number_from_file(file1)
    number2 = read_single_number_from_file(file2)
    
    if number1 is None or number2 is None:
        return False
    
    return abs(number1 - number2) <= tolerance

repositories = [
    "https://github.com/alpjakop/REP",
    "https://github.com/Humilokaki/TP2-REP-INSA-202425.git",
    "https://github.com/Mistyycs/REP-TP2",
    "https://github.com/Kaeios/assoc-REP/",
    "https://github.com/Dyskal/repro",
    "https://github.com/PaulineRoches/REP_popo_sos.git",
    "https://github.com/l55I1/REP",
    "https://github.com/matth1446/rep_mh_vvk",
    "https://github.com/AntoineMarchalDombrat/REP_Antoine_Jean"
]

target_dir = "external_repos"
my_answer_file = "answer_associativity.txt"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

os.chdir(target_dir)

for repo in repositories:
    repo_name = repo.split('/')[-1].replace('.git', '')
    
    if not os.path.exists(repo_name):
        command = f"git clone {repo}"
        result = os.system(command)
        if result == 0:
            print(f"[+] Cloné avec succès : {repo_name}")
        else:
            print(f"[-] Erreur lors du clonage : {repo_name}")
            continue
    
    answer_file_path = os.path.join(repo_name, "answer_associativity.txt")
    
    if os.path.exists(answer_file_path):
        if compare_single_numbers(my_answer_file, answer_file_path):
            print(f"[+] Le fichier 'answer_associativity.txt' de {repo_name} est identique à votre fichier.")
        else:
            print(f"[-] Le fichier 'answer_associativity.txt' de {repo_name} est différent de votre fichier.")
    else:
        print(f"[!] Le fichier 'answer_associativity.txt' est introuvable dans {repo_name}. Comparaison ignorée.")
