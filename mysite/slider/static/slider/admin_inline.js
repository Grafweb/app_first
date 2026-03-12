(function () {
  'use strict';

  // Fields that depend on link_type selection
  var FIELD_MAP = {
    internal_page:    ['page_link'],
    internal_article: ['article_link'],
    external:         ['external_url', 'link_new_tab'],
  };
  var ALL_DEPENDENT = ['page_link', 'article_link', 'external_url', 'link_new_tab'];

  function getRow(inlineDiv, fieldName) {
    return inlineDiv.querySelector('.field-' + fieldName);
  }

  function applyVisibility(inlineDiv, selectedType) {
    ALL_DEPENDENT.forEach(function (field) {
      var row = getRow(inlineDiv, field);
      if (!row) return;
      var visible = FIELD_MAP[selectedType] && FIELD_MAP[selectedType].indexOf(field) !== -1;
      row.style.display = visible ? '' : 'none';
    });
  }

  function initInline(inlineDiv) {
    var select = inlineDiv.querySelector('select[name$="-link_type"]');
    if (!select) return;
    applyVisibility(inlineDiv, select.value);
    select.addEventListener('change', function () {
      applyVisibility(inlineDiv, this.value);
    });
  }

  function initAll() {
    document.querySelectorAll('.inline-related').forEach(function (div) {
      initInline(div);
    });
  }

  // Handle dynamically added inlines (Add another)
  document.addEventListener('formset:added', function (e) {
    initInline(e.target);
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAll);
  } else {
    initAll();
  }
})();
