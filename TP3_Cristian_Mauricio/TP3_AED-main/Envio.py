class Envio():
    def __init__(self, cp, df, te, fp):
        self.codigo_postal = cp
        self.direccion_fisica = df
        self.tipo_envio = te
        self.forma_pago = fp

    def __str__(self):
        msg = f"Cod. Postal: {self.codigo_postal:<10}\tDir.Fisica: {self.direccion_fisica:<18}\tTipo Envio: {self.tipo_envio:<2}\tForma Pago: {self.forma_pago:<2}"
        return msg