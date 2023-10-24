## Classes and Objects.

"first-class everything", "everything" is treated the same way, everything is a class: functions and methods are values just like lists, integers or floats. Each of these are instances of their corresponding classes.

"self" is not a Python keyword. It's just a naming convention!

Data Abstraction = Data Encapsulation + Data Hiding

Encapsulation is seen as the bundling of data with the methods that operate on that data.
Encapsulation is often accomplished by providing getters and setters

Information hiding on the other hand is the principle that some internal information or data is "hidden", so that it can't be accidentally changed.

Private attributes should only be used by the owner, i.e. inside of the class definition itself.
Protected (restricted) Attributes may be used, but at your own risk. Essentially, they should only be used under certain conditions.
Public Attributes can and should be freely used.

https://python-course.eu/oop/object-oriented-programming.php


"There should be one-- and preferably only one --obvious way to do it." (see Zen of Python)
