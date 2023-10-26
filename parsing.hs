-- Program: LL Parser
-- Author: Alyssa
-- Date: 10/22/2023
-- Description: An LL parser for the
-- language of Kalee, using {q,c,u}

import System.Environment(getArgs)
 

processS :: String -> String

-- If empty, we can accept
processS [] = "Accept"

-- Break between the first letter and the rest of the word
processS (x:xs)
  |x == '-'  = processS xs
  |x == 'c'  = processC xs
  |x == 'q'  = processQ xs
  |x == 'u'  = processU xs
  |otherwise = "Reject"

  
processC :: String -> String
processC [] = "Accept"
processC (x:xs)
  |x == 'q'  = processC xs
  |x == 'u'  = processC xs
  |x == 'c'  = processC xs
  |otherwise = "Reject"

processQ :: String -> String
processQ [] = "Accept"
processQ (x:xs)
  |x == 'q'  = processB xs
  |x == 'u'  = processQ2 xs
  |x == 'c'  = processC xs
  |otherwise = "Reject"

processQ2 :: String -> String
processQ2 [] = "Accept"
processQ2 (x:xs)
  |x == 'u'  = processQ2 xs
  |x == 'q'  = processQ xs
  |x == 'c'  = processC xs
  |otherwise = "Reject"

processU :: String -> String
processU [] = "Accept"
processU (x:xs)
  |x == 'u'  = processB xs
  |x == 'q'  = processU2 xs
  |x == 'c'  = processC xs
  |otherwise = "Reject"

processU2 :: String -> String
processU2 [] = "Accept"
processU2 (x:xs)
  |x == 'q'  = processU2 xs
  |x == 'u'  = processU xs
  |x == 'c'  = processC xs
  |otherwise = "Reject"

processB :: String -> String
processB [] = "Accept"
processB (x:xs)
  |x == 'q'  = processB xs
  |x == 'u'  = processB xs
  |x == 'c'  = processC xs
  |otherwise = "Reject"



main :: IO()
main = do
  args <- getArgs
  let word = args !! 0
  putStrLn (processS word)