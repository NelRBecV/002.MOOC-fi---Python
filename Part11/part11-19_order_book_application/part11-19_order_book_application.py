# Write your solution here
	# If you use the classes made in the previous exercise, copy them here
	class Task:
	    id = 0
	 
	    def __init__(self, description: str, programmer: str, workload: int):
	        self.description = description
	        self.workload = workload
	        self.programmer = programmer
	        self._mark = False
	        Task.id += 1
	        self.id = Task.id
	 
	    def is_finished(self):
	        return self._mark:	            
	 
	    def mark_finished(self):
	        self._mark = True	 
	   	 
	    @property
	    def order_id(self):
	        return self.id
	 
	    def __str__(self) -> str:
	        hours = "hour" if self.workload == 1 else "hours"
	        condition = "FINISHED" if self.is_finished() else "NOT FINISHED"
	        return f"{self.id}: {self.description} ({self.workload} {hours}), programmer {self.programmer} {condition}"
	 
	 
	class OrderBook:
	    def __init__(self) -> None:
	        self._orders = []
	 
	    def add_order(self, description: str, programmer: str, workload: int):
	        self._orders.append(Task(description=description, workload=workload, programmer=programmer))
	 
	    def all_orders(self):
	        return self._orders
	 
	    def programmers(self):
	        programmer = [prog.programmer for prog in self._orders]
	        return list(set(programmer))
	 
	    def mark_finished(self, order: int):
	        for o in self._orders:
	            if o.order_id == order:
	                o.mark_finished()
	                break
	        else:
	            raise ValueError(f"The order {order} doesn't exist")
	 
	    def finished_orders(self):
	        orders = [p for p in self._orders if p.is_finished()]
	        return orders
	 
	    def unfinished_orders(self):
	        orders = [p for p in self._orders if not p.is_finished()]
	        return orders
	 
	    def status_of_programmer(self, programmer: str):
	        task_finished = len([task for task in self.finished_orders() if task.programmer == programmer])
	        task_unfinished = len([task for task in self.unfinished_orders() if task.programmer == programmer])
	        hours_finished = sum([hour.workload for hour in self.finished_orders() if hour.programmer == programmer])
	        hours_unfinished = sum([hour.workload for hour in self.unfinished_orders() if hour.programmer == programmer])
	        if not hours_finished and not hours_unfinished:
	            raise ValueError("programmer has no task assigned")
	 
	        return task_finished, task_unfinished, hours_finished, hours_unfinished
	 
	 
	class UserInterface:
	    def instructions(self):
	        print("commands: ")
	        print("0 exit")
	        print("1 add order")
	        print("2 list finished tasks")
	        print("3 list unfinished tasks")
	        print("4 mark task as finished")
	        print("5 programmers")
	        print("6 status of programmer")
	 
	    def interface(self):
	        orders = OrderBook()
	        while True:
	            command = input("command: ")
	            if command == "0":
	                break
	            elif command == "1":
	                desc = input("description: ")
	                try:
	                    programmer, workload = input("programmer and workload estimate: ").split()
	                    workload = int(workload)
	                except:
	                    print("erroneous input")
	                else:
	                    orders.add_order(desc,programmer,workload)
	                    print("added!")                
	            elif command == "2":
	                finished = [o for o in orders.finished_orders()]
	                if len(finished) != 0:
	                    for task in finished:
	                        print(task)
	                else:                    
	                    print("no finished tasks" )
	            elif command == "3":
	                unfinished = [o for o in orders.unfinished_orders()]
	                if len(unfinished) != 0:
	                    for task in unfinished:
	                        print(task)
	                else:
	                    print("no unfinished tasks" )
	            elif command == "4":
	                try:
	                    task_num = int(input("id: "))
	                    orders.mark_finished(task_num)
	                except ValueError:
	                    print("erroneous input")                    
	                else:               
	                    print("marked as finished")
	            elif command == "5":
	                for programmer in orders.programmers():
	                    print(programmer)
	            elif command == "6":
	                name = input("programmer: ")
	                try:
	                    fin, unfin,gone,left = orders.status_of_programmer(name)
	                except:
	                    print("erroneous input")
	                else:
	                    print(f"tasks: finished {fin} not finished {unfin}, hours: done {gone} scheduled {left}")
	            else:
	                print("command not supported")
	 
	    def execute(self):
	        self.instructions()
	        self.interface()
	 
	 
	program = UserInterface()
	program.execute()



