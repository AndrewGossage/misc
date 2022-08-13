import Text.Printf
import Data.Time.Clock

linreg :: [Double] -> [Double] -> Double -> Double
linreg a b c = sum (zipWith(*) a b) + c

for_loop :: Double -> Double -> Double 
for_loop x y= if ((linreg [2.4,6.9] [2.9, 4.4] 2 ) > 0 && (x > 0.0)) then for_loop (x-1.0) (y+1.0) else 0

main:: IO()
main = do
    now <- getCurrentTime
    let f = for_loop 10000000.0 0.0
    putStrLn (show f)
    end <- getCurrentTime
    let t =  diffUTCTime end now

    let s = nominalDiffTimeToSeconds  t
    putStrLn (show s)

