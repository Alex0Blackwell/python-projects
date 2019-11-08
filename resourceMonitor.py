# Computer resource monitor
import psutil
import pygame

pygame.init()
myfont = pygame.font.SysFont('lucidaconsole', 20)


def writeText(text):
    textsurface = myfont.render(text, 1, (255, 255, 255))
    return textsurface


def avgCores(allCores):
    avg = 0
    counter = 0
    for el in allCores:
        avg += el
        counter += 1
    avg = round(avg / counter, 1)
    return avg


def main():
    screen = pygame.display.set_mode((325, 200))
    pygame.display.set_caption("Command Prompt?")
    screen.fill((0, 0, 0))

    while True:
        memPercent = psutil.virtual_memory().percent
        cpuPercent = psutil.cpu_percent(interval=1, percpu=True)

        memText = f"Memory: {memPercent}%"
        cpuText = f"CPU:    {avgCores(cpuPercent)}%"
        screen.fill((0, 0, 0))
        screen.blit(writeText("C:\\Users\\Alex\\Programming\\"), (0, 0))
        screen.blit(writeText("Hover mouse to update"), (0, 25))
        screen.blit(writeText("C:\\Users\\Alex\\Programming\\"), (0, 60))
        screen.blit(writeText(memText), (0, 85))
        screen.blit(writeText(cpuText), (0, 110))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()


main()
