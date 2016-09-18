Code Blocks
###########
:date: 2015-11-01 00:45
:author: zutrinken
:tags: General
:slug: code-blocks

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

Jelly beans pudding oat cake pie. Cupcake cupcake oat cake candy lemon drops marzipan icing. Dessert topping croissant fruitcake sesame snaps. Cotton candy sweet danish sweet roll sweet sugar plum donut. Bear claw gingerbread cake donut chocolate bar topping cake fruitcake fruitcake. Ice cream icing chupa chups cupcake jelly-o candy. Croissant jujubes topping tart soufflé pudding. Cheesecake caramels icing. Cake jelly-o chocolate cake sugar plum carrot cake lollipop bonbon.
