def load_and_merge(tx_path, id_path):
    tx = pd.read_csv(tx_path)
    idt = pd.read_csv(id_path)

    assert idt["TransactionID"].is_unique, "ID table has duplicates"

    merged = tx.merge(idt, on="TransactionID", how="left")

    assert len(merged) == len(tx), "Row count mismatch after merge"

    return merged

REQUIRED_TX_COLS = {"TransactionID", "TransactionAmt", "ProductCD"}
REQUIRED_ID_COLS = {"TransactionID"}

def load_and_merge(tx_path, id_path):
    tx = pd.read_csv(tx_path)
    idt = pd.read_csv(id_path)

    if not REQUIRED_TX_COLS.issubset(tx.columns):
        raise ValueError("Transaction schema mismatch")

    if not REQUIRED_ID_COLS.issubset(idt.columns):
        raise ValueError("Identity schema mismatch")

    assert idt["TransactionID"].is_unique

    merged = tx.merge(idt, on="TransactionID", how="left")
    assert len(merged) == len(tx)

    return merged

