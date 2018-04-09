class Pet:

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.direction = 0
        self.is_alive = True
        self.is_revived = True
        self.happiness = 5

    def eat(self):
        if self.is_alive:
            print(self.name + " says 'Mmmmmm, so good and tasty!'")
        elif self.is_revived:
            print(self.name + " says 'Mmmmmm brains!'")
        else:
            print("Ummm...did you forget...I'm dead?")
            
            
    def sleep(self):
        if self.is_alive:
            print("I'm schleeep")
        elif self.is_revived:
            print(self.name + " says 'Do I really need to sleep?'")
        else:
            print("Hello? I'm already dead.")
            
    def play(self):
        if self.is_alive:
            print("Yeet!")
        elif self.is_revived:
            print(self.name + " says 'If I win I get to eat your brain, if you win I get to eat you brain.'")
        else:
            print("...")
            print("You idiot.")

    def rotate_right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0

    def rotate_left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1

    def kill(self, other):
        print(self.name + " attacks " + other.name +"!")
        print(other.name + " goes 'oof' and dies.")
        other.is_alive = False

    def revive(magic, other):
        print(magic.name + " revives " + other.name + ".")
        print(other.name + " comes back as zombie!")
        other.is_alive = False
        other.is_revived = True

    def revengekill(other, self):
        print(other.name + " kills " + self.name +"!")
        print(self.name + " got what they deserve and is now dead.")
        self.is_alive = False
        self.is_revived = False

    def hug(self, other):
        if self.is_alive:
            print(self.name + " hugs " + other.name +"!")
            other.happiness += 1
            print(other.name + " says, 'I'm like " + str(other.happiness) + " happy now.")        
        elif self.is_revived:
            print(self.name + " says 'I'm dead inside.'")
        else:
            print("I can't move.")
            
    def __repr__(self):
        return "Name: " + self.name + \
               " [x=" + str(self.x) + \
               ", y=" + str(self.y) + \
               ", d=" + str(self.direction) + "]"
    
pet1 = Pet("Emma")
pet2 = Pet("Shane")
pet3 = Pet("Enrique")
