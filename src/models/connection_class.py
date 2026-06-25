class Connection:
    def __init__(self, name1, name2, metadata=None) -> None:
        self.name1 = name1
        self.name2 = name2
        default_metadata = {"max_link_capacity": 1}
        self.metadata = default_metadata.copy()
        if metadata:
            self.metadata.update(metadata)
