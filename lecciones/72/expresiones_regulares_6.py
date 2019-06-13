import re

codigos = [
    '''
    Lorem ipsum dolor sit amet, 42consectetur adipiscing elit.
    Maecenas leo erat, varius non laoreet sed, cursus ut tortor.
    Morbi maximus pulvinar ante, ut pulvinar ex malesuada blandit.
    Maecenas venenatis, sapien vitae sodales viverra, ante urna
    tincidunt tellus, a faucibus elit dui congue dui. Quisque congue
    sed ex in sollicitudin. Pellentesque luctus justo quis felis
    feugiat, et semper erat laoreet. Curabitur id dui arcu. Curabitur
    purus massa, placerat id pretium ac, ornare eleifend ante.
    ''',
    '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Maecenas 42leo erat, varius non laoreet sed, cursus ut tortor.
    Morbi maximus pulvinar ante, ut pulvinar ex malesuada blandit.
    Maecenas venenatis, sapien vitae sodales viverra, ante urna
    tincidunt tellus, a faucibus elit dui congue dui. Quisque congue sed
    ex in sollicitudin. Pellentesque luctus justo quis felis feugiat, et
    semper erat laoreet. Curabitur id dui arcu. Curabitur purus massa,
    placerat id pretium ac, ornare eleifend ante.
    ''',
    '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas
    leo erat, varius non laoreet sed, cursus ut tortor. Morbi maximus
    pulvinar ante, ut pulvinar ex malesuada blandit. Maecenas venenatis,
    sapien vitae sodales viverra, ante urna tincidunt tellus, a faucibus
    elit dui congue dui. Quisque congue sed ex in sollicitudin.
    Pellentesque luctus justo quis felis feugiat, et semper erat laoreet.
    Curabitur id dui arcu. Curabitur purus massa, placerat id pretium ac,
    ornare eleifend ante.
    ''']

[print(c, end="\n") for c in codigos if re.search("42", c)]
