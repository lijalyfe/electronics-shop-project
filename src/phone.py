class Phone:
    def __init__(self, name: str, price: float, quantity: int, sim_slots: int) -> None:
        super().__init__(name, price, quantity)
        self.sim_slots = sim_slots

