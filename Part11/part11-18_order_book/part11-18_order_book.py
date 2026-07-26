# Write your solution here:
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
	        if self._mark == True:
	            return True
	        else:
	            return False
	 
	    def mark_finished(self):
	        self._mark = True
	        
	    @property
	    def mark(self):
	        return self._mark
	 
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
	 
	    def add_order(self, description:str, programmer:str, workload:int):
	        self._orders.append(Task(description=description,workload=workload,programmer=programmer))
	 
	    def all_orders(self) -> list:
	        return self._orders
	 
	    def programmers(self) -> list:
	        programmer = [prog.programmer for prog in self._orders]
	        return list(set(programmer)) 
	 
	    def mark_finished(self, order: int):
	        for o in self._orders:
	            if o.order_id == order:
	                o.mark_finished()
	                break
	        else:            
	            raise ValueError(f"The order {order} doesn't exist")
	 
	    def finished_orders(self) -> list:
	        orders = [p for p in self._orders if p.mark == True]
	        return orders
	                
	 
	    def unfinished_orders(self) -> list:
	        orders = [p for p in self._orders if p.mark == False]
	        return orders               
	 
	    def status_of_programmer(self,programmer:str) -> list:
	        task_finished = 0
	        task_unfinished = 0
	        hours_finished = 0
	        hours_unfinished = 0
	        programmer_task = [p for p in self._orders if p.programmer == programmer]
	        if len(programmer_task) != 0:
	            for p in programmer_task:
	                if p.mark == True:
	                    task_finished +=1
	                    hours_finished += p.workload
	                else:
	                    task_unfinished +=1
	                    hours_unfinished += p.workload
	        else:
	            raise ValueError("programmer has no task assigned")
	        return task_finished,task_unfinished,hours_finished,hours_unfinished
	 
	 
	if __name__ == "__main__":
	    orders = OrderBook()
	    orders.add_order("program webstore", "Adele", 10)
	    orders.add_order("program mobile app for workload accounting", "Adele", 25)
	    orders.add_order("program app for practising mathematics", "Adele", 100)
	    orders.add_order("program the next facebook", "Eric", 1000)
	 
	    orders.mark_finished(1)
	    orders.mark_finished(2)
	 
	    status = orders.status_of_programmer("Cibelle")
	    print(status)
	 



