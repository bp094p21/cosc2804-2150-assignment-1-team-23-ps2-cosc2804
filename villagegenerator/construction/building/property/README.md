# Property

This is the README file for the property subpackage.

1. Usage
2. Testing

## Usage

1. Instantiate architect
2. Give property specs to architect

### Instantiate Property object

```python
import property.architect as arch

architect = arch.Jin()      # or architect = arch.Architect()
```

### Give property specs to architect

```python
architect.give_specs(location_v3: v.Vec3, orientation: int, theme: str, mc: minecraft.Minecraft)
```

> Properties can be accessed through `architect.properties` or `architect.builder.properties`


## Testing

# TODO: Write test
1. Open server connection
2. Open minecraft and connect to server
3. Run `$ python3 architect.py`

