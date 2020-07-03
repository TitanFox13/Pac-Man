class Solver:

    def __init__(self, start, end, grid, enemies):
        # start and end of the maze
        self.start = start
        self.end = end
        # list of blocks yet to be discovered
        self.open_list = []
        # list of block that have already been evaluated
        self.closed_list = []
        # current block being evaluated
        self.current = None
        # a copy of current block used in finding path
        self.fake_current = None
        # index in the open list of the current block
        self.current_index = 0
        # path to the end
        self.path = []
        # grid the algorithm should work in
        self.grid = grid
        # list of all enemies
        self.enemies = enemies

    # function that will get the current block
    def get_current(self):
        # setting current to first element in open list
        self.current = self.open_list[0]
        # setting index back to 0
        self.current_index = 0
        for i, block in enumerate(self.open_list):
            # choosing the block with the lowest F cost
            if block.f_cost < self.current.f_cost:
                # setting current to the block with the lowest F cost
                self.current = block
                # choosing index of the current in the open list
                self.current_index = i
        # deleting current from the open list and adding it to the closed list
        self.closed_list.append(self.open_list.pop(self.current_index))

    # checking if the path was found
    def check_for_found_path(self):
        # if the Xs and Ys match then we found the path
        if self.current.grid_x == self.end.x and self.current.grid_y == self.end.y:
            # using backtracking to show the path
            self.fake_current = self.current
            while self.fake_current is not None:
                self.path.append(self.fake_current)
                self.fake_current = self.fake_current.parent
            # reversing the path, so its from the beginning
            self.path = self.path[::-1]
            return

    # setting up parents correctly based on G costs
    def set_parents_correctly(self):
        # for each neighbour that is not in the closed list
        for neighbour in self.current.neighbours:
            if neighbour not in self.closed_list:
                # if in open list
                if neighbour in self.open_list:
                    # if his parents G cost is bigger than current G cost
                    if neighbour.parent.g_cost > self.current.g_cost:
                        # his parent is now current
                        neighbour.parent = self.current
                # if not in open list nor closed list
                else:
                    # adding neighbour to the open list
                    self.open_list.append(neighbour)
                    # setting current as the parent of the neighbour
                    neighbour.parent = self.current
                    # setting all costs of the neighbour
                    neighbour.get_all_costs(self.end)

    # resetting the values of each block
    def reset(self):
        for row in self.grid:
            for block in row:
                block.reset()

    def solve(self):

        # setting current block
        self.get_current()

        # checking if we found the path
        self.check_for_found_path()

        # getting neighbours of the current
        self.current.get_neighbours(self.grid, self.enemies)

        # checking if there is a shorter path to the neighbour using G costs
        self.set_parents_correctly()

    # solving the maze
    def solve_run(self):

        # adding the start to the open list
        self.open_list.append(self.start)

        # only running if there are still some block in the open list, if there are not, there is no path
        while len(self.open_list) > 0:

            self.solve()
