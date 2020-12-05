printfn "Advent of Code 2020 Day 5"
// Day 5
let lines = System.IO.File.ReadAllLines("input.day5.txt") 
//let lines = System.IO.File.ReadAllLines("D4_kinput.txt") 
// let lines = System.IO.File.ReadAllLines("input.txt")
// let lines = System.IO.File.ReadAllLines("part2.txt") 
// printfn "%A" lines

let len = lines |> Seq.length
let width = lines.[0] |> Seq.length


printfn " Part 1 %d () 9: PM " 0
printfn " Part 2 %d () 9: PM " 0


let rec bb_to_int_fb (s:char list) valmin valmax =
    match s with
        | 'F'::tail -> bb_to_int_fb tail valmin ( (valmin + valmax) /2 )
        | 'B'::tail -> bb_to_int_fb tail ( (valmin + valmax) /2 ) valmax
        |  []       -> if valmin = valmax then valmin
                       else
                           // printfn "not single value %A %A " valmin valmax
                           valmin
        |  x::tail  -> bb_to_int_fb tail valmin valmax 

let rec bb_to_int_rl (s:char list) valmin valmax =
    match s with
        | 'L'::tail -> bb_to_int_rl tail valmin ( (valmin + valmax) /2 )
        | 'R'::tail -> bb_to_int_rl tail ( (valmin + valmax) /2 ) valmax
        |  []       -> if valmin = valmax then valmin
                       else
                           // printfn "not single value %A %A " valmin valmax
                           valmin
        |  x::tail  -> bb_to_int_rl tail valmin valmax 


let bb_to_int s = (bb_to_int_fb (s |>Seq.toList ) 0 128 ) * 8 + ( bb_to_int_rl (s |>Seq.toList )  0 8 )


let allboardingpasses_to_seats = seq {
    for i in lines do yield ( bb_to_int i )
    }

printfn "Part 1 Max seat = %A " ( allboardingpasses_to_seats |> Seq.max )

    
let sorted = allboardingpasses_to_seats |> Seq.sort |> Seq.toList
for i,j in (List.zip sorted.[0..(len-2)] sorted.[1..]) do
    if j - i > 1 then
        printfn "Part 2 here ? %d %d " i j

// printfn "t1 BFFFBBF %A  %A " ( 567/ 8 ) ( bb_to_int_fb ( "BFFFBBF" |> Seq.toList ) 0 128)
// printfn "t1 FFFBBBF %A  %A " ( 119/ 8 ) ( bb_to_int_fb ( "FFFBBBF" |> Seq.toList ) 0 128)
// printfn "t1 BBFFBBF %A  %A " ( 820/ 8 ) ( bb_to_int_fb ( "BBFFBBF" |> Seq.toList ) 0 128)

// printfn "t1 RRR %A  %A " 7  ( bb_to_int_rl ( "RRR" |> Seq.toList ) 0 8)
// printfn "t1 RRR %A  %A " 7  ( bb_to_int_rl ( "RRR" |> Seq.toList ) 0 8)
// printfn "t1 RLL %A  %A " 4  ( bb_to_int_rl ( "RLL" |> Seq.toList ) 0 8)
// printfn "t1 LLL %A  %A " 0  ( bb_to_int_rl ( "LLL" |> Seq.toList ) 0 8)

// printfn "t1 BFFFBBF %A  %A " ( 567/ 8 ) ( bb_to_int_fb ( "BFFFBBFRRR" |> Seq.toList ) 0 128)
// printfn "t1 FFFBBBF %A  %A " ( 119/ 8 ) ( bb_to_int_fb ( "FFFBBBFRRR" |> Seq.toList ) 0 128)
// printfn "t1 BBFFBBF %A  %A " ( 820/ 8 ) ( bb_to_int_fb ( "BBFFBBFRLL" |> Seq.toList ) 0 128)
// printfn "t1 BFFFBBF %A  %A " 7          ( bb_to_int_rl ( "BFFFBBFRRR" |> Seq.toList ) 0 128)
// printfn "t1 FFFBBBF %A  %A " 7          ( bb_to_int_rl ( "FFFBBBFRRR" |> Seq.toList ) 0 128)
// printfn "t1 BBFFBBF %A  %A " 4          ( bb_to_int_rl ( "BBFFBBFRLL" |> Seq.toList ) 0 128)

// printfn "t1 BFFFBBF %A  %A "  567       ( bb_to_int  "BFFFBBFRRR" )
// printfn "t1 FFFBBBF %A  %A "  119       ( bb_to_int  "FFFBBBFRRR" )
// printfn "t1 BBFFBBF %A  %A "  820       ( bb_to_int  "BBFFBBFRLL" )



(*
BFFFBBFRRR: row 70,  column 7, seat ID 567.
FFFBBBFRRR: row 14,  column 7, seat ID 119.
BBFFBBFRLL: row 102, column 4, seat ID 820.
*)

(*
   Part 1 Max seat = 828 
Part 2 here ? 564 566 
        0.12 real         0.10 user         0.01 sys

Compilation finished at Fri Dec  4 22:02:34

      --------Part 1--------   --------Part 2--------
Day       Time   Rank  Score       Time   Rank  Score
  5   00:54:22   7934      0   01:02:44   7273      0
  4   00:58:55   9120      0   02:16:28   9245      0
  3   00:09:50   2293      0   00:18:52   2837      0
  2   01:22:03   9557      0   01:45:06   9876      0
  1   17:23:49  63656      0   17:28:34  59000      0
  
*)
