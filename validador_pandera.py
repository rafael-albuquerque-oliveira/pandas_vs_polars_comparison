import polars as pl

# IMPORTANTE: Importando o motor específico do Polars!
import pandera.polars as pa


# 1. DEFINIÇÃO DO CONTRATO (SCHEMA) PANDERA
class TaxiSchema(pa.DataFrameModel):
    """
    Schema de validação em lote nativo para Polars.
    """

    # Usamos os tipos nativos do Python direto, o Pandera traduz para o Polars
    passenger_count: int = pa.Field(ge=0)
    fare_amount: float = pa.Field(ge=0.0)
    PULocationID: int = pa.Field()

    class Config:
        strict = False  # Permite outras colunas passarem sem validação
        coerce = True  # Tenta converter tipos automaticamente


# 2. TESTANDO COM DADOS (POLARS DATAFRAMES)
print("Criando DataFrames de Teste no Polars...")

df_limpo = pl.DataFrame(
    {
        "passenger_count": [1, 2, 4],
        "fare_amount": [15.5, 22.0, 8.75],
        "PULocationID": [142, 236, 161],
        "coluna_extra": ["A", "B", "C"],
    }
)


df_sujo = pl.DataFrame(
    {
        "passenger_count": [1, -2, 4],  # ERRO: -2 passageiros
        "fare_amount": [15.5, -5.0, 8.75],  # ERRO: tarifa negativa
        "PULocationID": [142, 236, 161],
    }
)

print("\n--- Testando DataFrame Limpo ---")
try:
    df_validado = TaxiSchema.validate(df_limpo)
    print("✅ Sucesso! O DataFrame passou no contrato.")
    print(df_validado)
except Exception as e:
    print(f"Erro inesperado: {e}")

print("\n--- Testando DataFrame Sujo ---")
try:
    TaxiSchema.validate(df_sujo)
except pa.errors.SchemaErrors as e:
    print("❌ Acesso Negado! O Pandera encontrou falhas nos dados:")
    print(e)
except Exception as e:
    print(f"❌ Acesso Negado! Erro capturado: \n{e}")
