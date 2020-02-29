export default () => {
    const md5 = require('js-md5');
    const AUTH = '7e3160ababa68617f3797335800f0b4e';
    return md5(localStorage['auth']) === AUTH;
}