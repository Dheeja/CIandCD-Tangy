class ThemeParkQueue:
    def __init__(self):
        self.queue = []

    def add_regular_ticket(self):
        self.queue.append("Regular")

    def add_vip_ticket(self):
        self.queue.append("VIP")

    def process_tickets(self):
        new_queue = []
        regular_count = 0
        
        for ticket in self.queue:
            if ticket == "Regular":
                regular_count += 1
                new_queue.append(ticket)
                if regular_count == 3:
                    new_queue.append("VIP")
                    regular_count = 0
            else:
                regular_count = 0
                new_queue.append(ticket)
        
        # Check if there are 2 regular tickets at the end
        if regular_count == 2:
            new_queue.append("VIP")

        self.queue = new_queue

    def show_queue(self):
        for i, ticket in enumerate(self.queue, 1):
            print(f"{i}: {ticket}")

# Example usage:
tp_queue = ThemeParkQueue()
for _ in range(9):  # Adding 9 regular tickets
    tp_queue.add_regular_ticket()

tp_queue.process_tickets()
tp_queue.show_queue()
