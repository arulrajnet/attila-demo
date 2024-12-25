Title: Code block for markdown
Date: 2015-11-01 00:45
Author: pelican
Tags: General
Slug: code-blocks-for-markdown
Status: published
disqus_identifier: /2015/11/code-blocks-for-markdown.html


Wafer gummies lollipop pastry cotton candy chocolate cake sweet roll.
Cupcake caramels brownie gummi bears. Sweet fruitcake chocolate bear
claw cake liquorice bear claw lemon drops cheesecake. Sweet sesame snaps
pie halvah.


```js
function codestyling() {
    $('pre code').each(function(i, e) {
        var code = $(this);
        var lines = code.html().split(/\n/).length;
        var numbers = [];
        for (i = 1; i < lines; i++) {
            numbers += '<span class="line">' + i + '</span>';
        }
        code.parent().append('<div class="lines">' + numbers + '</div>');
    });
}
codestyling();
```

Another JavaScript code block

```javascript
let cheese = 'Cheddar';

if (cheese) {
  console.log('Yay! Cheese available for making cheese on toast.');
} else {
  console.log('No cheese on toast for you today.');
}
```

Here is the yaml

```yaml
include:
   - infra.yaml
services:
  web:
    build: .
    ports:
      - "8000:5000"
    develop:
      watch:
        - action: sync
          path: .
          target: /code
```

Here is the python code

```python
import time

import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello World! I have been seen {count} times.\n'
```

Here is the JSON

```json
{
    "name": "John",
    "age": 30,
    "cars": {
        "car1": "Ford",
        "car2": "BMW",
        "car3": "Fiat"
    }
}
```

Here is the golang code

```go
package main

import "fmt"

func plus(a int, b int) int {
    return a + b
}

func plusPlus(a, b, c int) int {
    return a + b + c
}

func main() {
    res := plus(1, 2)
    fmt.Println("1+2 =", res)

    res = plusPlus(1, 2, 3)
    fmt.Println("1+2+3 =", res)
}
```

Jelly beans pudding oat cake pie. Cupcake cupcake oat cake candy lemon drops marzipan icing. Dessert topping croissant fruitcake sesame snaps. Cotton candy sweet danish sweet roll sweet sugar plum donut. Bear claw gingerbread cake donut chocolate bar topping cake fruitcake fruitcake. Ice cream icing chupa chups cupcake jelly-o candy. Croissant jujubes topping tart soufflé pudding. Cheesecake caramels icing. Cake jelly-o chocolate cake sugar plum carrot cake lollipop bonbon.


```bash
#!/bin/bash
file1="file1.txt"
file2="file2.txt"
if cmp -s "$file1" "$file2"; then
    echo "Files are identical."
else
    echo "Files are different."
fi
```
