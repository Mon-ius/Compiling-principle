


function addTestEvents ($test) {
  $test.bind('stay', function() {
    var $test = $(this).closest('.test');
    var $ghost = $test.find('.ghost');
    if ($ghost.length) {
      $test.find('.box:not(.ghost)').remove();
      $test.find('.ghost').removeClass('ghost');
    }
  });
  $test.bind('leave', function() {
    var $test = $(this).closest('.test');
    $test.trigger('reset');
    var $box = $test.find('.box:not(.ghost)');
    var $ghost = $box.clone().addClass('ghost').appendTo($test.find('.area'));
    $test.data('code').fn($box, $test);
  });
  }
function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function Ein(s) {
  var $s = $('#test-' + s);
  $s.trigger('stay');
}
async function Eout(s) {
  var $s = $('#test-' + s);
  $s.trigger('leave');
}
async function Movout(s,t) {
  Eout(s);
  await sleep(100);
  Ein(t);
}

function test(n,name,fn) {
  var i = n-$('.tests .cat').length;
  var $pre = $('<div class="col-md-12 col-xs-12 cat"></div>')
  var $test = $('<div class="test"><div class="area"><div class="box"></div></div><br>');
  if (i < 10) j = 0; else j = '';
  var $button1 = $('<button type="button" class="btn btn-default btn-sm controller" style="margin-right: 5px" id="u-'+i+'"><span class="glyphicon glyphicon-menu-up" aria-hidden="true"></span></button><br><span class="badge">' +j+ i+'</span><br>');
  var $button2 = $('<button type="button" class="btn btn-default btn-sm controller" id="d-' + i +'"><span class="glyphicon glyphicon-menu-down" aria-hidden="true"></span></button>');
    $pre.append($test);
    $pre.append($button1);
    $pre.append($button2);
  var m = fn.toString().match(/\{([\s\S]*)\}$/);
  var code = m[1];
  $test.attr('id', 'test-'+i);
  $test.data('code', {fn: fn});
  addTestEvents($test);
  $temp = $('.tests').append($pre)
}
$(document).ready(function () {
  window.once=true;
  window.es=1;

});





