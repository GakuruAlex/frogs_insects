from typing import List
def no_of_catches(frogs: List[int], tongues: List[int], insects: List[int])-> List[int]:
    catch_radii = list(map(lambda frog, tongue: frog + tongue , frogs, tongues))

    if len(insects) == 0 and len(frogs) > 0:
        return [0 for _ in frogs]
    elif len(frogs) == 0:
        return []
    else:
        return [count_catch(radius, insects) for radius in catch_radii]

def count_catch(radius: int, insects: List[int])-> int:
    return sum(map(lambda insect: insect <= radius, insects))

def main()-> None:
    frogs: List[int] = list(map(int, input(f"Frogs locations: ").split(" ")))
    tongues: List[int] = list(map(int, input(f"Size of each frogs tongue: ").split(" ")))
    insects: list[int] = list(map(int, input(f"Insects location: ").split(" ")))

    print(f"List of number of insects caught by each frog: {no_of_catches(frogs=frogs, tongues=tongues, insects=insects)}")

if __name__ == "__main__":
    main()