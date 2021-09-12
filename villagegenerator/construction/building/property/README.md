# Property

This is the README file for the property subpackage.

1. Usage
2. Testing
3. Examples

## Usage

1. Instantiate Property object
2. Build object at given location

### Instantiate Property object

```python
import property
from mcpi import vec3
from mcpi import minecraft

vec3_object = vec3.Vec3(0,0,0)
mc = minecraft.Minecraft.create()
entrance_edge = 0
biome = 0

property_object = property.Property(vec3_object, entrance_edge, biome, mc)
property_object.build()

## Testing

## Examples
