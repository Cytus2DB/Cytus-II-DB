process.env.VUE_APP_VERSION = require('../version.json').version

module.exports = {
  chainWebpack: config => {
    config.plugin('html').tap(options => {
      options[0].title = "Cytus II DB";
      return options;
    });
  },

  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'en',
      localeDir: 'locales',
      enableInSFC: false
    }
  }
}
