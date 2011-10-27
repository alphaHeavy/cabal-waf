module Lib3 (lib3) where

import Lib1 (lib1)
import Lib2 (lib2)

lib3 :: Int
lib3 = lib1 - 4 * lib3

