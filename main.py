from data_generation.conexao import conectar
from data_generation.generation import inserir_incidente

def main():
    conn = conectar()
    cursor = conn.cursor()
    for _ in range(10000):
        inserir_incidente(cursor)
    
    conn.commit()

if __name__ == '__main__':
    main()
