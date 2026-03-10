from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import Optional
from datetime import datetime


# 1. DEFINIÇÃO DO CONTRATO DE DADOS (SCHEMA)
class CorridaTaxi(BaseModel):
    """
    Schema de validação para uma corrida de táxi.
    Garante que os dados vindos da API/JSON estejam perfeitos antes do processamento.
    """

    VendorID: int
    tpep_pickup_datetime: datetime
    tpep_dropoff_datetime: datetime
    passenger_count: Optional[int] = Field(
        default=1, ge=0, description="Número de passageiros (mínimo 0)"
    )
    trip_distance: float = Field(
        ge=0.0, description="Distância da viagem não pode ser negativa"
    )
    PULocationID: int
    DOLocationID: int
    fare_amount: float

    # Validação customizada avançada
    @field_validator("fare_amount")
    @classmethod
    def validar_tarifa(cls, valor: float) -> float:
        if valor <= 0:
            raise ValueError("O valor da tarifa deve ser estritamente maior que zero.")
        return valor


# 2. TESTANDO NA PRÁTICA (SIMULANDO JSONs)

# Cenário A: Dado Perfeito chegando da API (Dicionário/JSON)
payload_valido = {
    "VendorID": 1,
    "tpep_pickup_datetime": "2023-01-01T00:32:10",  # O Pydantic converte string ISO para datetime automaticamente!
    "tpep_dropoff_datetime": "2023-01-01T00:40:36",
    "passenger_count": 2,
    "trip_distance": 2.5,
    "PULocationID": 142,
    "DOLocationID": 236,
    "fare_amount": 15.50,
}

# Cenário B: Dado Sujo chegando da API (Erro comum em sistemas legados)
payload_sujo = {
    "VendorID": "UM",  # Erro: String no lugar de Int
    "tpep_pickup_datetime": "2023-01-01 00:32:10",
    "tpep_dropoff_datetime": "2023-01-01 00:40:36",
    "passenger_count": -1,  # Erro: Passageiro negativo não existe
    "trip_distance": 2.5,
    "PULocationID": 142,
    "DOLocationID": 236,
    "fare_amount": 0.00,  # Erro: Tarifa zerada (barrado pelo nosso validador customizado)
}

print("--- Testando Payload Válido ---")
try:
    corrida_limpa = CorridaTaxi(**payload_valido)
    print("Sucesso! Dado validado e tipado:")
    print(repr(corrida_limpa))
except ValidationError as e:
    print(e)

print("\n--- Testando Payload Sujo ---")
try:
    corrida_suja = CorridaTaxi(**payload_sujo)
except ValidationError as e:
    print("Acesso Negado! O Pydantic barrou os seguintes erros:")
    print(e)
