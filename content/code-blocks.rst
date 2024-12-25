Code Blocks
###########
:date: 2015-11-01 00:45
:author: pelican
:tags: General
:slug: code-blocks
:disqus_identifier: /2015/11/code-blocks.html

Wafer gummies lollipop pastry cotton candy chocolate cake sweet roll.
Cupcake caramels brownie gummi bears. Sweet fruitcake chocolate bear
claw cake liquorice bear claw lemon drops cheesecake. Sweet sesame snaps
pie halvah.

.. code-block:: javascript

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



Another JavaScript code block

.. code-block:: javascript

  var cheese = 'Cheddar';

  if (cheese) {
    console.log('Yay! Cheese available for making cheese on toast.');
  } else {
    console.log('No cheese on toast for you today.');
  }

Here is the yaml

.. code-block:: yaml
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


Here is the python code

.. code-block:: python
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


Here is the JSON

.. code-block:: json
    {
        "name": "John",
        "age": 30,
        "cars": {
            "car1": "Ford",
            "car2": "BMW",
            "car3": "Fiat"
        }
    }


Here is the golang code

.. code-block:: go
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


Jelly beans pudding oat cake pie. Cupcake cupcake oat cake candy lemon drops marzipan icing. Dessert topping croissant fruitcake sesame snaps. Cotton candy sweet danish sweet roll sweet sugar plum donut. Bear claw gingerbread cake donut chocolate bar topping cake fruitcake fruitcake. Ice cream icing chupa chups cupcake jelly-o candy. Croissant jujubes topping tart soufflé pudding. Cheesecake caramels icing. Cake jelly-o chocolate cake sugar plum carrot cake lollipop bonbon.


.. code-block:: bash

    #!/bin/bash
    file1="file1.txt"
    file2="file2.txt"
    if cmp -s "$file1" "$file2"; then
        echo "Files are identical."
    else
        echo "Files are different."
    fi
