class NinjaBelt:

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.users = []

    def __str__(self):
        return f"{self.name.title()} ({self.score} pt)"

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"('{self.name}', {self.score})"
        )

    def __eq__(self, other):
        return self.score == other.score

    def __gt__(self, other):
        return self.score > other.score

    def __len__(self):
        return len(self.users)

    def __getitem__(self, position):
        return self.users[position]

    def __call__(self):
        print("I am callable")

    def __enter__(self):
        print("upper slice of bread")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("lower slice of bread")

    def __hash__(self):
        # for demo only, can be expensive
        return hash((self.name, self.score))
