(function() {
  var $albumV, $body, $win, SCREEN_DESKTOP, SCREEN_TABLET, generateMosaicGallery, setAlbumHeight;

  SCREEN_TABLET = 768;

  SCREEN_DESKTOP = 1199;

  $body = $('body');

  $win = $(window);

  $albumV = $('.album-vertical');

  generateMosaicGallery = function() {
    return $('.album-mosaic').each(function(_, el) {
      var fldGrd;
      return fldGrd = new FldGrd(el, {
        rowHeight: 450,
        rowHeightOrphan: function() {
          return 450;
        },
        itemSelector: '.album-mosaic-item',
        objSelector: 'img'
      });
    });
  };

  setAlbumHeight = function() {
    if ($win.width() >= SCREEN_TABLET && $albumV.length) {
      return $('.row', $albumV).height($win.height() - $albumV.offset().top);
    }
  };

  $(function() {
    var container, ps;
    container = document.querySelector('#ps');
    if (container) {
      ps = new PerfectScrollbar(container);
    }
    $('.js-product-files-toggle').on('click', function() {
      $(this).closest('.js-product-files').toggleClass('is-open');
      return false;
    });
    $('[data-responsive-nav-toggle-btn]').on('click', function(e) {
      e.preventDefault();
      return $body.toggleClass('responsive-nav--open');
    });
    if ($win.width() >= SCREEN_TABLET && $body.height() > $win.height() * 2) {
      $(window).on('scroll', function() {
        if ($(window).scrollTop() > $(window).height()) {
          return $('.btt').fadeIn("300");
        } else {
          return $('.btt').fadeOut("300");
        }
      });
    }
    if ($('.album-mosaic').length > 0) {
      $('.loader').hide();
      utils.detectIEEdge();
      $('.album-mosaic').animate({
        opacity: 1
      }, 500);
      generateMosaicGallery();
    }
    if ($(".contact-page").length > 0) {
      $('textarea.js-auto-size').textareaAutoSize();
      $("#contact_form").on("submit", function(e) {
        window.contactForm.submit();
        return e.preventDefault();
      });
    }
    return setAlbumHeight();
  });

  $(window).on('resize', function() {
    if ($('.album-mosaic').length > 0) {
      generateMosaicGallery();
    }
    return setAlbumHeight();
  });

  $(window).on("load", function() {
    if ($('.album-mosaic').length > 0) {
      return generateMosaicGallery();
    }
  });

}).call(this);
