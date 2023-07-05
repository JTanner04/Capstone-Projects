import pygame
import sys
import random
import torch
import torch.nn as nn
import torch.optim as optim

# Initialize Pygame
pygame.init()

# Set up the screen dimensions and grid size
screen_w = 800
screen_h = 600
grid_size = 20
grid_w = screen_w // grid_size
grid_h = screen_h // grid_size

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (124, 252, 0)


class Snake:
    def __init__(self):
        self.body = [(grid_w // 2, grid_h // 2)]
        self.direction = (0, 0)

    def update(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0], head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.body.pop()

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, green, (segment[0] * grid_size, segment[1] * grid_size, grid_size, grid_size))

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= grid_w or head[1] < 0 or head[1] >= grid_h:
            return True
        for segment in self.body[1:]:
            if head == segment:
                return True
        return False


class Food:
    def __init__(self):
        self.position = (random.randint(0, grid_w - 1), random.randint(0, grid_h - 1))

    def respawn(self):
        self.position = (random.randint(0, grid_w - 1), random.randint(0, grid_h - 1))

    def draw(self, screen):
        pygame.draw.rect(screen, red,
                         (self.position[0] * grid_size, self.position[1] * grid_size, grid_size, grid_size))


class AIPlayer:
    def __init__(self, snake, food):
        self.snake = snake
        self.food = food
        self.model = SnakeAIModel()
        self.criterion = nn.MSELoss()
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)

    def update(self):
        head = self.snake.body[0]
        food_pos = self.food.position

        input_tensor = torch.tensor([head[0], head[1], food_pos[0], food_pos[1]], dtype=torch.float32)
        output_tensor = self.model(input_tensor)
        target_tensor = torch.tensor([food_pos[0] - head[0], food_pos[1] - head[1]], dtype=torch.float32)

        self.train(input_tensor, target_tensor)

        # Get the current direction
        current_direction = self.snake.direction

        # Calculate the differences in position between the head and the food
        dx = food_pos[0] - head[0]
        dy = food_pos[1] - head[1]

        # Calculate the absolute differences
        abs_dx = abs(dx)
        abs_dy = abs(dy)

        # Check if the snake is closer to the food horizontally or vertically
        if abs_dx > abs_dy:
            # Move horizontally towards the food
            if dx > 0 and current_direction != (-1, 0):  # Move right
                self.snake.direction = (1, 0)
            elif dx < 0 and current_direction != (1, 0):  # Move left
                self.snake.direction = (-1, 0)
        else:
            # Move vertically towards the food
            if dy > 0 and current_direction != (0, -1):  # Move down
                self.snake.direction = (0, 1)
            elif dy < 0 and current_direction != (0, 1):  # Move up
                self.snake.direction = (0, -1)

    def train(self, state, target):
        output = self.model(state)
        loss = self.criterion(output, target)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()


class SnakeAIModel(nn.Module):
    def __init__(self):
        super(SnakeAIModel, self).__init__()
        self.fc1 = nn.Linear(4, 16)
        self.fc2 = nn.Linear(16, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


def main():
    # Set up the game window
    screen = pygame.display.set_mode((screen_w, screen_h))
    pygame.display.set_caption("Snake ML")
    clock = pygame.time.Clock()

    # Initialize game objects
    snake = Snake()
    food = Food()
    ai_player = AIPlayer(snake, food)

    # Initialize score
    score = 0

    # Start the game loop
    while True:
        # Reset the game
        snake = Snake()
        food = Food()
        ai_player.snake = snake
        ai_player.food = food
        score = 0

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Update the AI player and snake
            ai_player.update()
            snake.update()

            # Check for collision
            if snake.check_collision():
                run = False

            # Check if the snake ate the food
            if snake.body[0] == food.position:
                food.respawn()
                snake.body.append(snake.body[-1])
                score += 1

            # Draw game objects
            screen.fill(black)
            snake.draw(screen)
            food.draw(screen)
            pygame.display.update()

            # Delay to control the frame rate
            clock.tick(10)

        print("Score:", score)


if __name__ == '__main__':
    main()