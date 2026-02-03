import random

LOCATION = {
    "urbano_denso": {"Tóquio": "Kanto", "Osaka": "Kansai"},
    "urbano": {"Kyoto": "Kansai", "Kobe": "Kansai", "Miyagi": "TŌHOKU"},
    "industrial": {"Chiba": "Kanto", "Aichi": "CHŪBU"},
    "suburbano": {"Saitama": "Kanto"},
    "rural": {"Gifu": "CHŪBU", "Nagano": "CHŪBU", "Fukushima": "TŌHOKU", "Iwate": "TŌHOKU"},
    "misto": {"Kanagawa": "Kanto"}
}

# PESOS PROBABILISTICOS PARA GERAR INCIDENTES
# probabilidade de incidente por zona
INCIDENT_PROB_BY_ZONE = {
    "urbano_denso": 0.005,
    "urbano": 0.003,
    "industrial": 0.004,
    "suburbano": 0.003,
    "rural": 0.002,
    "misto": 0.003
}

# probabilidade de eidryan por zona
EIDRYAN_PROB_BY_ZONE = {
    "urbano_denso": {"Cognaris": 0.25, "Karnak": 0.20, "Incaris": 0.55},
    "urbano": { "Cognaris": 0.25, "Karnak": 0.20, "Incaris": 0.55},
    "suburbano": {"Cognaris": 0.30, "Karnak": 0.25, "Incaris": 0.45},
    "industrial": {"Cognaris": 0.25, "Karnak": 0.50, "Incaris": 0.25},
    "rural": {"Cognaris": 0.15, "Karnak":   0.65, "Incaris":  0.20},
    "misto": {"Cognaris": 0.35, "Karnak":   0.40, "Incaris":  0.25}
}

# probabilidade nivel por eidryan
LEVEL_PROB_BY_EIDRYAN = {
    "Cognaris": {4: 0.90, 5: 0.10},
    "Karnak": {2: 0.40, 3: 0.45, 4: 0.15},
    "Incaris": {1: 0.40, 2: 0.35, 3: 0.20, 4: 0.05}
}

# probabilidade de unidade responsavel por eidryan
UNIT_PROB_BY_EIDRYAN = {
    "Cognaris": {
        5: {
            "elite": 0.75,
            "especializada": 0.20,
            "regular": 0.05,
            "auxiliar": 0.00
        },
        4: {
            "elite": 0.41,
            "especializada": 0.57,
            "regular": 0.02,
            "auxiliar": 0.00
        }
    },

    "Karnak": {
        4: {
            "elite": 0.30,
            "especializada": 0.45,
            "regular": 0.20,
            "auxiliar": 0.05
        },
        3: {
            "elite": 0.10,
            "especializada": 0.40,
            "regular": 0.35,
            "auxiliar": 0.15
        },
        2: {
            "elite": 0.00,
            "especializada": 0.20,
            "regular": 0.50,
            "auxiliar": 0.30
        }
    },

    "Incaris": {
        4: {
            "elite": 0.05,
            "especializada": 0.20,
            "regular": 0.45,
            "auxiliar": 0.30
        },
        3: {
            "elite": 0.00,
            "especializada": 0.15,
            "regular": 0.55,
            "auxiliar": 0.30
        },
        2: {
            "elite": 0.00,
            "especializada": 0.10,
            "regular": 0.50,
            "auxiliar": 0.40
        },
        1: {
            "elite": 0.00,
            "especializada": 0.05,
            "regular": 0.45,
            "auxiliar": 0.55
        }
    }
}

# probabilidade de tempo de resposta por unidade
TIME_PROB_BY_UNIT = {
    "elite": {
        "muito_rapida": 0.45,
        "rapida":       0.35,
        "media":        0.15,
        "lenta":        0.04,
        "muito_lenta":  0.01
    },
    "especializada": {
        "muito_rapida": 0.30,
        "rapida":       0.40,
        "media":        0.20,
        "lenta":        0.08,
        "muito_lenta":  0.02
    },
    "regular": {
        "muito_rapida": 0.10,
        "rapida":       0.30,
        "media":        0.40,
        "lenta":        0.15,
        "muito_lenta":  0.05
    },
    "auxiliar": {  # menor rank
        "muito_rapida": 0.05,
        "rapida":       0.20,
        "media":        0.30,
        "lenta":        0.20,
        "muito_lenta":  0.15
    }
}


