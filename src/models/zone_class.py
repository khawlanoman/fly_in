class Zone:
    def __init__(self, name: str, x: int, y: int, metadata: dict[str, str | int] | None = None)-> None:
        self.name = name
        self.x = x
        self.y = y
        default_meta = {"color": None, "zone": "normal", "max_drones": 1}
        self.metadata = default_meta.copy()
        if metadata:
            self.metadata.update(metadata)

    def movement_cost(self) -> int:
        if (self.metadata["zone"] == "normal" or self.metadata["zone"] == "priority"):
                return (1)
        elif self.metadata["zone"] == "restricted":
                return (2)
        elif self.metadata["zone"] == "blocked":
                return 0
        return (0)
