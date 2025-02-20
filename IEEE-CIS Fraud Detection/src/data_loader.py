import pandas as pd

def load_and_merge(tx_path, id_path):
    tx = pd.read_csv(tx_path)
    idt = pd.read_csv(id_path)
    return tx.merge(idt, on="TransactionID", how="left")
