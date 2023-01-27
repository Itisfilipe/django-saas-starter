/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*
         * Root templates folder
         * app template folder root
         * app template folder subfolders
         */
        '../templates/**/*.html',
        '../apps/*/templates/**/*.html',

        /* Ignore any JavaScript in node_modules folder. */
        '!./node_modules',
        /* Ignore webpack generate file. */
        '!../templates/webpack_js_css.html',
        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../apps/**/*.py',
        // '../../core/**/*.py'
    ],
    theme: {
        extend: {},
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/line-clamp'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
