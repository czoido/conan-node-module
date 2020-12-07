{
    "targets": [{
		"cflags" : ["-std=c++11", "-Wall", "-Wextra", "-Wno-unused-parameter", "-fexceptions"],
		"cflags_cc" : ["-std=c++11", "-Wall", "-Wextra", "-Wno-unused-parameter", "-fexceptions"],
		"defines": [ "V8_DEPRECATION_WARNINGS=1" ],
        "target_name": "conan_node_module",
        "sources": ["main.cpp"],
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