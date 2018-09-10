let mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Laravel application. By default, we are compiling the Sass
 | file for the application as well as bundling up all the JS files.
 |
 */
// mix.disableSuccessNotifications();
mix.js('staticfiles/js/uncompiled/app.js', 'panel/static/js/app.js')
    .sass('staticfiles/css/uncompiled/app.scss', 'panel/static/css/app.css')