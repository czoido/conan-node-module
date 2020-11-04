# conan-node-module

This project is just a simple example on how a Conan custom generator can be used to handle dependencies when working with native node modules compiled with node-gyp.

The conan generator for this project is in: https://github.com/czoido/conan-gyp-generator Include the
generated conanbuildinfo.gyp in your project adding the dependencies in the bindings.gyp file:

```json
{
    "targets": [{
        "target_name": "conan_node_module",
        "sources": ["main.cpp"],
        "include_dirs": ["<!(node -e \"require('nan')\")"],
        "dependencies": ["<(module_root_dir)/conan_build/conanbuildinfo.gyp:yaml-cpp"],
        "conditions": [[
            "OS=='mac'", {
                "xcode_settings": {
                    "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
                }
            }
        ]]
    }]
}
```

```bash
git clone git@github.com:czoido/conan-node-module.git
mkdir conan_build && cd conan_build
conan install .. && cd ..
npm install
```

If you are using this module in electron you may want to build for it:

```bash
HOME=~/.electron-gyp node-gyp rebuild --target=10.1.5 --arch=x64 --dist-url=https://electronjs.org/headers
```