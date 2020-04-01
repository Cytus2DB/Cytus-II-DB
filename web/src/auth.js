export default () => {
    const now = new Date();
    const md5 = require('js-md5');
    const AUTH = (now.getMonth() == 3 && now.getDate() == 1)
                ?'620dfa49631a07e82f2d86156e1810ae'
                :'7e3160ababa68617f3797335800f0b4e';
    return md5(localStorage['auth']) === AUTH;
}