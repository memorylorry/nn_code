var AssetsPlugin = require('assets-webpack-plugin')
const version = new Date().getTime();

module.exports = {
    entry: {
        MainPage: './src/MainPage.js',
    },
    output: {
        filename: '[name].' + version + '.js',
        publicPath: '/dist/'
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                loader: "babel-loader"
            },
            {
                test: /\.(png|svg|jpg|gif)$/,
                use: ["file-loader"]
            },
            {
                test: /\.(less|css)$/,
                use: [
                    'style-loader',
                    { loader: 'css-loader', options: { importLoaders: 1 } },
                    'less-loader'
                ]
            }
        ]
    },
    plugins: [
        //assets-webpack-plugin
        new AssetsPlugin({
            filename: 'dist/webpack.assets.js',
            processOutput: function (assets) {
                return 'window.WEBPACK_ASSETS = ' + JSON.stringify(assets);
            }
        })
    ],
    devServer: {
        historyApiFallback: true
    }
};