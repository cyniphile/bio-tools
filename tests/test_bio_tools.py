from bio_tools.bio_tools import split_sequences_to_columns
import pandas as pd


def test_split_sequences_to_columns():
    test_seqs = pd.Series(["aaa", "bbb"])
    result = split_sequences_to_columns(test_seqs)
    assert(result.shape == (2,3))
