# You're at the zoo... all the meerkats look weird. Something has gone terribly wrong - someone has gone and switched their heads and tails around!
# Save the animals by switching them back. You will be given an array which will have three values (tail, body, head). It is your job to re-arrange the array so that the animal is the right way round (head, body, tail).
# Same goes for all the other arrays/lists that you will get in the tests: you have to change the element positions with the same exact logics
# Simples!


def fix_the_meerkat(arr):
    # ordered = [["head", "body", "tail"]["heads", "body", "tails"]["top", "middle", "bottom"]["upper legs", "torso", "lower legs"]["sky", "rainbow", "ground"]]
    


print(fix_the_meerkat(["tail", "body", "head"]), ["head", "body", "tail"])
print(fix_the_meerkat(["tails", "body", "heads"]), ["heads", "body", "tails"])
print(fix_the_meerkat(["bottom", "middle", "top"]), ["top", "middle", "bottom"])
print(fix_the_meerkat(["lower legs", "torso", "upper legs"]), ["upper legs", "torso", "lower legs"])
print(fix_the_meerkat(["ground", "rainbow", "sky"]), ["sky", "rainbow", "ground"])