import queue
from math import lcm
input_file = "input.txt"

if input_file == "ex1":
    path = "20/example1.txt"
elif input_file == "ex2":
    path = "20/example2.txt"
else:
    path = "20/input.txt"

with open(path) as f:
    module_list = f.read().split("\n")

class FlipFlop:
    def __init__(self, data) -> None:
        self.name = data.split(" -> ")[0][1:]
        self.state = "off"
        self.destinations = data.split("-> ")[1].split(", ")
    
    def recieve_pulse(self, pulse, queue):
        if pulse.strength == "high":
            pass
        elif pulse.strength == "low":
            if self.state == "off":
                self.state = "on"
                for destination in self.destinations:
                    queue.put(self.generate_pulse(source=self.name, destination=destination, strength="high"))
            elif self.state == "on":
                self.state = "off"
                for destination in self.destinations:
                    queue.put(self.generate_pulse(source=self.name, destination=destination, strength="low"))

    def generate_pulse(self, source, destination, strength):
        return Pulse(source, destination, strength)
        

class Conjunction:
    def __init__(self, data) -> None:
        self.name = data.split(" -> ")[0][1:]
        self.destinations = data.split("-> ")[1].split(", ")
        self.memory = self.get_source_modules(module_list)

    def get_source_modules(self, module_list):
        memory = {}
        for module in module_list:
            name = module.split(" -> ")[0].replace("%","").replace("&","")
            outputs = module.split("-> ")[1].split(", ")
            if self.name in outputs:
                memory[name] = "low"
        return memory
    
    def recieve_pulse(self, pulse, queue):
        source = pulse.source
        self.memory[source] = pulse.strength
        if "low" in "".join(self.memory.values()):
            for destination in self.destinations:
                queue.put(self.generate_pulse(source=self.name, destination=destination, strength="high"))
        else:
            for destination in self.destinations:
                queue.put(self.generate_pulse(source=self.name, destination=destination, strength="low"))

    def generate_pulse(self, source, destination, strength):
        return Pulse(source, destination, strength)
    
class Broadcaster:
    def __init__(self, data) -> None:
        self.name = data.split(" -> ")[0]
        self.destinations = data.split("-> ")[1].split(", ")

    def recieve_pulse(self, pulse, queue):
        for destination in self.destinations:
            queue.put(self.generate_pulse(source=self.name, destination=destination, strength="low"))

    def generate_pulse(self, source, destination, strength):
        return Pulse(source, destination, strength)

class Pulse:
    def __init__(self, source, destination, strength) -> None:
        self.source = source
        self.destination = destination
        self.strength = strength

module_map = {}
for module in module_list:
    if "%" in module:
        module_map[module.split(" -> ")[0][1:]] = FlipFlop(module)
    elif "&" in module:
        module_map[module.split(" -> ")[0][1:]] = Conjunction(module)
    else:
        module_map["broadcaster"] = Broadcaster(module)

action_queue = queue.Queue()

low_count = 0
high_count = 0

question_2 = True
question_2_found = False
button_presses = 0
            

for button_presses in range(0,1000):
    if button_presses % 1000 == 0:
        print(button_presses)
    button_presses += 1
    action_queue.put(Pulse("button", "broadcaster", "low"))
    while not action_queue.empty():
        current_pulse = action_queue.get()
        if current_pulse.strength == "low":
            low_count += 1
        else:
            high_count += 1
        try:
            current_module = module_map[current_pulse.destination]
        except KeyError:
            continue
        current_module.recieve_pulse(current_pulse, action_queue)
        if module_map["qt"].memory["mr"] == "low":
            continue
        else:
            print("mr", button_presses)

        if module_map["qt"].memory["kk"] == "low":
            continue
        else:
            print("kk", button_presses)

        if module_map["qt"].memory["gl"] == "low":
            continue
        else:
            print("gl", button_presses)

        if module_map["qt"].memory["bb"] == "low":
            continue
        else:
            print("bb", button_presses)


print("low_count: ", low_count)
print("high_count: ", high_count)
print("output :",  high_count * low_count)
answer = lcm(3907, 3931, 3989, 3967)
print("rx low triggered: ", answer)