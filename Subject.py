class Subject:
    def __init__(self, code, nameth, nameen, credit1, credit2, credit3):
        self.code = code
        self.nameth = nameth
        self.nameen = nameen
        self.credit1 = credit1
        self.credit2 = credit2
        self.credit3 = credit3
        
    def __str__(self) -> str:
        return f"รหัสวิชา {self.code} {self.nameth} ({self.nameen}) หน่วยกิต: {self.credit1}-{self.credit2}-{self.credit3}"