# PROBABILIDADE DE CONTENÇÃO
RESTRAINT_PROB_BY_TYPE = {
    "Cognaris": {
        4: {"contido": 0.005, "fuga": 0.45, "falha": 0.545},
        5: {"contido": 0.001, "fuga": 0.40, "falha": 0.599},
    },
    "Karnak": {
        2: {"contido": 0.70, "fuga": 0.05, "falha": 0.25},
        3: {"contido": 0.55, "fuga": 0.05, "falha": 0.40},
        4: {"contido": 0.35, "fuga": 0.05, "falha": 0.60},
    },
    "Incaris": {
        1: {"contido": 0.85, "fuga": 0.05, "falha": 0.10},
        2: {"contido": 0.70, "fuga": 0.05, "falha": 0.25},
        3: {"contido": 0.50, "fuga": 0.20, "falha": 0.30},
        4: {"contido": 0.30, "fuga": 0.25, "falha": 0.45},
    }
}

RESTRAINT_PROB_BY_TIME = {
    "muito_rapida": {
        "contido": 0.60,
        "fuga":    0.30,
        "falha":   0.10
    },
    "rapida": {
        "contido": 0.60,
        "fuga":    0.25,
        "falha":   0.15
    },
    "media": {
        "contido": 0.45,
        "fuga":    0.35,
        "falha":   0.20
    },
    "lenta": {
        "contido": 0.30,
        "fuga":    0.40,
        "falha":   0.30
    },
    "muito_lenta": {
        "contido": 0.15,
        "fuga":    0.45,
        "falha":   0.40
    }
}

# MODIFICADORES
MODIFIERS_ZONE = {
    "urbano_denso": {"contido": -0.05, "fuga": +0.10, "falha": +0.10},
    "urbano": {"contido": -0.05, "fuga": +0.05, "falha": +0.05},
    "suburbano": {"contido": -0.05, "fuga": 0.00, "falha": +0.05},
    "industrial": {"contido": +0.1, "fuga": +0.05, "falha": 0.00},
    "rural": {"contido": +0.05, "fuga": -0.05, "falha": +0.05},
    "misto": {"contido": -0.05, "fuga": +0.05, "falha": +0.05}
}

MODIFIER_RESPONSE_BY_UNIT = {
    "elite": {"contido": +0.10, "fuga": -0.10,"falha":   -0.05},
    "especializada": {"contido": +0.08,"fuga": -0.04,"falha":-0.04},
    "regular": {"contido": 0.00,"fuga": 0.00,"falha": 0.00},
    "auxiliar": {"contido": -0.05,"fuga": +0.05, "falha":   +0.5}
}


# cria incidentes
def gerar_incidentes():
    # gera zona probabilistica
    zones_list = list(INCIDENT_PROB_BY_ZONE.keys())
    zones_weights = list(INCIDENT_PROB_BY_ZONE.values())
    zone_chosen = random.choices(zones_list, zones_weights, k=1)[0]

    # pegar a cidade e região
    city = random.choice(list(LOCATION[zone_chosen].keys()))
    region = LOCATION[zone_chosen][city]

    # probabilidade de incidentes de eidryan por zona
    eidryan_by_zone_list = list(EIDRYAN_PROB_BY_ZONE[zone_chosen].keys())
    eidryan_by_zone_weights = list(EIDRYAN_PROB_BY_ZONE[zone_chosen].values())
    eidryan_type_chosen = random.choices(eidryan_by_zone_list, eidryan_by_zone_weights, k=1)[0]

    # probabilidade de level por eidryan
    level_by_eidryans_list = list(LEVEL_PROB_BY_EIDRYAN[eidryan_type_chosen])
    level_by_eidryans_weights = list(LEVEL_PROB_BY_EIDRYAN[eidryan_type_chosen].values())
    eidryan_level_chosen = random.choices(level_by_eidryans_list, level_by_eidryans_weights, k=1)[0]

    # probabilidade de unidade responsavel por eidryan
    unit_by_eidryan_list = list(UNIT_PROB_BY_EIDRYAN[eidryan_type_chosen][eidryan_level_chosen].keys()) #chaves do dict eidryan
    unit_by_eidryan_weights = list(UNIT_PROB_BY_EIDRYAN[eidryan_type_chosen][eidryan_level_chosen].values())
    unit_chosen = random.choices(unit_by_eidryan_list, unit_by_eidryan_weights, k=1)[0]

    # probabilidade de tempo de resposta por unidade responsável
    time_by_unit_list = list(TIME_PROB_BY_UNIT[unit_chosen])
    time_by_unit_weights = list(TIME_PROB_BY_UNIT[unit_chosen].values())
    time_response_chosen = random.choices(time_by_unit_list, time_by_unit_weights, k=1)[0]

    data_incident = {
        "Região": f"{region}",
        "Cidade": f"{city}",
        "Zona": f"{zone_chosen}",
        "Eidryan": f"{eidryan_type_chosen}",
        "Nivel":f"{eidryan_level_chosen}",
        "Unidade": f"{unit_chosen}",
        "Tempo": f"{time_response_chosen}"
    }

    return data_incident

