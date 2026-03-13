from rules.rules_data import gerar_incidentes, restraiment_prob

def inserir_incidente(cursor):
    dict_incidente = gerar_incidentes()
    resultado_incidente = restraiment_prob(dict_incidente)

    cursor.execute(
    "SELECT id FROM localidades WHERE cidade = %s",
    (dict_incidente['Cidade'],)
    )
    id_local = cursor.fetchone()[0]
        
    cursor.execute(
        "SELECT id FROM eidryans WHERE tipo = %s",
        (dict_incidente['Eidryan'],)
    )
    id_eidryan = cursor.fetchone()[0]

    sql = """
    INSERT INTO incidentes 
    (id_eidryan, id_local, nivel_eidryan, unidade, tempo_resposta, resultado)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    valores = (
        id_eidryan,
        id_local,
        dict_incidente['Nivel'],
        dict_incidente['Unidade'],
        dict_incidente['Tempo'],
        resultado_incidente
    )

    print(
    f"{id_eidryan:<10} "
    f"{id_local:<10} "
    f"{dict_incidente['Nivel']:<10} "
    f"{dict_incidente['Unidade']:<15} "
    f"{dict_incidente['Tempo']:<15} "
    f"{resultado_incidente:<15}"
)
    cursor.execute(sql, valores)
