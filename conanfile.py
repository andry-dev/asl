from conans import ConanFile, CMake, tools

class TewiConan(ConanFile):
    name = "asl"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/andry-dev/asl.git"
    description = "An easy to use, extendable, game engine"
    settings = "os", "compiler", "build_type", "arch"

    options = {
        "shared": [True, False],
    }

    default_options = {
        "shared": False,
    }

    generators = "cmake"
    exports_sources = "include/*"

    def build(self):
        cmake = CMake(self)
        self.run("cmake .. %s" % (cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)


    def package(self):
        self.copy("*", dst="include", src="include")

    def package_info(self):
        self.cpp_info.libs = ["asl"]

