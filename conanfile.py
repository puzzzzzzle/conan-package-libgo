from conans import ConanFile, CMake, tools
from distutils.dir_util import copy_tree

class LibgoConan(ConanFile):
    name = "libgo"
    version = "v3.1-stable"
    author = "tao_test"
    license = "MIT"
    url = "https://github.com/yyzybb537/libgo"
    description = "conan packge for libgo"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"

    def source(self):
        # self.run("git clone --recursive https://github.com/yyzybb537/libgo")
        self.run("git clone  https://github.com/yyzybb537/libgo")
        copy_tree("libgo", ".")
        self.run("git reset --hard 5d4f365")
        # self.run("git submodule update --init --recursive")

    def build(self):
        cmake = CMake(self)
        shared_options = "-DBUILD_DYNAMIC=ON" if self.options.shared else "-DBUILD_DYNAMIC=OFF"
        self.run("cmake %s %s" % (cmake.command_line, shared_options))
        self.run("cmake --build . %s -j8" % cmake.build_config)

    def collect_headers(self, include_folder):
        self.copy("*.h"  , dst="include", src=include_folder)
        self.copy("*.hpp", dst="include", src=include_folder)
        self.copy("*.inl", dst="include", src=include_folder)


    def package(self):
        self.collect_headers("libgo")
        self.copy("*.a"  , dst="lib", keep_path=False)
        self.copy("*.so" , dst="lib", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["libgo"]

