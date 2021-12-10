import iterated_power as ip


class EuclidianNorm:
    def __init__(self, mat, itermax, epsilon):
        self.iterpower = ip.IteratedPower(mat, itermax, epsilon)

    def calculate_norm(self):
        val_propre = self.iterpower.iterated_power_method()
