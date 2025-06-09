def load_and_merge(tx_path, id_path):
    tx = pd.read_csv(tx_path)
    idt = pd.read_csv(id_path)

    assert idt["TransactionID"].is_unique, "ID table has duplicates"

    merged = tx.merge(idt, on="TransactionID", how="left")

    assert len(merged) == len(tx), "Row count mismatch after merge"

    return merged
