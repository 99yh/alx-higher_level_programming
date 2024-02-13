## Why JavaScript programming is amazing
### How to create an object in JavaScript
### What this means
### What undefined means
### Why the variable type and scope is important
### What is a closure
A closure is a function having access to the parent scope, even after the parent function has closed.
```js
var countGenerator = function () {
  var n = 0;
  var count = function () { // this function is the closure
    n = n + 1;
    return n;
  };

  return count; // give the closure to be used
};

var count = countGenerator(); // a closure is created assigned to 'count'
// we can use the closure and it can access its own lexical environment (aka scope)
count(); // # 1
count(); // # 2
count(); // # 3

var count2 = countGenerator();
count2(); // # 1
count2(); // # 2

count(); // # 4

// JavaScript is AMAZING
```

### What is a prototype
### How to inherit an object from another
