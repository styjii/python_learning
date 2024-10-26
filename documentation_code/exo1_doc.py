""""Random integer number"""
import random

def intRandom() :
    """random one integer number

    Returns:
        int : random intiger
    """
    return random.randint(0, 100)

def intRandoms(n) :
    """random multiple integer number

    Args:
        n (int): number of the integer number

    Returns:
        list[int]: random intiger
    """
    return [intRandom() for _ in range(n)]

if __name__ == "__main__" :
    print(intRandoms(10))