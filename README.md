# conan-node-module

``` bash
mkdir conan_build && cd conan_build
conan install .. && cd ..
npm install
HOME=~/.electron-gyp node-gyp rebuild --target=10.1.5 --arch=x64 --dist-url=https://electronjs.org/headers
```