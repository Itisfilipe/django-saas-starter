const tailwindcss = require('tailwindcss')('./tailwind.config.js');
const autoprefixer = require('autoprefixer');
const pImport = require('postcss-import');
const simpleVars = require('postcss-simple-vars');
const nested = require('postcss-nested');

module.exports = {
    plugins: [
        tailwindcss,
        pImport,
        simpleVars,
        nested,
        autoprefixer,
    ]
}
