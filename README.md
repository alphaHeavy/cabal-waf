Basic cabal support for waf. This builds whole source trees to a private sandbox (much like cabal-dev) and supports package level parallel builds.

Set an alias so waf works anywhere:

    destroyer:cabal-waf nhowell$ alias waf=$PWD/waf

Run configure from the root, it only needs to be done once:

    destroyer:cabal-waf nhowell$ waf configure
    Setting top to                           : /Source/cabal-waf 
    Setting out to                           : /Source/cabal-waf/build 
    Checking for program cabal               : /usr/bin/cabal 
    Checking for program ghc-pkg             : /usr/bin/ghc-pkg 
    Created package database                 : /Source/cabal-waf/build/package.conf.d 
    'configure' finished successfully (0.020s)

Then run 'waf' or 'waf build' from the root to build the full tree. You can also do this in any subdirectory but it will only build child directories, not any ancestors.

    destroyer:cabal-waf nhowell$ waf
    Waf: Entering directory `/Source/cabal-waf/build'
    [ 1/22] cabal_configure: example/lib1/lib1.cabal -> build/example/lib1/setup-config
    [ 2/22] cabal_build: build/example/lib1/setup-config -> build/example/lib1/package.conf.inplace
    Preprocessing library lib1-0.1...
    Building lib1-0.1...
    [1 of 1] Compiling Lib1             ( Lib1.hs, /Source/cabal-waf/build/example/lib1/build/Lib1.o )
    [1 of 1] Compiling Lib1             ( Lib1.hs, /Source/cabal-waf/build/example/lib1/build/Lib1.p_o )
    Registering lib1-0.1...
    [ 3/22] cabal_copy: build/example/lib1/package.conf.inplace
    [ 4/22] cabal_register: build/example/lib1/package.conf.inplace
    [ 5/22] ghcpkg_register: build/example/lib1/package.conf.inplace
    lib1-0.1: Warning: haddock-interfaces: /Source/cabal-waf/build/dist/doc/html/lib1.haddock doesn't exist or isn't a file
    lib1-0.1: Warning: haddock-html: /Source/cabal-waf/build/dist/doc/html doesn't exist or isn't a directory
    [ 6/22] cabal_touch: build/example/lib1/package.conf.inplace -> build/lib1.package
    [ 7/22] cabal_configure: example/lib2/lib2.cabal -> build/example/lib2/setup-config
    [ 8/22] cabal_build: build/example/lib2/setup-config -> build/example/lib2/package.conf.inplace
    Preprocessing library lib2-0.1...
    Building lib2-0.1...
    [1 of 1] Compiling Lib2             ( Lib2.hs, /Source/cabal-waf/build/example/lib2/build/Lib2.o )
    [1 of 1] Compiling Lib2             ( Lib2.hs, /Source/cabal-waf/build/example/lib2/build/Lib2.p_o )
    Registering lib2-0.1...
    [ 9/22] cabal_copy: build/example/lib2/package.conf.inplace
    [10/22] cabal_register: build/example/lib2/package.conf.inplace
    [11/22] ghcpkg_register: build/example/lib2/package.conf.inplace
    lib2-0.1: Warning: haddock-interfaces: /Source/cabal-waf/build/dist/doc/html/lib2.haddock doesn't exist or isn't a file
    lib2-0.1: Warning: haddock-html: /Source/cabal-waf/build/dist/doc/html doesn't exist or isn't a directory
    [12/22] cabal_touch: build/example/lib2/package.conf.inplace -> build/lib2.package
    [13/22] cabal_configure: example/lib3/lib3.cabal -> build/example/lib3/setup-config
    [14/22] cabal_build: build/example/lib3/setup-config -> build/example/lib3/package.conf.inplace
    Preprocessing library lib3-0.1...
    Building lib3-0.1...
    [1 of 1] Compiling Lib3             ( Lib3.hs, /Source/cabal-waf/build/example/lib3/build/Lib3.o )
    [1 of 1] Compiling Lib3             ( Lib3.hs, /Source/cabal-waf/build/example/lib3/build/Lib3.p_o )
    Registering lib3-0.1...
    [15/22] cabal_copy: build/example/lib3/package.conf.inplace
    [16/22] cabal_register: build/example/lib3/package.conf.inplace
    [17/22] ghcpkg_register: build/example/lib3/package.conf.inplace
    lib3-0.1: Warning: haddock-interfaces: /Source/cabal-waf/build/dist/doc/html/lib3.haddock doesn't exist or isn't a file
    lib3-0.1: Warning: haddock-html: /Source/cabal-waf/build/dist/doc/html doesn't exist or isn't a directory
    [18/22] cabal_touch: build/example/lib3/package.conf.inplace -> build/lib3.package
    [19/22] cabal_configure: example/exe/exe.cabal -> build/example/exe/setup-config
    [20/22] cabal_build: build/example/exe/setup-config -> build/example/exe/package.conf.inplace
    Preprocessing executables for exe-0.1...
    Building exe-0.1...
    [1 of 1] Compiling Main             ( exe.hs, /Source/cabal-waf/build/example/exe/build/exe/exe-tmp/Main.o )
    Linking /Source/cabal-waf/build/example/exe/build/exe/exe ...
    [21/22] cabal_copy: build/example/exe/package.conf.inplace
    [22/22] cabal_touch: build/example/exe/package.conf.inplace -> build/exe.package
    Waf: Leaving directory `/Source/cabal-waf/build'
    'build' finished successfully (13.995s)

