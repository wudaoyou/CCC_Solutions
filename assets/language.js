document.querySelectorAll('[data-set-language]').forEach(button => {
  button.addEventListener('click', () => {
    const language = button.dataset.setLanguage;
    document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
    document.querySelectorAll('[data-language]').forEach(panel => {
      panel.hidden = panel.dataset.language !== language;
    });
    document.querySelectorAll('[data-set-language]').forEach(control => {
      control.setAttribute('aria-pressed', String(control === button));
    });
  });
});
