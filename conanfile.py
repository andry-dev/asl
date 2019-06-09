from conans import ConanFile, CMake, tools

class AslConan(ConanFile):
    name = "asl"
    version = "0.1"
    license = "MIT"
    url = "https://github.com/andry-dev/asl.git"
    description = "Another support library"
    exports_sources = "include/*"
    no_copy_sources = True

    def package(self):
        self.copy("*")

    def package_id(self):
        self.info.header_only()
