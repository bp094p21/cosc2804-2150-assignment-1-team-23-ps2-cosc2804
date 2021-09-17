# Main Program Outline

1. Get Player Pos
2. Survey Land
3. Instantiate Matrix object
4. Iterate and Build components


## Get Player Pos

```
Input None
Output x1,y1,z1
```

## Survey land
Survey land surrounding player and find an area to place matrix.


```
Input x1,y1,z1
Output x2,y2,z2 of one corner of the matrix
```

- One corner coordinates of suitable area is sufficient to build the entire matrix

## Instantiate Matrix object
Instantiate Matrix object and give it the coordinates of corner and the biome of
surroundings

```
Input x2,y2,z2,biome
Output the Matrix object
```

## Iterate and Build components
Iterate through each element in Matrix object and build a House/Misc/Road object there, giving each component the coordinates of one corner and the biome.

```
Input x3,y3,z3, biome
Output the House/Road/Misc object
```

Two viable methods:
	1. Templating
	2. Randomized with conditions

## Templating
1. Select at random one of the Matrix templates
   where each Matrix component contains data about
what component should be built there and what each
side of that component should have. i.e. an
Entrance for a Property component. an Entrance for
a Misc component. Connecting edge to a House/Park/Road for a Road component.
2. Iterate through each of the Matrix elements and
   call the build function for the given component
class and append the new object to Matrix

## Randomized with conditions
1. Iterate through each of the Matrix elements and
   randomize what component will be built there
conditionally

Conditions should involve:
-	whether or not current Matrix element is a corner element, a perimeter element, first & corner element
-	which component is adjacent to the current
	element
-	what data adjacent components have in terms of its edges. Example: If current component is oftype Road and a House component is adjacent to it, it will check if the House component points to the current Matrix element. If it does, then it will know to build the appropriate edge that will connect nicely to that House

End