Update a file and all dependencies will be rebuilt:

    destroyer:cabal-waf nhowell$ echo >> example/lib2/Lib2.hs 

Note: touch does not trigger rebuilds as waf checks the file contents, not timestamps.

    destroyer:cabal-waf nhowell$ waf
    Waf: Entering directory `/Source/cabal-waf/build'
    [ 8/22] cabal_build: build/example/lib2/setup-config -> build/example/lib2/package.conf.inplace
    Preprocessing library lib2-0.1...
    Building lib2-0.1...
    [1 of 1] Compiling Lib2             ( Lib2.hs, /Source/cabal-waf/build/example/lib2/build/Lib2.o )
    [1 of 1] Compiling Lib2             ( Lib2.hs, /Source/cabal-waf/build/example/lib2/build/Lib2.p_o )
    Registering lib2-0.1...
    [ 9/22] cabal_copy: build/example/lib2/package.conf.inplace
    [10/22] cabal_register: build/example/lib2/package.conf.inplace
    [11/22] ghcpkg_register: build/example/lib2/package.conf.inplace
    lib2-0.1: Warning: haddock-interfaces: /Source/cabal-waf/build/dist/doc/html/lib2.haddock doesn't exist or isn't a file
    lib2-0.1: Warning: haddock-html: /Source/cabal-waf/build/dist/doc/html doesn't exist or isn't a directory
    [12/22] cabal_touch: build/example/lib2/package.conf.inplace -> build/lib2.package
    [13/22] cabal_configure: example/lib3/lib3.cabal -> build/example/lib3/setup-config
    [14/22] cabal_build: build/example/lib3/setup-config -> build/example/lib3/package.conf.inplace
    Preprocessing library lib3-0.1...
    Building lib3-0.1...
    Registering lib3-0.1...
    [15/22] cabal_copy: build/example/lib3/package.conf.inplace
    [16/22] cabal_register: build/example/lib3/package.conf.inplace
    [17/22] ghcpkg_register: build/example/lib3/package.conf.inplace
    lib3-0.1: Warning: haddock-interfaces: /Source/cabal-waf/build/dist/doc/html/lib3.haddock doesn't exist or isn't a file
    lib3-0.1: Warning: haddock-html: /Source/cabal-waf/build/dist/doc/html doesn't exist or isn't a directory
    [18/22] cabal_touch: build/example/lib3/package.conf.inplace -> build/lib3.package
    [19/22] cabal_configure: example/exe/exe.cabal -> build/example/exe/setup-config
    [20/22] cabal_build: build/example/exe/setup-config -> build/example/exe/package.conf.inplace
    Preprocessing executables for exe-0.1...
    Building exe-0.1...
    Linking /Source/cabal-waf/build/example/exe/build/exe/exe ...
    [21/22] cabal_copy: build/example/exe/package.conf.inplace
    [22/22] cabal_touch: build/example/exe/package.conf.inplace -> build/exe.package
    Waf: Leaving directory `/Source/cabal-waf/build'
    'build' finished successfully (7.536s)

Rebuilds with no changes take a very short amount of time:

    destroyer:cabal-waf nhowell$ waf
    Waf: Entering directory `/Source/cabal-waf/build'
    Waf: Leaving directory `/Source/cabal-waf/build'
    'build' finished successfully (0.008s)

