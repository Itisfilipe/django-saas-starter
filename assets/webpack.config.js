const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = {
    entry: path.resolve(__dirname, './src/javascript.js'),
    output: {
        filename: 'javascript.js',  // output bundle file name
        path: path.resolve(__dirname, './dist'),  // path to our Django dist directory
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'styles.css',
        }),
        new HtmlWebpackPlugin({
            filename: '../../templates/webpack_js_css.html',
            inject: false,
            hash: true,
            templateContent: ({htmlWebpackPlugin}) => {
                // Get the hash from the generated assets
                const hash = htmlWebpackPlugin.files.js[0].split('?')[1];
                return `
                    {% load static %}
                    <link rel="stylesheet" href="{% static 'styles.css' %}?${hash}" />
                    <script src="{% static 'javascript.js' %}?${hash}" defer></script>
                `;
            }
        })
    ],
    module: {
        rules: [
            {
                test: /\.js$/i,
                include: path.resolve(__dirname, './src'),
                use: 'babel-loader',
            },
            {
                test: /\.css$/i,
                include: path.resolve(__dirname, './src'),
                use: [MiniCssExtractPlugin.loader, 'css-loader', 'postcss-loader'],
            },
        ],
    },
    watchOptions: {
        ignored: [path.resolve(__dirname, '../templates/webpack_js_css.html')],
    }
};
