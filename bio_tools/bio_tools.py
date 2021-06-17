import pandas as pd


def split_sequences_to_columns(sequences: pd.Series) -> pd.DataFrame:
    """
    TODO: rather slow, research jax unirep
    """
    return sequences.apply(lambda x: pd.Series(list(x)))
