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
    screen = pygame.display.set_mode((1000, 200))
    pygame.display.set_caption("Alex Resource Monitor")
    screen.fill((0, 0, 0))

    while True:
        memPercent = psutil.virtual_memory().percent
        cpuPercent = psutil.cpu_percent(interval=1, percpu=True)

        memText = f"Memory: {memPercent}%"
        cpuText = f"CPU: {avgCores(cpuPercent)}%"
        screen.fill((0, 0, 0))
        screen.blit(writeText(memText), (0, 0))
        screen.blit(writeText(cpuText), (0, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            pygame.display.update()


main()
