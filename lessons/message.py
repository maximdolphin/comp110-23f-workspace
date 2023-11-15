"""Class that store a message (operator overload, union types, default paramters)."""

class Email:
    
    to: str | int
    message: str
    important: bool
    
    def __init__(self, recipient: str | int, message_text: str = "", importance_flag: bool = False):
        """Constructor of an email"""
        self.to = recipient
        self.message = message_text
        self.important = importance_flag
        
    def __str__(self) -> str:
        m_string: str = f"To: {self.to} \n"
        m_string += f"Important? {self.important} \n"
        m_string += f'"{self.message}"'
        return m_string
    
    def __mul__(self, factor: int):
        """Operator overload for multiplication."""
        self.message *= factor
        
email_to_chiara: Email = Email("chiara", "You're a great TA! ", False)

# email_to_chiara * 100

print(email_to_chiara)
email_to_lauren: Email = Email(730658668)
print(email_to_lauren)
email_to_lauren.message = "You're the best!"
print(email_to_lauren)