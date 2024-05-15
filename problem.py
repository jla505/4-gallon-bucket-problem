class Buckets:
    def __init__(self, capacity1, capacity2):
        self.capacity1 = capacity1
        self.capacity2 = capacity2
        self.current1 = 0
        self.current2 = 0

    def fill_bucket1(self):
        self.current1 = self.capacity1

    def fill_bucket2(self):
        self.current2 = self.capacity2

    def empty_bucket1(self):
        self.current1 = 0

    def empty_bucket2(self):
        self.current2 = 0

    def pour_bucket1_to_bucket2(self):
        space_left_in_bucket2 = self.capacity2 - self.current2
        if self.current1 <= space_left_in_bucket2:
            self.current2 += self.current1
            self.current1 = 0
        else:
            self.current1 -= space_left_in_bucket2
            self.current2 = self.capacity2

    def pour_bucket2_to_bucket1(self):
        space_left_in_bucket1 = self.capacity1 - self.current1
        if self.current2 <= space_left_in_bucket1:
            self.current1 += self.current2
            self.current2 = 0
        else:
            self.current2 -= space_left_in_bucket1
            self.current1 = self.capacity1

    def is_solution(self):
        return self.current1 == 4 or self.current2 == 4

def water_jug_problem():
    buckets = Buckets(3, 5)
    steps = 0

    while not buckets.is_solution() and steps < 15:
        if buckets.current1 == 0:
            buckets.fill_bucket1()
        elif buckets.current1 > 0 and buckets.current2 < buckets.capacity2:
            buckets.pour_bucket1_to_bucket2()
        elif buckets.current2 == buckets.capacity2:
            buckets.empty_bucket2()
        steps += 1

    if buckets.is_solution():
        print("4 gallons of water fetched successfully in less than 15 steps!")
    else:
        print("Solution not found within 15 steps.")

water_jug_problem()
