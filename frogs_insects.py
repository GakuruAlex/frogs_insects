from typing import List
def no_of_catches(frogs: List[int], tongues: List[int], insects: List[int])-> List[int]:
    """_Calculate how many insects a frog can catch from its given location, given frogs locations_

    Args:
        frogs (List[int]): _A list of where the frogs are located_
        tongues (List[int]): _A list of tongues each corresponding to a frog_
        insects (List[int]): _A list of locations for frogs_

    Returns:
        List[int]: _A list of number of insects each frog can catch from its given location_
    """
   
    catch_radii = [(max(0,combo[0] - combo[1]), combo[0]+ combo[1]) for combo in zip(frogs, tongues)]

    print(f"Catcn range: {catch_radii}")

    if len(insects) == 0 and len(frogs) > 0:
        return [0 for _ in frogs]
    elif len(frogs) == 0:
        return []
    else:
        return [count_catch(radius, insects) for radius in catch_radii]

def count_catch(radius: int, insects: List[int])-> int:
    return sum(map(lambda insect: radius[0] <= insect  and insect <= radius[1], insects))

def main()-> None:
    frogs: List[int] = list(map(int, input(f"Frogs locations: ").split(" ")))
    tongues: List[int] = list(map(int, input(f"Size of each frogs tongue: ").split(" ")))
    insects: list[int] = list(map(int, input(f"Insects location: ").split(" ")))

    print(f"List of number of insects caught by each frog: {no_of_catches(frogs=frogs, tongues=tongues, insects=insects)}")

if __name__ == "__main__":
    main()