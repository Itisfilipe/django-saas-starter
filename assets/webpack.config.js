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