# sortear estado final com distribuição probabilisitca de variaveis aleatorias descritivas
def restraiment_prob(data_incident):
    eidryans_type = data_incident["Eidryan"]
    eidryans_level = int(data_incident["Nivel"])

    # contenção por tipo e nivel, tempo de resposta
    states_list_by_type = RESTRAINT_PROB_BY_TYPE[eidryans_type] # dicionario com os niveis
    states_list_by_temp = RESTRAINT_PROB_BY_TIME[data_incident["Tempo"]]

    # calcular suporte em peso de cada estado
    contido_by_type_weights = states_list_by_type[eidryans_level]["contido"]
    contido_by_temp_weights = states_list_by_temp["contido"]

    fuga_by_type_weights = states_list_by_type[eidryans_level]["fuga"]
    fuga_by_temp_weights = states_list_by_temp["fuga"]

    falha_by_type_weights = states_list_by_type[eidryans_level]["falha"]
    falha_by_temp_weights = states_list_by_temp["falha"]

    support_vectors_contido = contido_by_temp_weights + contido_by_type_weights
    support_vectors_fuga = fuga_by_temp_weights + fuga_by_type_weights
    support_vectors_falha = falha_by_temp_weights + falha_by_type_weights

    # modificadores
    modifiers_zone = MODIFIERS_ZONE[data_incident["Zona"]]
    modifier_zone_contido = modifiers_zone["contido"]
    modifier_zone_fuga = modifiers_zone["fuga"]
    modifier_zone_falha = modifiers_zone["falha"]

    # modificador da variavel contido
    support_vectors_contido = support_vectors_contido + modifier_zone_contido
    support_vectors_fuga = support_vectors_fuga + modifier_zone_fuga
    support_vectors_falha = support_vectors_falha + modifier_zone_falha

    support_vectors_contido = max(0, support_vectors_contido)
    support_vectors_fuga    = max(0, support_vectors_fuga)
    support_vectors_falha   = max(0, support_vectors_falha)


    # distribuição
    suporte_total = support_vectors_contido + support_vectors_fuga + support_vectors_falha
    if suporte_total == 0:
        raise ValueError("Soma dos suportes deu zero — distribuição impossível")
    
    dist_contido = support_vectors_contido / suporte_total
    dist_fuga = support_vectors_fuga / suporte_total
    dist_falha = support_vectors_falha / suporte_total

    print(f"Contido: {dist_contido:.2f}%")
    print(f"Fuga: {dist_fuga:.2f}%")
    print(f"Falha: {dist_falha:.2f}%")

    estados = ["contido", "fuga", "falha"]
    pesos = [dist_contido, dist_fuga, dist_falha]
    estado_sort = random.choices(estados, pesos, k=1)

    sucesso = True if estado_sort[0] == "contido" else False

    return [estado_sort[0], sucesso]

incidente_gerado = gerar_incidentes()
print(incidente_gerado)
print(restraiment_prob(incidente_gerado))
