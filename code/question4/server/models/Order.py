class Order:
    def __init__(self, supplier_id, item, status):
        self.id = 0
        self.supplier_id = supplier_id
        self.item = item
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "supplier_id": self.supplier_id,
            "item": self.item,
            "status": self.status
        }

    def from_dict(data):
        return Order(
            id=data["id"],
            supplier_id=data["supplier_id"],
            item=data["item"],
            status=data["status"]
        )
