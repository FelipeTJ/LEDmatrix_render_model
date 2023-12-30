from render_sim.core.frame_gen import pd, get_empty_df


def intersect_series(row_int: int, col_int: int, N: int) -> pd.DataFrame:
    assert_int_size(row_int, N)
    assert_int_size(col_int, N)
    df = get_empty_df(N)

    rowS = value_to_series(row_int, N)
    colS = value_to_series(col_int, N)
    rowS.name = 'rows'
    colS.name = 'cols'
    
    comb = pd.merge(rowS, colS, how='cross').all(axis=1)
    active_rows = comb.index[comb] // N
    active_cols = comb.index[comb] % N
    df.loc[active_rows, active_cols] = True

    return df

def get_2powerN(N: int) -> pd.Series:
    return pd.Series([2**i for i in range(N)])

def get_series_value(row: pd.Series) -> int:
    return get_2powerN(row.size).loc[row].sum()

def value_to_series(val: int, N: int) -> pd.Series:
    assert_int_size(val, N)
    return pd.Series(reversed(list(f"{val:0{N}b}")), dtype=int).astype(bool)

def assert_int_size(int: int, N: int) -> None:
    assert 0 <= int < 2 ** (N + 1), f"Out of range {int} > {N}"