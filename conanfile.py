from conans import ConanFile, CMake, tools

class TewiConan(ConanFile):
    name = "asl"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/andry-dev/asl.git"
    description = "An easy to use, extendable, game engine"
    exports_sources = "include/*", "CMakeLists.txt"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*", src="include", dst="include")

    def package_info(self):
        self.info.header_only()
