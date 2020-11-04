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