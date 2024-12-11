print("==============================")

input_filepath = "./input_09.txt"
example_filepath = "./example_09.txt"
example_filepath2 = "./example_09_2.txt"

class Disk:
    def __init__(self, filepath):
        self.filepath = filepath
        self.input_array = open(filepath).read()
        self.get_full_array()


    def get_full_array(self):
        self.array = []
        for i, element in enumerate(self.input_array):
            if i % 2 == 0:
                self.array += int(element) * [int(i/2)]
            else:
                self.array += int(element) * ["."]

    def defrag1(self):
        while "." in self.array:
            if self.array[-1] == ".":
                self.array.pop(-1)
                continue
            for i, el in enumerate(self.array):
                if el == ".":
                    break
            self.array[i] = self.array[-1]
            self.array.pop(-1)

    def defrag2(self):
        current_data_val = None
        current_data_len = 0
        current_empty_length = 0
        for i_rev, el_rev in enumerate(self.array[::-1]):
            if el_rev == "." and current_data_val is None:
                continue
            elif el_rev != "." and current_data_val is None:
                current_data_val = el_rev
                current_data_len += 1
            elif el_rev == current_data_val:
                current_data_len += 1
            elif el_rev == "." or el_rev != current_data_val:
                for i, el in enumerate(self.array[:-i_rev]):
                    if el != ".":
                        current_empty_length = 0
                        continue
                    if el == ".":
                        if current_empty_length == 0:
                            start_index = i
                        current_empty_length += 1
                        if current_data_len > current_empty_length:
                            continue
                        else:
                            k = 1
                            for j in range(start_index,start_index+current_data_len):
                                self.array[j] = current_data_val
                                self.array[-i_rev-k+current_data_len] = "."
                                k += 1
                            if el_rev == ".":
                                current_data_val = None
                                current_data_len = 0
                            else:
                                current_data_val = el_rev
                                current_data_len = 1
                            current_empty_length = 0
                            break
                else:
                    if el_rev == ".":
                        current_data_val = None
                        current_data_len = 0
                    else:
                        current_data_val = el_rev
                        current_data_len = 1
                    current_empty_length = 0

    def checksum(self):
        self.checksum_total = 0
        for i, num in enumerate(self.array):
            try:
                self.checksum_total += i*num
            except:
                continue

example = Disk(example_filepath)
input = Disk(input_filepath)
example_2 = Disk(example_filepath2)

part_1 = False
part_2 = not part_1


if part_1:
    print("Part 1")
    example.defrag1()
    input.defrag1()
elif part_2:
    print("Part 2")
    example.defrag2()
    input.defrag2()
    example_2.defrag2()


example.checksum()
input.checksum()
example_2.checksum()

print("Example: ", example.checksum_total, "\n\n")
print("Input solution: ", input.checksum_total)
print("Example: ", example_2.checksum_total, "\n\n")
print("==============================")
