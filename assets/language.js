(function () {
  'use strict';
  const supported = ['en', 'ko', 'ja', 'vi'];
  const normalize = value => typeof value === 'string' ? value.toLowerCase().split(/[-_]/)[0] : '';
  function chooseLanguage(requested, stored, languages) {
    for (const value of [requested, stored, ...(languages || [])]) {
      const language = normalize(value);
      if (supported.includes(language)) return language;
    }
    return 'en';
  }
  window.Cooing = { chooseLanguage };
  const root = document.documentElement;
  const explicit = root.dataset.language;
  const base = root.dataset.base;
  const route = root.dataset.route;
  let stored;
  try { stored = localStorage.getItem('cooing.language'); } catch (_) {}
  if (supported.includes(explicit)) {
    try { localStorage.setItem('cooing.language', explicit); } catch (_) {}
    return;
  }
  const query = new URLSearchParams(location.search);
  const language = chooseLanguage(query.get('lang'), stored, navigator.languages || [navigator.language]);
  location.replace(base + language + '/' + (route ? route + '/' : '') + location.hash);
})();
